class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        
        digits=[0]*num
        idx=num-1 
        current_digit=9
        current_sum=0 
        s=sum
        while idx>=0:

            if sum >= current_digit:
                digits[idx]=current_digit 
                sum=sum-current_digit 
                current_sum+=current_digit 

                idx-=1 
            
            if sum<current_digit:

                if current_digit>0:
                    current_digit-=1 
            
       
        if current_sum!=s:
            return "" 

        ans="".join(str(d) for d in digits) 

        if ans>=ans[::-1]:
            return ans 
        else:
            return ans[::-1]
    
        
    
        
        

                
            


        