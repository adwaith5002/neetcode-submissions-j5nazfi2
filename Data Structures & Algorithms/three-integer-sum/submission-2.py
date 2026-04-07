class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<2:
            return []
        arr=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i >0 and nums[i-1]==nums[i]:
                continue
            j=i+1
            k=len(nums)-1
            while(j<k):
                sum= nums[i] + nums[j] + nums[k]
                if sum == 0:
                    arr.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1
                    while (j < k and nums[k] == nums[k+1]):
                        k -= 1
                elif sum<0:
                    j+=1
                    continue
                else:
                    k-=1
                    continue
        return arr