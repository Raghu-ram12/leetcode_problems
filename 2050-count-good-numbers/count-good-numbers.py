class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD=10**9+7
        e=math.ceil(n/2) 
        o=math.floor(n/2) 
        return (pow(5,e,MOD) * pow(4,o,MOD ))%MOD