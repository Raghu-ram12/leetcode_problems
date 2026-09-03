class Solution:
    def is_prime(self,n):
        if n<=1:
            return False 
        if n==2:
            return True 
        if n%2==0:
            return False
        i=3
        while i*i <= n:
            if n%i==0:
                return False 
            i+=2 
        return True 

    def isThree(self, n: int) -> bool:

        return int(math.sqrt(n))==math.sqrt(n) and self.is_prime(math.sqrt(n))

    
        
        