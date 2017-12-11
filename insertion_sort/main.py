#!/usr/bin/python3

"""
Insertion Sort

Given: A positive ingeter n <= 10^3 and an array A[1..n] of integers.

Return: The number of swaps performed by insertion sort algorithm on A[1..n].
"""

def main():
    n = 0   # number of integers in array A
    array = []

    # Parse in.txt
    with open('./in.txt') as f:
        for i, line in enumerate(f):
            if i == 0:
                n = int(line)
            else:
                array = [int(x) for x in line.split()]

    print(insertion_sort_swaps(array))


def insertion_sort_swaps(array):
    """Number of times insertion sort performs a swap

    Args:
        array: An unsorted list that will undergo insertion sort.

    Returns:
        The number of swaps that insertion sort performed.
    """
    swap = 0
    for i, x in enumerate(array):
        k = i
        while k > 0 and array[k] < array[k-1]:
            array[k], array[k-1] = array[k-1], array[k]
            swap += 1
            k -= 1
    return swap 

if __name__ == '__main__':
    main()
