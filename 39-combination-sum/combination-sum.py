class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        result=[] 
        n=len(candidates)
        def backtrack(idx,ans,target):

            if target==0:
                
                result.append(ans[:])
                return  
            
            if idx==n or target <0:
                return  
            
            ans.append(candidates[idx]) 
            
            backtrack(idx,ans,target-candidates[idx]) 
            ans.pop()
            backtrack(idx+1,ans,target)
        
        backtrack(0,[],target) 

        return result
        