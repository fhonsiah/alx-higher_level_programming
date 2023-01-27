#!/usr/bin/python3
if __name == "__main__":
    a = 10
    b = 5
    from calculator_1 import add, subtract, multiply, divide
    result = add(a, b)
    result = subtract(result, b)
    result = multiply(result, a)
    result = divide(result, b)
    print(result)
