''' Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

solution:
use prefix sum and hashmap - using these makes it similar to find if there are 2 elements with sum k in array.
Using prefix sum gives us the sum of a range of continous elements in an array and if we want to find out if the sum equals k, we just substract the sum of the range of elements(subarray) from k.
Initialize prefix sum with 0:1 for cases where the whole array sum = k
The prefix sum dictionary here stores frequency of the sums as there can be negative numbers as well, the prefix sums may not always be increasing.
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps={0:1}
        ans=0
        run_sum=0
        for i in nums:
            run_sum+=i
            if run_sum-k in ps:
              ans+=ps[run_sum-k]
            if  run_sum not in ps: 
                ps[run_sum]=0
            ps[run_sum]+=1
            
        return ans
