# Prompt:
# Complete the following code in python3. Convert a non-negative integer num to its English words representation. 
# Example 1: 
# Input: num = 123 Output: "One Hundred Twenty Three"  
# Example 2: 
# Input: num = 12345 Output: "Twelve Thousand Three Hundred Forty Five"  
# Example 3: 
# Input: num = 1234567 Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"  
# Constraints: 
#     0 <= num <= 231 – 1 

# Accepted
# Runtime: 57ms, 5.58 percentile
# Memory: 16.6MB, 5.45 percentile

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        ones = {0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
        tens = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
        decimals = {20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
        
        def convert(num):
            if num == 0:
                return ""
            elif num < 10:
                return ones[num] + " "
            elif num < 20:
                return tens[num] + " "
            elif num < 100:
                return decimals[num // 10 * 10] + " " + convert(num % 10)
            elif num < 1000:
                return ones[num // 100] + " Hundred " + convert(num % 100)
            elif num < 1000000:
                return convert(num // 1000) + "Thousand " + convert(num % 1000)
            elif num < 1000000000:
                return convert(num // 1000000) + "Million " + convert(num % 1000000)
            else:
                return convert(num // 1000000000) + "Billion " + convert(num % 1000000000)
    
        return convert(num).strip()
