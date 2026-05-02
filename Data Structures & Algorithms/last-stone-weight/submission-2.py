from _heapq import heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones= [-s for s in stones]
        heapq.heapify(stones)
        i=0
        while len(stones)>1:
            x=heapq.heappop(stones)
            y=heapq.heappop(stones)
            if y>x:
                heapq.heappush(stones,x-y)

            
        if stones: return abs(heapq.heappop(stones))
        else: return 0