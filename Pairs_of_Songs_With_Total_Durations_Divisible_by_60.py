'''You are given a list of songs where the ith song has a duration of time[i] seconds.
Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.'''

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt =0
        # l=[0]*60
        dic={}
        for i in time:
            rem = i%60
            # cnt+= l[(60-rem)%60]
            com=(60-rem)%60
            if com in dic:
                cnt+= dic[com]
            dic[rem]=dic.get(rem,0)+1
        return cnt
        
