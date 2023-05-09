# Prompt:
# Rerwite this code to improve memory usage and speed up runtime.

# Accepted
# Runtime 53ms, 50.52 percentile
# Memory 16.2MB, 18.72 percentile

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev = roman_to_int[s[-1]]
        result = prev
        for i in range(len(s)-2, -1, -1):
            current = roman_to_int[s[i]]
            if current < prev:
                result -= current
            else:
                result += current
            prev = current
        return result
