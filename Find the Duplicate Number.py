''' Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space. 

Solution - Its like detecting cycle in a linked list. as there are n+1 integers ranging between 1 to n, the array values will be in same range as the indexes value and if we point the next array element by using 
array value as index values then their must be 2 or more elements pointing to the same index. (look for notes in copy)

Floyd's cycle detection alog - https://www.youtube.com/watch?v=S5TcPmTl6ww
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

        
