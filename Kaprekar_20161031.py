"""
    In mathematics, a Kaprekar number for a given base is a non-negative integer,
    the representation of whose square in that base can be split into two parts that add up to the original number again
    For instance, 45 is a Kaprekar number, because 452 = 2025 and 20+25 = 45. The Kaprekar numbers are named after D. R. Kaprekar
"""


def is_kaprekar(n):
    squared = pow(n, 2)
    str_squared = str(squared)
    for i in range(len(str_squared)-1):
        left_substr = str_squared[:i+1]
        right_substr = str_squared[i+1:]
        left = int(left_substr)
        right = int(right_substr)
        if left > 0 and right > 0 and (left + right) == n:
            return True
    return False


def find_kaprekar_numbers_range(line):
    result = []
    min_range = line.split(' ')[0].strip()
    max_range = line.split(' ')[1].strip()

    for i in range(int(min_range), int(max_range)):
        if is_kaprekar(i):
            result.append(i)

    for i in result:
        print(str(i) + ' ')


def main():
    line = input('>')
    while len(line) > 0:
        find_kaprekar_numbers_range(line)
        line = input('>')

if __name__ == '__main__':
    main()
