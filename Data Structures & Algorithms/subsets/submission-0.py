class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for num in nums:
            sub=[]
            for subset in res:
                new=subset+[num]
                sub.append(new)
            for x in sub:
                res.append(x)
        return res