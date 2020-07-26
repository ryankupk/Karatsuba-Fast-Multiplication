import math
from bitstring import BitArray

def subtract(ar1, ar2):
    zero = BitArray(y.len if y.len > x.len else x.len)
    while ar2 != zero:
        carry = ar1 & ar2
        ar1 ^= ar2
        ar2 = carry << 1
    return ar1

if __name__ == "__main__":
    numbers = input("Enter two numbers separated by a space: ").split()

    x = BitArray(bin=bin(int(numbers[0])))
    x = [0] + x
    print("x is ", x, x.int)

    y = BitArray(bin=bin(int(numbers[1])))
    y = [0] + y
    print("y is ", y, y.int)
    n = min(x.len, y.len)
    print("n is ", n)
    b = 2
    m = None
    for i in range(n-1, 0, -1):
        if bin(i)[2] == '1' and '1' not in bin(i)[3:]:
            m = i.bit_length() - 2
            break
    print("m is ", m)
    b_m = b << m
    print("b_m is ", b_m)
    x1 = x >> m
    y1 = y >> m
    # x0 = x - x1
    print(x1, x1.int, y1, y1.int)