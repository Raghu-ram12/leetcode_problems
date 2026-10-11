class Solution:
    def sumOfSquares(self, nums: List[int]) -> int: 

        n=len(nums) 
        ans=0
        for i,v in enumerate(nums):

            if n%(i+1)==0:
                ans+=v*v
        
        return ans


        