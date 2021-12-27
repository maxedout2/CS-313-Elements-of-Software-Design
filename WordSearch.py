#  File: WordSearch.py
#  Description: Given an n by n grid of letters, and a list of words, find the location in the grid where the word can be found. A word matches a straight, contiguous line of letters in the grid. The match could either be done horizontally (left or right) or vertically (up or down) or along any diagonal either right to left or from left to right.
#  Student Name: Anna Dougharty
#  Student UT EID: amd5933
#  Course Name: CS 313E
#  Unique Number: 52600
#  Date Created: 9/2/2021
#  Date Last Modified: 9/3/2021

import sys

# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def rows(puzzle, word_bank, write_words):
  rows_front = []
  rows_back = []

  for row in puzzle:
    #go through the rows and join them into one large string
    line_front = ''.join(row)
    #same thing but backwards
    line_back = line_front[::-1]
    #14 elements of rows front and 14 elements of rows back
    rows_front.append(line_front)
    rows_back.append(line_back)

  num_row = 0
  #check all of the elements in rows_front for the words in the word bank
  for row in rows_front:
    num_row += 1
    for word in word_bank:
      num_column = row.find(word)
      #find() will return the first occurence of the word or -1 if not found
      if num_column != -1:
        #append found values to the write words dictionary if find() found the word
        write_words[word][0] = num_row
        write_words[word][1] = num_column + 1

  #now the same for rows_back
  num_row = 0
  for row in rows_back:
    num_row += 1
    for word in word_bank:
      num_column = row.find(word)
      if (num_column != -1):
        (write_words[word])[0] = num_row
        (write_words[word])[1] = (len(row) - (num_column))

def columns(puzzle, word_bank, write_words):
  columns_up = []
  columns_down = []

  rotated_puzzle = zip(*puzzle)

  for column in rotated_puzzle:
    line_front = ''.join(column)
    line_back = line_front[::-1]
    columns_down.append(line_front)
    columns_up.append(line_back)

  num_column = 0
  for column in columns_down:
    num_column += 1
    for word in word_bank:
      num_row = column.find(word)
      if (num_row != -1):
        (write_words[word])[0] = num_row +1
        (write_words[word])[1] = num_column

  num_column = 0
  for column in columns_up:
    num_column += 1
    for word in word_bank:
      num_row = column.find(word)
      if num_row != -1:
        (write_words[word])[0] = (len(column) - num_row)
        (write_words[word])[1] = num_column

def diagonals(puzzle, word_bank, k, write_words):

  bottom_top = [[] for i in range(2 * len(puzzle)-1)]
  for row in range(len(puzzle)):
    for col in range(len(puzzle[row])):
      bottom_top[row+col].append(puzzle[col][row])

  top_bottom = [[] for i in range(2 * len(puzzle)-1)]
  #print(top_bottom)
  for row in range(len(puzzle)):
    for col in range(len(puzzle[row])):
      top_bottom[row-col].append(puzzle[row][col])

  #print('top:',top_bottom)

  direction = True
  search_diagonal(word_bank, bottom_top, direction, write_words)
  direction = False
  search_diagonal(word_bank, top_bottom, direction, write_words)

def search_diagonal(word_bank, bottom_top, direction, write_words):
  diagonals_front = []
  diagonals_back = []

  for row in bottom_top:
    line_front = ''.join(row)
    line_back = line_front[::-1]
    diagonals_front.append(line_front)
    diagonals_back.append(line_back)
  print(diagonals_front)

  num_row = 0
  for row in diagonals_front:
    for word in word_bank:
      num_column = row.find(word)
      if (num_column != -1):
        print(num_column)
        if direction:
          num_row = diagonals_front[num_column]
          num_column += 1
          (write_words[word])[0] = num_row
          (write_words[word])[1] = num_column
        else:
          num_row = len(row)
          num_column += 1
          (write_words[word])[0] = num_row
          (write_words[word])[1] = num_column

def main():
  fileOpen = sys.stdin.readline().strip()
  fileOpen = int(fileOpen)
  x = sys.stdin.readline()
  # creating an empty 2D list
  puzzle = [[0 for i in range(fileOpen)] for j in range(fileOpen)]
  for i in range(fileOpen):
    line = sys.stdin.readline().strip()
    line = line.split()
    # line is now list
    puzzle[i] = line
    #print(puzzle[i])
  y = sys.stdin.readline()
  word_bank = []
  k = int(sys.stdin.readline())
  for i in range(k):
    line = sys.stdin.readline().strip()
    word_bank.append(line.strip('\n'))

  write_words = dict((word,[0,0]) for word in word_bank)
  diagonals(puzzle, word_bank, k, write_words)
  columns(puzzle, word_bank, write_words)
  rows(puzzle, word_bank, write_words)


  for key, values in write_words.items():
    string_val1 = values[0]
    string_val2 = values[1]
    string_set = "{}: ({}, {})".format(str(key), string_val1, string_val2)
    print(string_set)


if __name__ == "__main__":
  main()
