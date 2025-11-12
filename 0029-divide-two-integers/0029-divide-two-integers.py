class Solution(object):
    def divide(self, dividend, divisor): # 10, 3
        a, b = dividend, divisor # 10, 3
        if a == 0: return 0

        sign = -1 if (a < 0) ^ (b < 0) else 1 # 1
        a = abs(a) # 10
        b = abs(b) # 3
        
        quotient = 0
        temp = b # 3
        while a >= (temp << 1): # 2**32 >= 2 ** 33
            temp <<= 1 # 2 ** 32
        
        while temp >= b: # 2 ** 31 >= 2**0
            if a >= temp: # 0 >= 2 ** 32
                a -= temp # 0
                quotient += 1 # 1
            temp >>= 1 # 2 ** 31
            quotient <<= 1 # 2 ** 32

        res = quotient * sign >> 1
        maxi = (2**31) - 1
        return res if res <= maxi else maxi
        