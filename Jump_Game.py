''' You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise. '''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cnt=0
        for i in nums:
            if cnt<0:
                return False
            elif i>cnt:
                cnt=i
            cnt-=1
        return True

''' Intuition - think of this as car and gas problem. as long as u have gas and u can reach to the position then its fine. fillup gas whenever u reach a position having more gas. for each position ahead gas is decreased by 1 '''
