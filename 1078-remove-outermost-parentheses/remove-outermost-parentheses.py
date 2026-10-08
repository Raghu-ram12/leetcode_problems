class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        b=0 
        stack=[] 
        ans=""
        for i in range(len(s)):

            if s[i]=="(":
                b+=1 
                stack.append(s[i])
            else:
                b-=1 
                stack.append(s[i])
            
            if b==0:
                ans+="".join(stack[1:-1]) 
                stack=[] 

        return ans

        