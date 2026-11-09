class Solution:
    def calculateScore(self, a: int, b: int) -> int:

        s1=0 
        s2=0
        while a>0:

            a=a&(a-1)
            s1+=1 

        while b>0:

            b=b&(b-1)
            s2+=1 

        if s1>=s2:
            return s1*s2 
        else:
            return s2//s1 
            