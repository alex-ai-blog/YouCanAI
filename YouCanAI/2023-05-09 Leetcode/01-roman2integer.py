
# Prompt:
# Complete the following code in python3. It should be a function to convert roman numerals to integers. It should work on roman numerals up to M. 

# class Solution: 

#     def romanToInt(self, s: str) -> int: 


# Accepted

class Solution:

    def romanToInt(self, s: str) -> int:
        
        values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0
        i = 0
        
        while i < len(s):
            if i+1 < len(s) and values[s[i]] < values[s[i+1]]:
                result += values[s[i+1]] - values[s[i]]
                i += 2
            else:
                result += values[s[i]]
                i += 1
                
        return result