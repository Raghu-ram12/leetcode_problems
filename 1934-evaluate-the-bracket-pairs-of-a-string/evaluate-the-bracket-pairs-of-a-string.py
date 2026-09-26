class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        result=""
        n=len(s) 

        i=0  
        result= ''  

        mpp={} 

        for row in knowledge:
            key=row[0] 
            value=row[1] 
            mpp[key]=value

        while i<n:
            c=s[i] 

            if c=="(":

                key=''
                i+=1 
                 
                while s[i]!=")":

                    key+=s[i]
                    i+=1 

                result+=mpp.get(key,"?") 

            else:

                result+=c
                
            i+=1 
        
        return result
