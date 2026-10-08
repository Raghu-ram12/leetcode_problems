class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        from collections import deque 

        dq=deque() 

        left=0 
        right=0 

        n=len(nums) 
        result=[]
        while right<n:

            while len(dq)!=0 and nums[right]>dq[-1]:
                dq.pop() 
                
            
            dq.append(nums[right]) 
            
            if (right-left+1==k):

                result.append(dq[0]) 
                
                if nums[left]==dq[0]:
                    dq.popleft() 
                left+=1 
            
            right+=1 
        
        return result
            
        