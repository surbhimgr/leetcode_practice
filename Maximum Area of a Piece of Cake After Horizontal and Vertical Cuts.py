''' 
You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.

Solution - Sort the arrays, then compute the maximum difference between two consecutive elements for horizontal cuts and vertical cuts.
Handle the edge cases i.e distance from 0 and from h or w
'''
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = (10**9)+7
        hc=len(horizontalCuts)
        vc=len(verticalCuts)
        horizontalCuts.sort()
        verticalCuts.sort()
        hmax=max(horizontalCuts[0],h-horizontalCuts[-1])
        vmax=max(verticalCuts[0],w-verticalCuts[-1])
        if hc>1:
            for i in range(hc-1):
                hmax=max(hmax,horizontalCuts[i+1]-horizontalCuts[i])
        if vc>1:
            for j in range(vc-1):
                vmax=max(vmax,verticalCuts[j+1]-verticalCuts[j])
        ans=hmax*vmax
        return ans%MOD
