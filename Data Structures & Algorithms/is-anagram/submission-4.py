class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == 0 or len (t)==0 or len(s)!=len(t):
            return False
        changed_x=sorted(s)
        changed_y= sorted(t)
        for i in range(len(changed_x)):
            if changed_x[i] != changed_y[i]:
                return False
        return True
        
