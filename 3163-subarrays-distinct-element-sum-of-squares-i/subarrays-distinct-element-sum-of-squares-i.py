class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        

        n=len(nums) 
        ans=0

        for i in range(n):

            for j in range(i,n):

                k=len(set(nums[i:j+1]))
                ans+=(k**2)
        
        return ans

                

        
        