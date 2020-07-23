import math


if __name__ == "__main__":
    numbers = input("Enter two numbers separated by a space: ").split()

    x = numbers[0]
    y = numbers[1]

    n = max(len(x), len(y))
    print(math.log10(int(x)))