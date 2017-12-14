#!/usr/bin/python3

"""
2SUM

Given: A positive integer k <= 20, a positive integer n <= 10^4, and k arrays
of size n containing integers from -10^5 to 10^5.

Return: For each array A[1..n], output two different indices 1 <= p < q <= n
such that A[p] = -A[q] if exist, and "-1" otherwise.
"""

def main():
    k = 0   # number of vertices
    n = 0   # number of edges

    # Parse in.txt
    with open('./in.txt') as f:
        for i, line in enumerate(f):
            if i == 0:
                k, n = (int(x) for x in line.split())
            else:
                array = [int(x) for x in line.split()]
                two_sum(array, n)

def two_sum(array, n):
    """Solves the 2SUM problem as described above

    Convert array to a dictionary where the keys are the values in array and
    the values are a list of the indices of that value. This should take O(n).

    Once the dictionary is created, then iterate through array and identify
    whether the negative version of the value exists in the array. Return the
    index of the current item being looked at in array and the index of the
    item found in the dictionary lookup. Iterating through the array should
    take O(n) and the dictionary lookup should take O(1).

    Therefore the complexity of the overall algorithm should be O(n).

    Args:
        array: A list of at most 20 integers

    Returns:
        Does not return any elements but prints the following:
            -1 if there are no elements that satisfy the 2SUM problem
            A tuple of the indices p and q that satisfy the 2SUM problem

    """
    
    # Creates a dictionary using the indices of array as the keys
    two_sum_dict = {}
    for i, x in enumerate(array):
        if not x in two_sum_dict:
            two_sum_dict[x] = [i+1]
        else:
            two_sum_dict[x].append(i+1)

    for x in array:
        p = -1
        q = -1
        if x <= n and -x in two_sum_dict:
            p = two_sum_dict[x][0]
            q = two_sum_dict[-x][0]
        
        # Special case where we're dealing with 0
        if x <= n and x == 0 and len(two_sum_dict[x]) > 1:
            p = two_sum_dict[x][0]
            q = two_sum_dict[x][1]

        if p < q and q <= n:
            print(p, q)
            return
    print(-1)
    return
    

if __name__ == '__main__':
    main()
