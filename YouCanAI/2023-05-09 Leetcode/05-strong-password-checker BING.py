

class Solution:

    def strongPasswordChecker(self, password: str) -> int:
        # initialize the number of steps
        steps = 0

        # check the length of the password
        n = len(password)
        if n < 6:
            # if too short, insert characters to reach 6
            steps += 6 - n
        elif n > 20:
            # if too long, delete characters to reach 20
            steps += n - 20

        # check the types of characters in the password
        has_lower = False
        has_upper = False
        has_digit = False
        for c in password:
            if c.islower():
                has_lower = True
            elif c.isupper():
                has_upper = True
            elif c.isdigit():
                has_digit = True

        # count the number of missing types
        missing_types = 0
        if not has_lower:
            missing_types += 1
        if not has_upper:
            missing_types += 1
        if not has_digit:
            missing_types += 1

        # check the number of repeating characters in the password
        repeats = 0
        i = 0
        while i < n:
            # find the length of the current run of the same character
            j = i + 1
            while j < n and password[j] == password[i]:
                j += 1
            run_length = j - i

            # if the run length is at least 3, count it as a repeat
            if run_length >= 3:
                repeats += run_length // 3

            # move to the next different character
            i = j

        # if the password is too short, the missing types can be fixed by inserting characters
        if n < 6:
            steps += max(missing_types - (6 - n), 0)
        # if the password is too long, the repeats can be fixed by deleting characters
        elif n > 20:
            # try to delete one character from each run of length k * 3 + 1 for k >= 1
            k = 1
            while k * 3 + 1 <= n and repeats > 0:
                for i in range(n - (k * 3 + 1) + 1):
                    if password[i] == password[i + k * 3] and password[i] == password[i + k * 3 + 1]:
                        repeats -= 1
                        break
                k += 1

            # try to delete two characters from each run of length k * 3 + 2 for k >= 1
            k = 1
            while k * 3 + 2 <= n and repeats > 0:
                for i in range(n - (k * 3 + 2) + 1):
                    if password[i] == password[i + k * 3] and password[i] == password[i + k * 3 + 2]:
                        repeats -= min(2, repeats)
                        break
                k += 1

            # add the remaining repeats to the steps
            steps += repeats

        # if the password is within the length range, the missing types and repeats can be fixed by replacing characters
        else:
            steps += max(missing_types, repeats)

        return steps