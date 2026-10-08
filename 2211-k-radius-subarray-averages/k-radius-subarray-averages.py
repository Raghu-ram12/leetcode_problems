class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n=len(nums)
        result=[-1]*n 

        right=0 
        left=0 
        s=0
        while right<n:
            s+=nums[right] 

            if right-left+1==2*k+1:

                result[(left+right)//2]=s//(2*k+1) 
                s-=nums[left] 

                left+=1 
            
            right+=1
        
        return result



        