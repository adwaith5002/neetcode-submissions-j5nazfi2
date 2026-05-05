class MedianFinder:

    def __init__(self):
        self.left=[]
        self.right=[]
    def addNum(self, num: int) -> None:
        if not self.left:
            heapq.heappush(self.left,num)
        else:
            if num>self.left[0]:
                heapq.heappush(self.left,num)
            else:
                heapq.heappush(self.right,-num)
        if abs(len(self.right)-len(self.left))>1:
            if len(self.right)>len(self.left):
                heapq.heappush(self.left,-(heapq.heappop(self.right)))
            else:
                heapq.heappush(self.right,-(heapq.heappop(self.left)))
    def findMedian(self) -> float:
        if (len(self.left)+len(self.right))%2==0:
            left=self.left[0]
            right=-(self.right[0])
            return (right+left)/2
        else:
            if len(self.right)>len(self.left):
                return -(self.right[0])
            else:
                return self.left[0]