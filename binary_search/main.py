#!/usr/bin/python3

"""
Binary Search

Given: Two positive integers n <= 10^5 and m <= 10^5, a sorted array A[1..n] of
integers from -10^5 to 10^5 and a list of m integers 
-10^5 <= k_1, k_2, ..., k_m <= 10^5.

Return: For each k_i, output an index 1 <= j <= n, s.t. A[j] = k_i or "-1" if
there is no such index.
"""

def main():
    n = 0   # length of sorted_list
    m = 0   # length of eval_list
    sorted_list = []
    eval_list = []
    
    # Parse in.txt
    with open('./in.txt') as f:
        for i, line in enumerate(f):
            if i == 0:
                n = int(line)
            elif i == 1:
                m = int(line)
            elif i == 2:
                sorted_list = [int(x) for x in line.split()]
            else:
                eval_list = [int(x) for x in line.split()]

    # Perform Binary Search for each item in eval_list
    for x in eval_list:
        print(binary_sort(x, 0, n-1, sorted_list), end=" ")

def binary_sort(x, start, end, sorted_list):
    """Performs Binary Search

    Get the middle index (start+end/2)
    Take the middle element of the sorted list and compare it to x
    If x is the middle element, return the index
        If start == end then return -1
    If x is less than this, perform binary sort on the left list
        Pass the new start and end indices
    If x is more than this, perform binary sort on the right list
        Pass the new start and end indices

    Args:
        x: The search element
        start: The start index of the sub-array of sorted_list
        end: The end index of the sub-array of sorted_list
        sorted_list: The sorted list that we will be searching

    Returns:
        An int corresponding to the index of x in sorted_list
        Otherwise returns -1 if x does not exist in sorted_list
    """
    
    middle = int((start + end) / 2)

    if start == end:
        if x == sorted_list[middle]:
            return middle+1
        else:
            return -1
    else:
        if x == sorted_list[middle]:
            return middle+1
        if x < sorted_list[middle]:
            return binary_sort(x, 0, middle-1, sorted_list)
        if x > sorted_list[middle]:
            return binary_sort(x, middle+1, end, sorted_list)


if __name__ == '__main__':
    main()
