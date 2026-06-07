''' A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory. 

Intuition - 3 steps
step 1 : find the last element where its next element is greater than it. lets say we got it at index i. 
step 2 : find the smallest elemnt in the remaining array i.e. i+1 to end. swap it with i. --> next permutation will always be a greater number than the current number
step 3 : reverse the remaining array i.e. i+1 to end --> but it will be the minimum greater number comapred to remaining permutations. making the all digits of number to descending order will
give the largest permutation, hence ascending will give the lowest.
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        li=-1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                li=i
        if li==-1:
            nums.sort()
        else:
            m=999
            mi=-1
            for j in range(li+1, len(nums)):
                if nums[li]<nums[j]:
                    mi=j
            nums[li],nums[mi]=nums[mi],nums[li]
            nums[li+1:]= reversed(nums[li+1:])
        
