class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        peak_sum=0 
        valley_sum=0 

        n=len(nums) 

        for i in range(1,n-1):

            if nums[i-1]<nums[i] and nums[i+1]<nums[i]:
                peak_sum+=nums[i] 

            if nums[i-1]>nums[i] and nums[i+1]>nums[i]:
                valley_sum+=nums[i] 

        return peak_sum-valley_sum 
        