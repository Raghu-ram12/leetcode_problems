class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        ans=0 
        n=len(arr) 

        for i in range(n):

            for j in range(n):

                sub=arr[i:j+1] 

                if(j-i+1)%2!=0:
                    ans+=sum(sub) 
        
        return ans


    
        