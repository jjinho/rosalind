#!/usr/bin/python3

"""
Majority Element

Given: A positive integer k <= 20, a positive integer n <= 10^4, and k arrays
of size n containing positive integers not exceeding 10^5.

Return: For each array, output an element of this array occuring strictly more
than n/2 times if such element exists, and "-1" otherwise.
"""

def main():
    n = 0   # number of cases
    m = 0   # number of elements
    array = []

    # Parse in.txt
    with open('./in.txt') as f:
        for i, line in enumerate(f):
            if i == 0:
                n, m = (int(x) for x in line.split())
            else:
                majority = {}
                array = [int(x) for x in line.split()]
                for x in array:
                    if x not in majority:
                        majority[x] = 1
                    else:
                        majority[x] += 1
           
                maj = -1
                for k, v in majority.items():
                    if v > m/2:
                        maj = k

                print(maj, end=" ")
        print()

if __name__ == '__main__':
    main()
