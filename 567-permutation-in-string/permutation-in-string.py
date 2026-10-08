class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        base_map={}

        for i in s1:

            if i in base_map:

                base_map[i]+=1 
            else:
                base_map[i]=1 

        right=0 
        left=0 

        n=len(s2) 

        current_map={}
        k=len(s1)
        while (right<n):

            if s2[right] in current_map:

                current_map[s2[right]]+=1 
            else:
                current_map[s2[right]]=1 
            
            if right-left+1==k:

                if base_map==current_map:
                    return True 
                
                current_map[s2[left]]-=1 

                if current_map[s2[left]]==0:
                    current_map.pop(s2[left]) 
                
                left+=1  
            
            right+=1 
        
        return False



        

        