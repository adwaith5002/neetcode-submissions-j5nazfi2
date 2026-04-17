class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area=[]
        area.append((0,heights[0]))
        max_area=0
        for i in range(1,len(heights)):
            if heights[i]<area[-1][1]:
                index=i
                while(area and heights[i]<area[-1][1]):
                    max_area=max(max_area, area[-1][1]*(i-area[-1][0]))
                    index=area[-1][0]                
                    area.pop()
                area.append((index,heights[i]))
            else:
                area.append((i,heights[i]))
        for i in range(len(area)):
            max_area=max(area[i][1]*(len(heights)-area[i][0]), max_area)

        return max_area