Q2. Rotate Non Negative Elements
Solved
Medium
4 pt.
You are given an integer array nums and an integer k.

Rotate only the non-negative elements of the array to the left by k positions, in a cyclic manner.

All negative elements must stay in their original positions and must not move.

After rotation, place the non-negative elements back into the array in the new order, filling only the positions that originally contained non-negative values and skipping all negative positions.

Return the resulting array.

 

Example 1:

Input: nums = [1,-2,3,-4], k = 3

Output: [3,-2,1,-4]

Explanation:​​​​​​​

The non-negative elements, in order, are [1, 3].
Left rotation with k = 3 results in:
[1, 3] -> [3, 1] -> [1, 3] -> [3, 1]
Placing them back into the non-negative indices results in [3, -2, 1, -4].

class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        l=[]
        for i in nums:
            if i>=0:
                l.append(i)
        n=len(l)
        l1=[i for i in range(n)]
        for i in range(n):
            l1[(i-k+n)%n]=l[i]
            j=0
        for i in range(len(nums)):
            if nums[i]>=0:
                nums[i]=l1[j]
                j+=1

        return nums
            
