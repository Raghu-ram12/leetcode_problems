MAX=1000001
primes=[True]*(MAX) 
primes[0],primes[1]=False,False 

i=2
while i*i <= MAX:

    if primes[i]:

        for j in range(i*i,MAX,i):

            primes[j]=False

    i+=1 

class Solution:

    def findPrimePairs(self, n: int) -> List[List[int]]:
 
        
        result=[] 

        for i in range(2,(n//2)+1):

            if primes[i] and primes[n-i]:

                result.append([i,n-i]) 
        
        return result



        