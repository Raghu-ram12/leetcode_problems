class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        result=[]
    
        n=len(nums)

        visited=set()

        def dfs(arr):

            if len(arr)==n:
                result.append(arr[:]) 
                return
            
            for i in nums:

                if i not in visited:

                    visited.add(i) 
                    arr.append(i) 
                    dfs(arr) 
                    visited.remove(i) 
                    arr.pop()
        
        dfs([]) 

        return result
                

                