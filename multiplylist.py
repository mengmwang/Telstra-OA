# Multiply Lists
# You have 2 lists of positive integers. Write a program which multiplies corresponding elements in these lists.
# Input:
# Your program should read lines from standard input. Each line contains two space-delimited lists. The lists are separated with a pipe char (|). Both lists have the same length, in range [1, 10]. Each element in the lists is a number in range [0, 99].
# Output:
# Print the multiplied list.
# 9 0 6 | 15 14 9 --> 135 0 54
# 13 4 15 1 15 5 | 1 4 15 14 8 2 --> 13 16 225 14 120 10

import sys

for line in sys.stdin:
    l = line.split() 
    l.remove('|')
    l = [int(x) for x in l]
    l1 = l[:int(len(l)/2)]
    l2 = l[int(len(l)/2):]
    print(' '.join(map(str, [a*b for a,b in zip(l1,l2)])), end="")
