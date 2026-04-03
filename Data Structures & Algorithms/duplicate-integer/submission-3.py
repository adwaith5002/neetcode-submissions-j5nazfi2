class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if (len(nums)==0 or len(nums)==1):
            return False
        i=0
        nums.sort()
        range=len(nums)
        while True:
            if nums[i]==nums[i+1]:
                return True
            elif i+1==range-1:
                break
            else:
                i+=1
        return False
