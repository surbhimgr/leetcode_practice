''' Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order. 

Solution - Recursion+backtracking
create an empty list for storing result --> ans
create a boolean list for marking items that are already visited --> vis
create a empty list for storing current permutation that we're worklking on --> path
create a backtrack function that takes path and vis as inpput
base condition --> if len(path) == len(nums) then append to ans. Keep in mind to append like this --> ans.append(path[:]) --> using this we're not actually appending path but appending its current copy as path is a variable and its value will change in future.
create a for loop iterating through all elemnts of nums, if vis[i]==False then add current element to path, mark its vis[i] =True.
call backtrack function with the updated path and vis --> next element will automatically keep adding next elements which are not visited
after coming out of function pop from path, mark vis[i]=False
the for loop will continue exploring next elements as our backtrack step
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]

        def backtrack(path,vis):
            if len(nums)==len(path):
                ans.append(path[:])
                return
            for i in range(len(nums)):
                if not vis[i]:
                    path.append(nums[i])
                    vis[i]=True
                    backtrack(path,vis)
                    path.pop()
                    vis[i]=False
        vis=[False] * len(nums)
        backtrack([],vis)
        return ans


        
