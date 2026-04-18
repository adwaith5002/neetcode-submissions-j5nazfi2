class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        rows=len(matrix)
        cols=len(matrix[0])
        h=(rows*cols)-1
        while(l<=h):
            mid=l+((h-l)//2)
            if matrix[mid//cols][mid%cols]==target:
                return True
            elif matrix[mid//cols][mid%cols]>target:
                h=mid-1
            else:
                l=mid+1

        return False