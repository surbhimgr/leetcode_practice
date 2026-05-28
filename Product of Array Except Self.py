''' Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0] 

Solution - store the product of whole array. for each element divide it from the total product to get the answer array.
Handle zeroes - keep count of number of zero 
- when more than 2 zeroes then whole answer array will always be zero
- when 1 zero except for the zero's index all other values of answer array will always be zero
'''

# Space - O(n)
# Time - O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot_prod = 1
        zero=0
        for i in nums:
            if i!=0:
                tot_prod*=i
            if i==0:
                zero+=1
        ans=[]
        for i in nums:
            if i!=0 and zero==0:
                ans.append(tot_prod//i)
            elif i==0 and zero==1:
                ans.append(tot_prod)
            else:
                ans.append(0)

        return ans
        
