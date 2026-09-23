class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        def func(n,k):

            if n==1:
                return 0 
            

            return (func(n-1,k)+k)%n 
        
        return func(n,k)+1




