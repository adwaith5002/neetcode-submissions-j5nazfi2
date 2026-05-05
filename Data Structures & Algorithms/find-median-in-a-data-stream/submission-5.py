class MedianFinder:

    def __init__(self):
        self.arr=[]
    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
    def findMedian(self) -> float:
        length=len(self.arr)
        if length%2!=0:
            res= self.arr[length//2]
        else:
            print(length)
            print(self.arr[length//2-1])
            print(self.arr[(length//2)])
            res= (self.arr[length//2-1]+self.arr[(length//2)])/2
        return res