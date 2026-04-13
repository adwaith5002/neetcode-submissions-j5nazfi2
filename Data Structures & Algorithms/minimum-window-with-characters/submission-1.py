class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        
        count=defaultdict(int)
        for i in range(len(t)):
            count[t[i]]+=1
        min_dist=float("infinity")
        min_r=len(s)-1
        min_l=0
        i=0
        count1=defaultdict(int)
        have,need=0,len(count)
        for j in range(len(s)):
            count1[s[j]]+=1
            if s[j] in count and count[s[j]]==count1[s[j]]:
                have+=1
            while have==need:
                if min_dist>=(j-i+1):
                    min_dist= j-i+1
                    min_r=j
                    min_l=i
                count1[s[i]]-=1
                if s[i] in count and count1[s[i]]<count[s[i]]:
                    have-=1
                i+=1
        return s[min_l:min_r+1] if min_dist!=float("infinity") else ""
            