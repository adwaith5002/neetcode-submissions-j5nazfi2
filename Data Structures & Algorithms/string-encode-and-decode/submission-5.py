class Solution:
    def encode(self, strs: List[str]) -> str:
        L=""
        for i in  strs:
            for s in i:
                L=L+s
            L=L+"."
        return L
    def decode(self, s: str) -> List[str]:
        L=[]
        x=""
        for i in range(len(s)):
            if s[i]==".":
                L.append(x)
                x=""
            else:
                x=x+s[i]
        return L