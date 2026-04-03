class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic= defaultdict(list)
        for s in strs:
            res=[0]*26
            for i in s:
                res[ord(i)-ord('a')]+=1
            key=tuple(res)
            dic[key].append(s)
        return list(dic.values()) 