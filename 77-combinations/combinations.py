class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result=[]
        def solve(start,ans):

            if len(ans)==k:
                result.append(ans[:])
                return 

            for i in range(start+1,n+1):
                ans.append(i)
                solve(i,ans) 
                ans.pop() 
        
        solve(0,[])

        return result


                

            

        
        
            
            

