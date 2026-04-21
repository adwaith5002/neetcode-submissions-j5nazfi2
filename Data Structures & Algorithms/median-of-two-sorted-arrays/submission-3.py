class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        A,B=nums1,nums2
        half=(m+n)//2

        if m>n:
            A=nums2
            B=nums1
        l=0
        h=len(A)-1
        while(True):
            i=(l+h)//2
            j=half-i-2
            
            Aleft=A[i] if i>=0 else float("-infinity")
            Aright=A[i+1] if (i+1)<len(A) else float("infinity")

            Bleft=B[j] if j>=0 else float("-infinity")
            Bright=B[j+1] if (j+1)<len(B) else float("infinity")

            if Aleft<=Bright and Bleft<=Aright:
                if (m+n)%2:
                    return min(Aright,Bright)
                return (max(Aleft,Bleft)+min(Bright,Aright))/2
            elif Aleft>Bright:
                h=i-1
            else:
                l=i+1
            

