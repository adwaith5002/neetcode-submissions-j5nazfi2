class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if (len(nums)==0 or len(nums)==1):
            return False
        return len(nums) != len(set(nums))
