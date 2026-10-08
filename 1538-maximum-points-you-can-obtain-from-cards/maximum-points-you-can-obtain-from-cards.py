class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        
        ans=float('inf') 
        right=0 
        left=0 
        n=len(cardPoints) 
        if n==k:
            return sum(cardPoints)
        s=0
        while(right<n):

            s+=cardPoints[right] 

            if right-left+1==(n-k):

                ans=min(ans,s) 

                s-=cardPoints[left] 
                left+=1 
            
            right+=1 

        return sum(cardPoints)-ans
        