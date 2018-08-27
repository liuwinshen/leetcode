def valid_palindrome(s):
    if len(s) == 0:
        return True

    s = s.upper()
    for char in s:
        if char in '!@#$%^&*():"\';.,?/\\-`~<>{}|' or char == ' ':
            s = s.replace(char, '')
    return s == s[::-1]

print(valid_palindrome('A man, a plan, a canal: Panama'))
print(valid_palindrome('hello there!'))
