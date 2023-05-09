
# Prompt:
# Complete the following code in python3. It should be a function to convert roman numerals to integers. It should work on roman numerals up to M. 

# class Solution: 

#     def romanToInt(self, s: str) -> int: 


# Accepted
# Runtime 70ms, 8.33 percentile
# Memory 16.3MB, 7.13 percentile

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        i = 0
        while i < len(s):
            current = roman_to_int[s[i]]
            if i + 1 < len(s) and roman_to_int[s[i+1]] > current:
                result -= current
            else:
                result += current
            i += 1
        return result
