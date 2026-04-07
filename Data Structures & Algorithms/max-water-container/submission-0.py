class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j=0, len(heights)-1
        vol=0
        while(i<j):
            breadth=j-i
            height=min(heights[i],heights[j])
            local_vol=breadth*height
            if local_vol>vol:
                vol=local_vol
                if heights[i]>heights[j]:
                    j-=1
                else:
                    i+=1
            else:
                if heights[i]>heights[j]:
                    j-=1
                else:
                    i+=1
        return vol