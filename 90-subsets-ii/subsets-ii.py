class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result=[] 
        n=len(nums) 

        def dfs(idx,ans):

            if len(ans)<=n:
                result.append(ans[:]) 
            
            if idx==n:
                return  
            ans.append(nums[idx])
            dfs(idx+1,ans) 
            ans.pop()
            dfs(idx+1,ans) 
        
        dfs(0,[]) 
        
        return [list(x) for x in set(tuple(item) for item in result)]

        