class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        target=high
        while(low<=high):
            mid=low+((high-low)//2)
            count=0
            for i in range(len(piles)):
                count+= math.ceil(piles[i]/mid)            
            if count<=h:
                target=mid
                high=mid-1
            else:
                low=mid+1
        return target

