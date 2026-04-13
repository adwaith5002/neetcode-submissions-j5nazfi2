class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr=[]
        for i in range(len(tokens)):
            if tokens[i] == "+":
                temp2=arr.pop()
                temp1=arr.pop()
                arr.append(temp1+temp2)
            elif tokens[i] == "-":
                temp2=arr.pop()
                temp1=arr.pop()
                arr.append(temp1-temp2)
            elif tokens[i] == "*":
                temp2=arr.pop()
                temp1=arr.pop()
                arr.append(temp1*temp2)
            elif tokens[i] == "/":
                temp2=arr.pop()
                temp1=arr.pop()
                arr.append(int(float(temp1/temp2)))
            else:
                arr.append(int(tokens[i]))
        return arr[-1] if len(arr)<=1 else 0