#!/usr/bin/env python3
import calculator_1 as calculator
import sys

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

a = int(sys.argv[1])
operator = sys.argv[2]
b = int(sys.argv[3])

if operator not in ['+', '-', '*', '/']:
    print("Unknown operator. Available operator: +, -, * and /")
    sys.exit(1)

result = None
if operator == '+':
    result = calculator.add(a, b)
elif operator == '-':
    result = calculator.sub(a, b)
elif operator == '*':
    result = calculator.mul(a, b)
else:
    result = calculator.div(a, b)


print("{} {} {} = {}".fomart(a, operator, b, result))
