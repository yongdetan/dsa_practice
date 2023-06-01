digits = [9,9]

def plusOne(digits):
    digits[-1] += 1
    while 10 in digits:
        index = digits.index(10)
        digits[index] -= 10
        print(index, index-1, digits)
        if digits[index] == digits[index-1]:
            digits.insert(index, 1)
        else:
            digits[index-1] += 1
    return digits

print(plusOne(digits))