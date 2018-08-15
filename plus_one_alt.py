def plus_one_alt(digits):
    number = ''
    for digit in digits:
        number += str(digit)
    number = int(number) + 1

    return [int(digit) for digit in str(number)]
