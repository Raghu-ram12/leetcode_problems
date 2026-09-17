class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals.sort()
        result=[intervals[0]]
        for interval in intervals[1:]:

            prev_end=result[-1][-1]

            start,end=interval[0],interval[1] 

            if start<=prev_end:
                
                if end > prev_end:
                    
                    result[-1][-1]=end 
            else:


                result.append(interval) 
                
        return result
        