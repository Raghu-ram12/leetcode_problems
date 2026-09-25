class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum=nums[0] 
        ans=nums[0] 

        for num in nums[1:]:

            current_sum=max(current_sum+num,num)

            ans=max(ans,current_sum) 
        
        return ans
        