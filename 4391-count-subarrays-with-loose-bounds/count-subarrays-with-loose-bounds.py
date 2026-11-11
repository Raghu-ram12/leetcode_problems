class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:

        total_sub_arrays=0 
        current_len=0 
        n=len(nums) 
        
        for i in range(n):

            if nums[i]>=minK and nums[i]<=maxK:

                current_len+=1 
                total_sub_arrays+=current_len 
            else:
                current_len=0 

        return total_sub_arrays 
        