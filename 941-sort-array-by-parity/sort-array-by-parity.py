class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:

        i=-1 

        for j in range(len(nums)):

            if nums[j]%2==0:
                i+=1 
                nums[i],nums[j]=nums[j],nums[i] 
        
        return nums
            
            

        