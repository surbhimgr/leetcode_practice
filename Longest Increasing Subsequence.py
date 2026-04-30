''' Given an integer array nums, return the length of the longest strictly increasing subsequence.
Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Solution - The main idea is to store the increasing tail considering all elements of num as the smallest element in the subsequence one by one. 
create an sub
iterate for each element in nums.
bisect uses binary search find the expected position of num in sub. It maintains a sorted list and returns position where num fit after keeping the array sorted.
if size of sub==pos --> num is the largest element encountered hence add to end
else replace the element in the sorted sub list
return len of sub
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub=[]
        for num in nums:
            pos=bisect.bisect_left(sub,num)
            if pos==len(sub):
                sub.append(num)
            else:
                sub[pos]=num
        return(len(sub))
        
