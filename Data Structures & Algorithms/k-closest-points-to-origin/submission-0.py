class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        kpoints=[]
        for x,y in points:
            distance=-(math.sqrt(x**2 + y**2))
            heapq.heappush(kpoints, [distance, x ,y] )
            if len(kpoints)>k:
                heapq.heappop(kpoints)

        res=[]
        while kpoints:
            distance,x,y=heapq.heappop(kpoints)
            res.append([x,y])
        return res