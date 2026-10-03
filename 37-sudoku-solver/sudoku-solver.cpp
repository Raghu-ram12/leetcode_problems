class Solution {
public:
    bool valid(vector<vector<char>>& board,int row,int col,char c){

        for(int i=0;i<9;i++){

            if(board[i][col]==c || board[row][i]==c){
                return 0;
            }
        }

        

        int sx=(row/3)*3;
        int sy=(col)/3*3;

        for(int i=sx;i<sx+3;i++){

            for(int j=sy;j<sy+3;j++){

                if(board[i][j]==c){
                    return 0;
                }
            }
        }

        return 1;


    }
    bool solve(vector<vector<char>>&board){

        for(int i=0;i<9;i++){

            for(int j=0;j<9;j++){

                if (board[i][j]=='.'){

                for(char k='1';k<='9';k++){

                    if(valid(board,i,j,k)){

                        board[i][j]=k; 

                        if(solve(board)){

                            return 1;

                        }

                        board[i][j]='.';

                    }

                }
                return 0;
                
                }
                
            }
        }

        return 1;

    }
    void solveSudoku(vector<vector<char>>& board) {

        solve(board);
        
    }
};