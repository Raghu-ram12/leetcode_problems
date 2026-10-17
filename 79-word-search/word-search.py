class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        mpp={
            0:[-1,0],
            1:[1,0],
            2:[0,-1],
            3:[0,1] 
        }

        k=len(word) 
        m=len(board) 
        n=len(board[0]) 
      
        def solve(row,col,idx):

            if idx==k:
                return True
            
            temp=board[row][col] 

            board[row][col]='#' 

            for i in range(4):

                new_row=row+mpp[i][0]
                new_col=col+mpp[i][1] 

     
                if (new_row>=0 and new_row<m ) and (new_col>=0 and new_col<n):

                    if word[idx]==board[new_row][new_col]:

                        if solve(new_row,new_col,idx+1):

                            return True 
            
            board[row][col]=temp
            
        

        for i in range(m):

            for j in range(n):

                if board[i][j]==word[0]:

                    if solve(i,j,1): 

                        return True 
                    

        return False



        
