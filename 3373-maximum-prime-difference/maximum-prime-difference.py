class Solution:
    def is_prime(self,n):

        if n<=1:
            return False 
        if n==2:
            return True 
        if n%2==0:
            return False 
        i=3 

        while i*i <=n:

            if n%i==0:
                return False 
            i+=2 
        return True 

    def maximumPrimeDifference(self, nums: List[int]) -> int:

        first=0 

        for i,n in enumerate(nums):

            if self.is_prime(n):
                first=i 
                break 

        last=first
        n=len(nums)
        for i in range(first+1,n):

            if self.is_prime(nums[i]):
                last=i 
        
        return last-first
        