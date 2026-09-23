class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result=[]
        def func(idx,n,nums,ans):

            if idx==n:
                result.append(ans[:])
                return 
            
            ans.append(nums[idx])
            func(idx+1,n,nums,ans) 

            ans.pop() 
            func(idx+1,n,nums,ans)
        
        n=len(nums) 
        ans=[]
        func(0,n,nums,ans) 

        return result




        