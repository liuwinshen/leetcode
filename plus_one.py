def plus_one(digits):
    digits.reverse()

    for i, digit in enumerate(digits):
        if digit >= 9:
            digits[i] = 0
            try:
                digits[i+1] += 1
                if digits[i+1] <= 9:
                    break
            except IndexError:
                digits.append(1)
                break
        else:
            digits[i] += 1
            break

    digits.reverse()
    return digits

print(plus_one([1,2,3,4])
print(plus_one([9]))
print(plus_one([7,8,9])
