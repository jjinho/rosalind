#!/usr/bin/python3

"""
Merge Sort Two Arrays

Given: A positive integer n <= 10^5 and a sorted array A[1..n] of integers
from -10^5 to 10^5, a positive integer m <= 10^5 and a sorted array B[1..m] of
integers from -10^5 to 10^5.

Return: A sorted array C[1..n+m] containing all the elements of A and B.
"""

def main():
    n = 0   # number of elements in array A
    m = 0   # number of elements in array B
    array_a = []
    array_b = []

    # Parse in.txt
    with open('./in.txt') as f:
        for i, line in enumerate(f):
            if i == 0:
                n = int(line.strip())
            if i == 1:
                array_a = [int(x) for x in line.split()]
            if i == 2:
                m = int(line.strip())
            if i == 3:
                array_b = [int(x) for x in line.split()]
        
        # Non-recursive way to solve
        array_c = []
        while array_a and array_b:
            if array_a[0] < array_b[0]:
                array_c += [array_a.pop(0)]
            else:
                array_c += [array_b.pop(0)]
        
        # Can do this because array_a and array_b are already sorted
        if array_a:
            array_c += array_a
        if array_b:
            array_c += array_b

        for x in array_c:
            print(x, end=" ")
        print()

# This works but is too 
def merge_arrays(array_a, array_b):
    if array_a and array_b:
        if array_a[0] < array_b[0]:
            return [array_a.pop(0)] + merge_arrays(array_a, array_b)
        else:
            return [array_b.pop(0)] + merge_arrays(array_a, array_b)
    else:
        if array_a:
            return array_a
        if array_b:
            return array_b
    return array_c

if __name__ == '__main__':
    main()
