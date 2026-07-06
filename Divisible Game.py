''' Divisible Game
Solved
Medium
premium lock icon
Companies
Hint
You are given an integer array nums of length n.

Alice and Bob are playing a game. Alice chooses:

An integer k such that k > 1.
Two integers l and r such that 0 <= l <= r < n.
Initially, both Alice's and Bob's scores are 0.

For each index i in the range [l, r] (inclusive):

If nums[i] is divisible by k, Alice's score increases by nums[i].
Otherwise, Bob's score increases by nums[i].
The score difference is Alice's score minus Bob's score.

Alice wants to maximize the score difference. If there are multiple values of k that achieve the maximum score difference, she chooses the smallest such k.

Return the product of the maximum score difference and the chosen value of k. Since the result can be large, return it modulo 109 + 7. '''

class Solution:
    def divisibleGame(self, nums: list[int]) -> int:
        MOD=10**9+7
        unqp=set([2])
        for num in nums:
            temp=num
            d=2
            while d*d<=temp:
                if temp%d==0:
                    unqp.add(d)
                    while temp%d==0:
                        temp//=d
                d+=1
            if temp>1:
                unqp.add(temp)
        maxdif=float('-inf')
        bestk=float('inf')
        for k in unqp:
            currmax=float('-inf')
            currsum=0
            for x in nums:
                val=x if x%k==0 else -x
                currsum=max(val,currsum+val)
                currmax=max(currmax,currsum)
            if currmax>maxdif:
                maxdif=currmax
                bestk=k
            elif currmax==maxdif and k<bestk:
                bestk=k
        return (maxdif*bestk)%MOD
