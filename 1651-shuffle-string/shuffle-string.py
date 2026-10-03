class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        
        n=len(s) 

        arr=[""]*n
        
        for i in range(n):

            arr[indices[i]]=s[i]
        
        return "".join(arr)

            
