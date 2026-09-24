class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result=[]
        def backtrack(current_str,open,close):

            if len(current_str)==2*n:
                result.append(current_str) 
                return 
            

            if open < n:
                backtrack(current_str+"(",open+1,close) 
            
            if close < open:

                backtrack(current_str+")",open,close+1) 

        
        backtrack("",0,0) 

        return result


                

        