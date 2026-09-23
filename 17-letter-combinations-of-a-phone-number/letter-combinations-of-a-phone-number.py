mpp={
    "2":"abc",
    "3":"def",
    "4":"ghi",
    "5":"jkl",
    "6":"mno",
    "7":"pqrs",
    "8":"tuv",
    "9":"wxyz"
}
class Solution:
    def letterCombinations(self,digits: str) -> list[str]:
        result=[]
        def func(idx,digits,ans):

            if idx>=len(digits):

                result.append(ans)
                return 
            
            for c in mpp[digits[idx]]:

                func(idx+1,digits,ans+c) 
                ans[:-1] 
        ans=""
        func(0,digits,ans)

        return result

        



        