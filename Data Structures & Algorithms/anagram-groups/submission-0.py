class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [strs]
        temp_L_ist=[]
        L_ist=[]
        k=0
        for i in range(len(strs)):
            temp_L_ist.append(''.join(sorted(strs[i])))
        while(k<len(strs)):
            L_ist.append([strs[k]])
            j=k+1
            while(j < len(strs)):
                if temp_L_ist[k]==temp_L_ist[j]:
                    L_ist[k].append(strs[j])
                    temp_L_ist.pop(j)
                    strs.pop(j)
                else:
                    j+=1
            k+=1
        return L_ist 
