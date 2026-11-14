class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        
        ans=float("inf") 
        n=len(nums) 

        for k in range(l,r+1):

            left=0 
            current=0
            for right in range(n): 

                current+=nums[right] 

                if right-left+1==k:
                    if current>0:
                        ans=min(ans,current)
                    current-=nums[left]
                    left+=1
        
        if ans!=float('inf'):
            return ans 
        else:
            return -1
