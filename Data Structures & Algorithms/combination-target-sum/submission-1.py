class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        for i in range(len(nums)):
            curr=[nums[i]]
            combination=self.findsum(nums[i:],target,nums[i],curr,res)

        return res
    def findsum(self,nums,target,local,curr,res):
        if local>target:
            return
        if local==target:
            res.append(curr)
            return True
        if local<target:
            for i in range(len(nums)):
                combination=self.findsum(nums[i:],target,local+nums[i],curr+[nums[i]],res)
        