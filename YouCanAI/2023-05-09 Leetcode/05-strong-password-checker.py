# Prompt:
# Complete the following code in python3. Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0. 
# A password is considered strong if the below conditions are all met: 
#     It has at least 6 characters and at most 20 characters. 
#     It contains at least one lowercase letter, at least one uppercase letter, and at least one digit. 
#     It does not contain three repeating characters in a row (i.e., "Baaabb0" is weak, but "Baaba0" is strong). 
# Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0. 
# In one step, you can: 
#     Insert one character to password, 
#     Delete one character from password, or 
#     Replace one character of password with another character. 
# Example 1: 
# Input: password = "a" 
# Output: 5 

# Example 2: 
# Input: password = "aA1" 
# Output: 3  

# Example 3: 
# Input: password = "1337C0d3" 
# Output: 0 

# Constraints: 
#     1 <= password.length <= 50 
#     password consists of letters, digits, dot '.' or exclamation mark '!'. 
# class Solution: 
#     def strongPasswordChecker(self, password: str) -> int: 

# Failed 

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        # Define the password conditions
        has_upper, has_lower, has_digit = False, False, False

        for c in password:
            if c.isupper():
                has_upper = True
            elif c.islower():
                has_lower = True
            elif c.isdigit():
                has_digit = True

        # Check if the password meets all the conditions
        meets_length = 6 <= len(password) <= 20
        meets_conditions = has_upper and has_lower and has_digit
        meets_repeating = self.check_repeating(password)

        steps = 0

        # If the password doesn't meet the length requirement, add steps to make the length correct
        if not meets_length:
            missing_chars = 6 - len(password) if len(password) < 6 else 0
            extra_chars = len(password) - 20 if len(password) > 20 else 0
            steps += max(missing_chars, extra_chars)

        # If the password doesn't meet the other conditions, add steps to make it correct
        if not meets_conditions:
            steps += 3 - (has_upper + has_lower + has_digit)

        # If the password doesn't meet the repeating character condition, add steps to make it correct
        if not meets_repeating:
            steps += self.fix_repeating(password)

        return steps

    # Helper function to check for repeating characters
    def check_repeating(self, password: str) -> bool:
        for i in range(len(password) - 2):
            if password[i] == password[i+1] == password[i+2]:
                return False
        return True

    # Helper function to fix repeating characters
    def fix_repeating(self, password: str) -> int:
        length = len(password)
        repeats = []

        # Find all the repeating sequences and their lengths
        i = 0
        while i < length:
            j = i + 1
            while j < length and password[j] == password[i]:
                j += 1
            if j - i >= 3:
                repeats.append(j - i)
            i = j

        # Initialize variables
        changes = 0
        ones = length % 3 == 0
        twos = length % 3 == 1

        # If there are no repeating sequences, return 0
        if not repeats:
            return 0

        # Try to remove one character from each repeating sequence
        for repeat in repeats:
            if ones and repeat == 3:
                ones = False
            elif twos and repeat == 4:
                twos = False
            else:
                changes += 1
                if repeat - 1 >= 3:
                    repeats.append(repeat - 1)

        # If there are no more changes needed, return the number of changes made
        if not ones and not twos:
            return changes

        # Try to remove two characters from one repeating sequence
        for repeat in repeats:
            if ones and repeat >= 6:
                ones = False
                changes += 2
            elif twos and repeat >= 7:
                twos = False
                changes += 2

        # If there are no more changes needed, return the number of changes made
        if not ones and not twos:
            return changes

        # If all else fails, add characters to the password until it meets the other conditions
        return changes + 6 - len(password) if len(password) < 6 else changes
