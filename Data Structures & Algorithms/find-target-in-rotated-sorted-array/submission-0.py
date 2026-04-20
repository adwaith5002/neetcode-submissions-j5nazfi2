class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while(l<r):
            mid=l+((r-l)//2)
            if nums[mid]<nums[r]:
                r=mid
            else:
                l=mid+1
        print(l)
        left=0
        right=l-1
        while(left<=right):
            mid=left+((right-left)//2)
            if target==nums[mid]:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        
        left=l
        right=len(nums)-1
        while(left<=right):
            mid=left+((right-left)//2)
            if target==nums[mid]:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1

        return -1