# Capitalize Words
# Write a program which capitalizes the first letter of each word in a sentence.
# Input:
# Your program should read lines from standard input. Each line has a sequence of words.
# Output:
# Print the capitalized words.
# Example
# Hello world --> Hello World
# a letter --> A Letter

import sys

for line in sys.stdin:
    print(line.title(), end="")
