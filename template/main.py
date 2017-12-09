#!/usr/bin/python3

"""
Given:

Return:
"""

def main():
    # Parse in.txt
    with open('./in.txt') as f:
        for i, line in enumerate(f):
            print(i, line)

if __name__ == '__main__':
    main()
