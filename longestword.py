# Longest Word
# In this challenge you need to find the longest word in a sentence. If the sentence has more than one word of the same length you should pick the one that appears first.
# Input:
# Your program should read lines from standard input. Each line has one or more words. Each word is separated by a space char.
# Output:
# Print the longest word in the sentence.
# Example:
# some line with text --> some
# another line --> another

import sys

for line in sys.stdin:
    print(max(line.split(), key=len), end="")
