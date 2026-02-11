from sys import *
from collections import *
from math import *

from typing import *

#check sting is palindrome or not, if not adding it's value how many times to make it palindrome
def palindrome(A: List[int]) -> int: 
    # Write your code here.
    n = len(A)
    left = 0
    right = n-1
    ops = 0

    while left <= right:
        if A[left] == A[right]:
            left += 1
            right -= 1
        
        elif A[left] < A[right]:
            A[left + 1] = A[left] + A[left+1]
            left += 1
            ops += 1
        
        else:
            A[right - 1] = A[right] + A[right-1]
            right -= 1
            ops += 1

    return print(ops)

palindrome([1,2,1,1])