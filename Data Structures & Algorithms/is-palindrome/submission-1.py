class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","")
        print(s)
        i=0
        j=len(s)-1
        while(i<j):
            if not(self.alphanum(s[i])):
                i+=1
            if not(self.alphanum(s[j])):
                j-=1
            if self.alphanum(s[i]) and self.alphanum(s[i]):
                if s[i].lower()!=s[j].lower():
                    return False
                i+=1
                j-=1
        return True
    def alphanum(self, c)->bool:
        return (ord('A')<= ord(c) <= ord('Z')
            or ord('a') <= ord(c) <= ord('z')
            or ord('0') <= ord(c) <= ord('9')
        )