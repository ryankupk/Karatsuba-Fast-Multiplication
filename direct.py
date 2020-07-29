import math
from bitstring import BitArray

#adds ar2 to ar1
def add(ar1, ar2):
    zero = BitArray(ar1.len if ar1.len > ar2.len else ar2.len)
    while ar2 != zero:
        carry = ar1 & ar2
        ar1 ^= ar2
        ar2 = carry << 1
    return ar1

#subtracts ar2 from ar1
#ar1 - ar2
def subtract(ar1, ar2):
    zero = BitArray(ar1.len if ar1.len > ar2.len else ar2.len)
    while ar2 != zero:
        borrow = (~ar1) & ar2
        ar1 = ar1 ^ ar2
        ar2 = borrow << 1
    return ar1

#multiplies ar1 by ar2
def multiply(ar1, ar2):
    zero = BitArray(ar1.len if ar1.len > ar2.len else ar2.len)
    while ar2 != 0:
        ar1 = add(ar1, ar1)
        ar2 = subtract(ar2, BitArray("0b1"))
    return ar1

if __name__ == "__main__":
    numbers = [0,0]
    while numbers[0] < 999 and numbers[1] < 999:
        numbers = input("Enter two numbers greater than 999 separated by a space: ").split()
        numbers[0], numbers[1] = int(numbers[0]), int(numbers[1])

    x = BitArray(bin=bin(numbers[0]))
    x = [0] + x
    print("x is ", x, x.int)

    y = BitArray(bin=bin(numbers[1]))
    y = [0] + y
    print("y is ", y, y.int)
    print("multiplication is ", multiply(x, y))
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
    x0 = subtract(x, x1)
    y0 = subtract(y, y1)
    print(x1, x1.int, y1, y1.int)
    print("Subtraction is", subtract(x1, y1))
    z2 = x1 * y1
    print("z2 is", z2)