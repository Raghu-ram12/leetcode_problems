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

    def splitArray(self, nums: List[int]) -> int:

        sum_a=0 
        sum_b=0 

        for i,n in enumerate(nums):

            if self.is_prime(i):
                sum_a+=n 
            else:
                sum_b+=n

        return abs(sum_a-sum_b) 

        