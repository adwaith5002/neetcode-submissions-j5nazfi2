class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res={}
        for i in nums:
            res[i]=1+res.get(i,0)
        arr=[]
        for cnt,num in res.items():
            arr.append([cnt,num])
        arr.sort(key= lambda x:x[1])
        L=[]
        i=0
        while(i<len(res)):
            L.append(arr.pop()[0])
            i+=1
            if i==k: break
        return L