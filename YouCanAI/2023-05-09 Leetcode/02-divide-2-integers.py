# Prompt:
# Complete the following code in python3. Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator. 
# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2. 
# Return the quotient after dividing dividend by divisor. 
# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231. 

# class Solution: 

#     def divide(self, dividend: int, divisor: int) -> int: 

# Accepted
# Runtime: 55ms, 5.2 percentile
# Memory: 16.2MB, 11.94 percentile


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1
            
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        
        for i in range(31, -1, -1):
            if (dividend >> i) - divisor >= 0:
                quotient += 1 << i
                dividend -= divisor << i
                
        quotient = sign * quotient
        
        if quotient > (2**31) - 1:
            quotient = (2**31) - 1
        elif quotient < -(2**31):
            quotient = -(2**31)
            
        return quotient