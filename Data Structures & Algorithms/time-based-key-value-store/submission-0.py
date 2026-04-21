class TimeMap:
    def __init__(self):
        self.keystore={}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore:
            self.keystore[key]=[]
        self.keystore[key].append([value,timestamp])
    def get(self, key: str, timestamp: int) -> str:
        res=""
        values=self.keystore.get(key,[])
        l=0
        h=len(values)-1
        while(l<=h):
            mid=l+(h-l)//2
            if values[mid][1]<=timestamp:
                res=values[mid][0]
                l=mid+1
            else:
                h=mid-1
        return res            

        