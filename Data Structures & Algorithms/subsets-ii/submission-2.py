class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        path=[]
        res=[]
        def backtrack(res,path,nums,idx):
            res.append(path[::])
            for i in range(idx,len(nums)):
                if i>idx and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(res,path,nums,i+1)
                path.pop()
        backtrack(res,path,nums,0)
        return res