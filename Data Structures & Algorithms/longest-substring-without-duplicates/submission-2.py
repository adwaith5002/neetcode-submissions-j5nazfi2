class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSub=0
        table={}
        count=0
        max_count=0
        l,r=0,0
        while(r<len(s)):
            if s[r] not in table:
                max_count=max(max_count,r-l+1)
                table[s[r]]=r
                r+=1
                continue
            l=max(l,table[s[r]]+1)
            max_count=max(max_count,r-l+1)
            table[s[r]]=r
            r+=1
        return max_count            