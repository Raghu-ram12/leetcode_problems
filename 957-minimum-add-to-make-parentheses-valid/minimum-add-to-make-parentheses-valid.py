class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        balance = 0
        unmatched_closing = 0
        
        for char in s:
            if char == "(":
                balance += 1
            else:  # char == ")"
                balance -= 1
                if balance < 0:
                    unmatched_closing += 1
                    balance = 0
                    
        return unmatched_closing + balance