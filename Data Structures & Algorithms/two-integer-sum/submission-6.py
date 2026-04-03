class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L_ist=[]
        if len(nums)<=1:
            return L_ist
        for i in range(len(nums)-1):
            y=target-nums[i]           
            for j in range(i+1,len(nums)):
                if(y==nums[j]):
                    L_ist.append(i)
                    L_ist.append(j)
                    return L_ist
