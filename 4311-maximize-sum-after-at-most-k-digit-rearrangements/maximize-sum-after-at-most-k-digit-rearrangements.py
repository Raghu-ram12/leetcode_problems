class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        gains=[]
        for n in nums:

            max_num=int("".join(sorted(str(n)))[::-1])
            gain=max_num-n 

            if gain>0:
                gains.append(gain)

        gains.sort(reverse=True)
        return sum(nums)+sum(gains[:k]) 
        
        
        