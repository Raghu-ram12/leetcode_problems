class Solution:
    def find_sum(self,n):
        s=0
        while n>0:
            s+=n%10 
            n=n//10 
        
        return s

    def smallestIndex(self, nums: List[int]) -> int:
        
        ans=len(nums)

        for i,v in enumerate(nums):

            if i==self.find_sum(v):

                if i<ans:
                    ans=i 
        
        if ans==len(nums):
            return -1 
        else:
            return ans



        