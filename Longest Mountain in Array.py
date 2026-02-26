class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        i = 0
        up, down = 0, 0
        while i < n - 1:  
            if arr[i] >= arr[i+1]:
                i += 1  
            else:
                while i < n-1 and arr[i] < arr[i+1]:
                    i += 1
                    up += 1
                while i < n-1 and arr[i] > arr[i+1]:
                    i += 1
                    down += 1
                if up > 0 and down > 0:
                    res = max(res, up + down + 1)
                up, down = 0, 0

        return res
