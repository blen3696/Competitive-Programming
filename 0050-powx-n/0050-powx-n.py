class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x,n):
            if n == 1:
                return x
            if n == 0:
                return 1
            div =  pow(x , n//2)
            if n % 2 == 0:
                return div * div
            else:
                return div * div * x

        return pow(x,n) if n >= 0 else 1/pow(x,abs(n))

    

        
        