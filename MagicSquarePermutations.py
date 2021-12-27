#  File: MagicSquare.py

#  Description: Generate all magic squares of integer n through permutation

#  Student Name: Anna Dougharty

#  Student UT EID: amd5933

#  Course Name: CS 313E

#  Unique Number: 52600

#  Date Created: Dec 1 2021

#  Date Last Modified: Dec 3 2021

import sys
import math

def is_magic ( a ):

    n = int(math.sqrt(len(a)))
    constant = n * (n ** 2 + 1) / 2

    # check rows
    idx = 0
    for i in range(n):
        row_sum = 0
        for j in range(n):
            row_sum += a[idx]
            idx += 1
        if row_sum != constant:
            return False
        
    # check columns
    for i in range(n):
        idx = i
        col_sum = 0
        for j in range(n):
            col_sum += a[idx]
            idx += n
        if col_sum != constant:
            return False

    # check diagonals
    diag_sum_1 = 0
    diag_sum_2 = 0
    idx_1 = 0
    idx_2 = n-1
    for x in range(n):
        diag_sum_1 += a[idx_1]
        diag_sum_2 += a[idx_2]
        idx_1 += n + 1
        idx_2 += n - 1
    if diag_sum_1 != constant or diag_sum_2 != constant:
        return False

    # else
    return True

def is_magic_row(a, row, n, constant):
    row_sum = 0
    for i in range(n):
        row_sum += a[row * n + i]
    return row_sum == constant

def is_magic_col(a, col, n, constant):
    col_sum = 0
    for i in range(n):
        col_sum += a[col + i * n]
    return col_sum == constant

def is_magic_r_diag(a, n, constant):
    diag_sum_2 = 0
    for i in range(n):
        diag_sum_2 += a[(n - 1) * (1 + i)]
    return diag_sum_2 == constant

def potential_magic_col(a, idx, col, n, constant):
    valid_num = constant

    for i in range(n - 1):
        valid_num -= a[col + n * i]
    
    if (valid_num <= 0 or valid_num > n ** 2 or valid_num in a[1:idx]):
        return False
    return True

def permute( a, idx, all_magic ):

    length = len(a)
    n = int(math.sqrt(length))
    constant = n * (n ** 2 + 1) / 2
    permute_helper(a, 0, all_magic, length, n, constant)

def permute_helper( a, idx, all_magic, length, n, constant):

    if (idx == length):
        all_magic.append(a[:])

    else:

        if ((idx + 1) < length and (idx + 1) % n == 0):
            for i in range(idx, length):
                a[idx], a[i], = a[i], a[idx]

                if is_magic_row(a, ((idx + 1) // n) - 1, n, constant):

                    permute_helper(a, idx + 1, all_magic, length, n, constant)
                a[idx], a[i] = a[i], a[idx]

        elif (n * (n - 2) <= idx < n * (n - 1)):
            for i in range(idx, length):
                a[idx], a[i], = a[i], a[idx]

                if potential_magic_col(a, idx, idx % n, n, constant):
                    permute_helper(a, idx + 1, all_magic, length, n, constant)
                a[idx], a[i] = a[i], a[idx]

        elif (idx == n * (n - 1)):
            for i in range(idx, length):
                a[idx], a[i], = a[i], a[idx]

                if is_magic_col(a, idx % n, n, constant) and is_magic_r_diag(a, n, constant):
                    permute_helper(a, idx + 1, all_magic, length, n, constant)
                a[idx], a[i] = a[i], a[idx]

        elif (n * (n - 1) < idx < length-2 ):
            for i in range(idx, length):
                a[idx], a[i], = a[i], a[idx]

                if is_magic_col(a, idx % n, n, constant):
                    permute_helper(a, idx + 1, all_magic, length, n, constant)
                a[idx], a[i] = a[i], a[idx]

        elif (idx == length-1):
            for i in range(idx, length):
                a[idx], a[i], = a[i], a[idx]

                if is_magic(a):
                    permute_helper(a, idx + 1, all_magic, length, n, constant)
                a[idx], a[i] = a[i], a[idx]

        else: 
            for i in range(idx, length):
                a[idx], a[i], = a[i], a[idx]
                permute_helper(a, idx + 1, all_magic, length, n, constant)
                a[idx], a[i] = a[i], a[idx]

def main():

    line = sys.stdin.readline()
    line = line.strip()
    n = int (line)

    all_magic = []

    numbers = []
    for i in range(n ** 2):
        numbers.append(i + 1)

    permute(numbers, 0, all_magic)

    for square in all_magic:
        print (square)

if __name__ == "__main__":
    main()
