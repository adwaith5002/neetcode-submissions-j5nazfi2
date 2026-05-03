class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kLarge=[]
        for num in nums:
            heapq.heappush(kLarge,num)
            if len(kLarge)>k:
                heapq.heappop(kLarge)
        
        return kLarge[len(kLarge)-k]