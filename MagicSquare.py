#  File: MagicSquare.py

#  Description: Create a magic square based on an odd integer and
#  return the sum of all adjacent numbers to a given number

#  Student's Name: Anna Dougharty

#  Student's UT EID: amd5933

#  Course Name: CS 313E

#  Unique Number: 52600

#  Date Created: 9.9.21

#  Date Last Modified: 9.10.21

import sys
import math

def make_square(n):
    #make an empty 2D list with the dimensions of magic square
    square_elem = [[0 for i in range(n)] for j in range(n)]

    num = 1
    #row
    i = -1
    #column
    j = math.floor(n/2)

    #Go through all the numbers that will show up in the magic square
    for num in range(1, n**2+1):
        #assign the number 1 spot
        if num == 1:
            square_elem[i][j] = num
            i += 1
            j += 1
        #if the number is in the corner off the grid move it to above the previous cell
        elif i > n-1 and j > n-1:
            i -= 2
            j -= 1
            square_elem[i][j] = num
            i += 1
            j += 1
        #if the number is off the grid by column
        elif i > n-1:
            i = 0
            square_elem[i][j] = num
            i += 1
            j += 1
        #if the number is off the grid row
        elif j > n-1:
            j = 0
            square_elem[i][j] = num
            i += 1
            j += 1
        #if the number is just normal
        elif square_elem[i][j] == 0:
            square_elem[i][j] = num
            i += 1
            j += 1
        #if the number movement stays within the grid but is occupied move it to above the previous cell
        elif square_elem[i][j] != 0:
            i -= 2
            j -= 1
            square_elem[i][j] = num
            i += 1
            j += 1
    return square_elem

def print_square(magic_square):
    for i in magic_square:
        for j in i:
            print(j, end = ' ')
        print()

def check_square(magic_square):
    n = len(magic_square)  # size
    csum = n * (n ** 2 + 1) / 2  # canonical sum
    # sums rows and columns
    r = 0  # sum of rows
    c = 0  # sum of columns

    for i in range(0, n):
        r = 0
        c = 0
        for j in range(0, n):
            r = r + magic_square[i][j]  # rows
            c = c + magic_square[j][i]  # columns
        if ((r != csum) or (c != csum)):  # when sum is not canonical sum
            return False  # matrix is not magic square

    # sum of diagonals
    d1 = 0  # top left to bottom right sum
    d2 = 0 # top right to bottom left sum
    x = 0 #first possible index
    last = n - 1  # last possible index
    while (x<n):
        d1 = d1 + magic_square[x][x]
        d2 = d2 + magic_square[x][last]
        x = x + 1  # incrementing value
        last = last - 1  # decrementing value
    if ((d1 != csum) or (d2 != csum)):  # when sum is not canonical sums
        return False  # matrix is not magic square
    return True

def sum_adjacent_numbers(square, n):
    surrounding = []
    k = len(square)
    for i, sublist in enumerate(square):
        if n in sublist:
            j = sublist.index(n)
            #above
            if i-1 > -1:
                surrounding.append(square[i-1][j])
            #above right
            if j+1 < k and i-1 > -1:
                surrounding.append(square[i-1][j+1])
            #right
            if j+1 < k:
                surrounding.append(square[i][j + 1])
            #bottom right
            if i+1 < k and j+1 < k:
                surrounding.append(square[i + 1][j + 1])
            #bottom
            if i+1 < k:
                surrounding.append(square[i + 1][j])
            #left bottom
            if i+1 <k and j-1 > -1:
                surrounding.append(square[i + 1][j-1])
            #left
            if j-1 > -1:
                surrounding.append(square[i][j - 1])
            #above left
            if i-1 > -1 and j-1 > -1:
                surrounding.append(square[i - 1][j - 1])
    return sum(surrounding)

def main():
    #getting the first number for the dimensions of the square
    n = int(sys.stdin.readline())
    search_list = []  # Start with empty list
    while True:
        #get the next line and strip the space
        search_input = sys.stdin.readline().strip('\n')
        if not search_input:  # Exit on empty string.
            break
        #add all the numbers to a list
        search_list.append(search_input)
    #go through list and print the sum if it is found in the square
    for i in search_list:
        print(sum_adjacent_numbers(make_square(n), int(i)))

if __name__ == "__main__":
    main()