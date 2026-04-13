class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        for i in range(len(s)):
            if s[i]=="{" or s[i]=='(' or s[i]=='[':
                arr.append(s[i])
            else:
                if len(arr)==0:
                    return False
                if s[i]=="}":
                    if arr[-1]=='{':
                        arr.pop()
                    else:
                        return False
                elif s[i]==")":
                    if arr[-1]=='(':
                        arr.pop()  
                    else:
                        return False  
                else:
                    if arr[-1]=='[':
                        arr.pop() 
                    else:
                        return False
        return True if len(arr)==0 else False