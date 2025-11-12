class Solution(object):
    def divide(self, dividend, divisor):
        sign = 1
        if divisor < 0 or dividend < 0:
            sign = -1
        if divisor < 0 and dividend < 0:
            sign = 1

        divisor = abs(divisor)
        dividend = abs(dividend)

        if sign * (dividend // divisor) > (2**31 - 1):
            return 2**31 - 1
        if sign * (dividend // divisor) < -(2**31):
            return -2**31
        else:
            return sign * (dividend // divisor)