#!/bin/python
#short function that explains recursion simply by calculating a factorial
import sys

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1
if __name__ == "__main__":
    n = int(raw_input().strip())
    result = factorial(n)
    print result
