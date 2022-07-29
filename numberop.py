# Number Operations
# Alice has invented a new card game to play with Bob. Alice made a deck of cards with random values between 1 and 52. Bob picks 5 cards. 
# Then, he has to rearrange the cards so that by utilizing the operations plus, minus, or times, the value of the cards reach Alice's favorite number, 42. 
# More precisely, find operations such that ((((val1 op1 val2) op2 val3) op3 val4) op4 val5) = 42.
# Help Bob by writing a program to determine whether it is possible to reach 42 given 5 card values.
# For example, Bob picks 5 cards out of the deck containing 40, 1, 3, 4, and 20. Bob rearranges the cards and supplies four operations, so that 4 * 20 - 40 + 3 - 1 = 42.
# Input:
# The input consists of five integers on a line, separated by spaces. Each integer is between 1 and 52, inclusive.
# Output:
# Print a line containing "YES" if it is possible to reach the value 42 according to the rules of the game, or "NO" otherwise.
# Example
# 40 1 3 4 20 --> YES

import sys
from itertools import permutations
# import numpy as np
# import pandas as pd
# from sklearn import ...

for line in sys.stdin:
    l = line.split()
    t = 42
    op = ['+','-','*','/']
    valcal = []
    for v1 in permutations(l,len(l)):
        for v2 in permutations(op,len(op)):
            cal = ''.join(o+v for o,v in zip(['']+list(v2),v1))
            valcal.append(eval(cal))
    if t in valcal:
        print('YES')
    else:
        print('NO')
