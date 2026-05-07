class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def possible(open,close,res,curr):
            if open==0 and close==0:
                res.append(curr)
            if open>0:
                possible(open-1, close,res,curr+"(")
            if close>open:
                possible(open, close-1,res,curr+")")            
        possible(n,n,res,"")
        return res