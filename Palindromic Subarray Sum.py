''' Q4. Palindromic Subarray Sum
Solved
Hard
6 pt.
You are given an integer array nums.

Return the maximum possible sum of a subarray of nums that is a palindrome. '''


class Solution:
    def getSum(self, nums: List[int]) -> int:
        n=len(nums)
        pref=[0]*(n+1)
        for i in range(n):
            pref[i+1]=pref[i]+nums[i]

        t=[-2,-1]
        for num in nums:
            t.append(num)
            t.append(-1)
        t.append(-3)
        m=len(t)
        p=[0]*m
        c=0
        r=0
        for i in range(1,m-1):
            imir=2*c-i
            if r>i:
                p[i]=min(r-i,p[imir])
            while t[i+1+p[i]]==t[i-1-p[i]]:
                p[i]+=1
            if i+p[i]>r:
                c=i
                r=i+p[i]
        maxs=0
        for i in range(1,m-1):
            l=p[i]
            if l>0:
                st=(i-1-l)//2
                cursum=pref[st+l]-pref[st]
                if cursum>maxs:
                    maxs=cursum
        return maxs
