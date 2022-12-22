def check_even_digits(numbers: List[int]) -> bool:
    count = 0
    for number in numbers:
        even_count = 0
        for digit in str(number):
            if int(digit) % 2 == 0:
                even_count += 1
        if even_count == 2:
            count += 1
        if count > 3:
            return False
    return True
