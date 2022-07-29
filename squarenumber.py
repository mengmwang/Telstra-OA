# Square a Number
# Write a program that squares an integer and prints the result.

import sys

for line in sys.stdin:
    print(str(int(line)*int(line)), end="")
