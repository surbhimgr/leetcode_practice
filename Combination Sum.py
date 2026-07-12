''' Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations. 

Solution - Backtraking - 
Edge cases -
1 - when no such combination exists

iterate through the array, check all combinations with a particular current index and remaining difference with target. break when remaining is 0, append answer. break when remaning is less than 0 or array is finished.
pop the current index and backtrack to next index element
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        n = len(candidates)

        def dfs(index: int, remaining: int) -> None:

            if remaining == 0:
                ans.append(path.copy())
                return

            if remaining < 0 or index == n:
                return

            path.append(candidates[index])
            dfs(index, remaining - candidates[index])   # choosing the same candidate multiple times
            path.pop()

            dfs(index + 1, remaining)  # going to next element

        dfs(0, target)

        return ans
