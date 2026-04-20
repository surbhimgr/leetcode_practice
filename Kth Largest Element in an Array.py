''' Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting? 
solution - python has minimum heap implemented
min heap - parent will be samller than child. so root has smallest element from whole tree
heappop - pops root
heappush - pushes new element and maintains heap property
create a heap with k elements. iterate remaining elemnts and when the element is greater than root, pop root and insert the new element.
At the end u will have have a heap with top n largest element. return root as it will be smallest from the list and our kth largest
'''

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:      
        h=nums[:k]
        heapq.heapify(h)
        for i in range(k,len(nums)):
            if h[0]<nums[i]:
                heapq.heappop(h)
                heapq.heappush(h,nums[i])
        
        return h[0]
        
