class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def possible(nums,idx,res):
            if idx==len(nums):
                res.append(nums[:])
                return 
            for i in range(idx,len(nums)):
                nums[idx],nums[i]=nums[i],nums[idx]
                possible(nums,idx+1,res)
                nums[idx],nums[i]=nums[i],nums[idx]

        possible(nums,0,res)
        return res