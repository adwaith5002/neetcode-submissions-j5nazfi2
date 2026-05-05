class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()

        def findcombination(idx,target,local,curr):
            if local==target:
                res.append(curr.copy())
                return
            if local>target:
                return
            else:
                for i in range(idx,len(candidates)):
                    if i>idx and candidates[i]==candidates[i-1]:
                        continue
                    findcombination(i+1,target,local+candidates[i],curr+[candidates[i]])

        findcombination(0,target,0,[])
        return res
    