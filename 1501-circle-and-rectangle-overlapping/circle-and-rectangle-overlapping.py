class Solution:
    def checkOverlap(self, r: int, cx: int, cy: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        if cx<x1:

            dx=x1

        elif cx>x2 :

            dx=x2 
        else:
            dx=cx 
            
        dy=0
        if cy<y1:

            dy=y1

        elif cy>y2:

            dy=y2 
        else:
            dy=cy
        
        return (cx-dx)**2+(cy-dy)**2 <=r*r 