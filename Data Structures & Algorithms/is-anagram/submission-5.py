class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == 0 or len (t)==0 or len(s)!=len(t):
            return False
        count_S, count_T ={},{}
        for i in range(len(s)):
            count_S[s[i]]= 1+ count_S.get(s[i],0)
            count_T[t[i]]= 1+count_T.get(t[i],0)
        return count_T==count_S
        
