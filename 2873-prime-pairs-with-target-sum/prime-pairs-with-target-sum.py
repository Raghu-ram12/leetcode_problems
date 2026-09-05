class Solution:

    def findPrimePairs(self, n: int) -> List[List[int]]:

        primes=[True]*(n+1) 
        primes[0],primes[1]=False,False 

        i=2

        while i*i <= n+1:

            if primes[i]:

                for j in range(i*i,n+1,i):

                    primes[j]=False

            i+=1 
        
        
        result=[] 

        for i in range(2,(n//2)+1):

            if primes[i] and primes[n-i]:

                result.append([i,n-i]) 
        
        return result



        