class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        arr=[-1]*(n+1)
        def cost(i):
            if i>=n:
                return 0
            if arr[i]!=-1:
                return arr[i]
            arr[i]=max(nums[i]+cost(i+2),cost(i+1))
            return arr[i]
        return cost(0)