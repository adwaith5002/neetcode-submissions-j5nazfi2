class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        arr=sorted(nums)
        res=[]
        res.append(arr[0])
        maxlen=0
        i=0
        j=1
        while(j<=len(nums)-1):
            if arr[i]==arr[j]:
                i+=1
                j+=1
                continue
            elif(arr[j]-arr[i]==1):
                res.append(arr[j])
                j+=1
                i+=1
            else:
                maxlen=max(maxlen,len(res))
                print(maxlen)
                i=j
                j+=1
                res=[]
                res.append(arr[i])
        maxlen=max(maxlen,len(res))
        return maxlen