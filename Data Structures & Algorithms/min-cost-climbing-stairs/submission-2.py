class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        arr=[-1]*(n+1)
        def climb(i):
            if i>=n:
                return 0
            if arr[i]!=-1:
                return arr[i]
            arr[i]=cost[i]+min(climb(i+1),climb(i+2))
            return arr[i]
        return min(climb(0), climb(1))