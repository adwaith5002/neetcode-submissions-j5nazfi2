class Solution:
    def trap(self, height: List[int]) -> int:
        l=len(height)
        if l<=2:
            return 0
        i,j=0,1
        water=0
        leftmax=[0]*l
        leftmax[0]=height[0]
        rightmax=[0]*l
        rightmax[l-1]=height[l-1]
        for i in range(1,l):
            leftmax[i]=max(leftmax[i-1],height[i])
        for i in range(l-2,-1,-1):
            rightmax[i]=max(rightmax[i+1],height[i])
        for i in range(l):
            water+=min(leftmax[i],rightmax[i])-height[i]
        return water

