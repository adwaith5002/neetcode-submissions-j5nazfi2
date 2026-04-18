class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        h=len(matrix)-1

        while(l<=h):
            mid=l+(h-l)//2
            low=0
            high=len(matrix[mid])-1

            while(low<=high):
                middle=low+((high-low)//2)
                if matrix[mid][middle]==target:
                    return True
                elif matrix[mid][middle]>target:
                    high=middle-1
                    h=mid-1
                else:
                    low=middle+1
                    l=mid+1

        return False