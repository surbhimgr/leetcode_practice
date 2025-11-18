class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt=0
        arr=[]
        for i in range(len(nums)):
            if nums[i]!=val:
                arr.append(nums[i])  
                cnt+=1
        for j in range(len(arr)):
            nums[j]=arr[j]
        return cnt