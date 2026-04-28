"""
Stack Profiler: Converting Stack Samples to Trace Events

A sampling profiler takes snapshots of the active call stack at specific times.
This module converts those samples into a timeline of start/end events.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Sample:
    """
    Represents a single stack sample taken at a specific time.

    Attributes:
        ts: The timestamp when this sample was taken.
        stack: The call stack from outermost (root) to innermost (leaf).
               For example: ["main", "foo", "bar"] means main called foo,
               which called bar, and bar is currently executing.
    """
    ts: float
    stack: List[str]


@dataclass
class Event:
    """
    Represents a function start or end event.

    Attributes:
        kind: Either "start" or "end" indicating the event type.
        ts: The timestamp when this event occurred.
        name: The name of the function that started or ended.
    """
    kind: str
    ts: float
    name: str


def convert_samples_to_events(samples: List[Sample]) -> List[Event]:
    """
    Convert a list of stack samples into a list of trace events.

    Given samples sorted by time, this function detects when functions
    start and end by comparing consecutive stack snapshots.

    Algorithm:
    - Compare each pair of consecutive samples
    - Find the common prefix (shared call chain from root)
    - Generate "end" events for functions that disappeared (bottom-up order)
    - Generate "start" events for new functions (top-down order)

    Args:
        samples: A list of Sample objects sorted by timestamp.
                 Each sample contains a timestamp and a call stack.

    Returns:
        A list of Event objects representing function starts and ends,
        ordered by timestamp. Does NOT generate end events for functions
        still on the stack after the last sample.

    Example:
        >>> samples = [
        ...     Sample(1.0, ["main"]),
        ...     Sample(2.5, ["main", "func1"]),
        ...     Sample(3.1, ["main"])
        ... ]
        >>> events = convert_samples_to_events(samples)
        >>> # Returns: [Event("start", 1.0, "main"),
        >>> #          Event("start", 2.5, "func1"),
        >>> #          Event("end", 3.1, "func1")]
    """
    events = []
    
    if not samples:
        return events
    
    # First sample: all frames are starting (top-down order)
    prev_sample = samples[0]
    for func_name in prev_sample.stack:
        events.append(Event("start", prev_sample.ts, func_name))
    
    # Compare consecutive samples
    for i in range(1, len(samples)):
        curr_sample = samples[i]
        prev_stack = prev_sample.stack
        curr_stack = curr_sample.stack
        
        # Find the common prefix length
        common_len = 0
        for j in range(min(len(prev_stack), len(curr_stack))):
            if prev_stack[j] == curr_stack[j]:
                common_len += 1
            else:
                break
        
        # Generate end events for functions that disappeared (bottom-up)
        for j in range(len(prev_stack) - 1, common_len - 1, -1):
            events.append(Event("end", curr_sample.ts, prev_stack[j]))
        
        # Generate start events for new functions (top-down)
        for j in range(common_len, len(curr_stack)):
            events.append(Event("start", curr_sample.ts, curr_stack[j]))
        
        prev_sample = curr_sample
    
    return events


def convert_samples_to_debounced_events(samples: List[Sample], n: int) -> List[Event]:
    """
    Convert stack samples to events, filtering out short-lived functions.

    This is similar to convert_samples_to_events, but only generates events
    for functions that appear in at least N consecutive samples. This helps
    reduce noise from very fast function calls.

    A frame is considered "consecutive" only if:
    - It appears at the exact same depth in the stack
    - All parent frames (the path from root to this frame) are identical
    - It appears in N samples in a row without interruption

    If a function stops and starts again, the counter resets to 1.

    Args:
        samples: A list of Sample objects sorted by timestamp.
        n: The minimum number of consecutive samples a frame must appear in
           before generating start/end events.

    Returns:
        A list of Event objects for functions that met the threshold.
        Start events are generated at the Nth occurrence (when confirmed).
        End events are generated when a confirmed function disappears.

    Example:
        >>> samples = [
        ...     Sample(1.0, ["main"]),
        ...     Sample(2.0, ["main"]),
        ...     Sample(3.0, ["main", "foo"]),
        ...     Sample(4.0, ["main", "foo"])
        ... ]
        >>> events = convert_samples_to_debounced_events(samples, 2)
        >>> # Returns: [Event("start", 2.0, "main"),
        >>> #          Event("start", 4.0, "foo")]
        >>> # main starts at t=2.0 (2nd consecutive appearance)
        >>> # foo starts at t=4.0 (2nd consecutive appearance)

    Edge Case:
        >>> samples = [
        ...     Sample(1, ["a", "b"]),
        ...     Sample(2, ["c", "b", "a"])
        ... ]
        >>> # Here "a" and "b" do NOT count as consecutive!
        >>> # At t=2, the entire stack changed. The "b" at depth 1 in sample 1
        >>> # is different from "b" at depth 1 in sample 2 because the
        >>> # parent frame changed from "a" to "c".
    """
    events = []
    
    if not samples:
        return events
    
    # Track state for each depth:
    # state[depth] = {"path": tuple, "count": int, "confirmed": bool}
    state = {}
    
    for sample in samples:
        curr_stack = sample.stack
        curr_path_by_depth = {}  # depth -> full path as tuple
        
        # Build current paths for each depth
        for depth in range(len(curr_stack)):
            curr_path_by_depth[depth] = tuple(curr_stack[:depth + 1])
        
        # First, handle end events for confirmed frames that disappeared
        for depth in list(state.keys()):
            if depth not in curr_path_by_depth or curr_path_by_depth[depth] != state[depth]["path"]:
                # This frame disappeared or changed
                if state[depth]["confirmed"]:
                    func_name = state[depth]["path"][-1]
                    events.append(Event("end", sample.ts, func_name))
                del state[depth]
        
        # Now update counters and check for confirmations
        for depth in range(len(curr_stack)):
            curr_path = curr_path_by_depth[depth]
            
            if depth in state and state[depth]["path"] == curr_path:
                # Same frame continues, increment counter
                state[depth]["count"] += 1
                
                # Check if we just reached N consecutive
                if not state[depth]["confirmed"] and state[depth]["count"] == n:
                    func_name = curr_stack[depth]
                    events.append(Event("start", sample.ts, func_name))
                    state[depth]["confirmed"] = True
            else:
                # New frame at this depth or changed frame, start counting
                state[depth] = {"path": curr_path, "count": 1, "confirmed": False}
    
    return events
