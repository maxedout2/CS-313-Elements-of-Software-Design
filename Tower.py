#  File: Tower.py

#  Description: tower of hanoi problem with 4 pegs

#  Student's Name: anna dougharty

#  Student's UT EID: amd5933

#  Course Name: CS 313E

#  Unique Number: 52600

#  Date Created: 10/11/2021

#  Date Last Modified: 10/11/2021

import sys
import math

# Input: n the number of disks
# Output: returns the number of transfers using four needles
# Input: n the number of disks
# Output: returns the number of transfers using four needles
def num_moves (n):

  nummoves = []

  if n > 0:
    transfer(n, nummoves)

  if len(nummoves) == 0:
    nummoves.append(0)

  # store the number of moves in first element of list
  return nummoves[0]

# the 4 tower peg solution
def transfer (n, nummoves):
  k = round(n - math.sqrt(2 * n + 1) + 1)

  # start the count for the number of moves
  if len(nummoves) == 0:
    nummoves.append(0)

  # special case if theres 1 disk
  if n == 1:
    nummoves[0] = nummoves[0] + 1

  # special case if there are 2 disks
  elif n == 2:
    nummoves[0] = nummoves[0] + 3

  else:
    towers(n - k - 1, nummoves)
    nummoves[0] = nummoves[0] + 1
    towers(n - k - 1, nummoves)
    transfer(k, nummoves)
    transfer(k, nummoves)

# Recursive towers helper to count the # of moves with n disks (3 tower peg solution)
def towers (n, nummoves):

  # start the count for number of moves
  if len(nummoves) == 0:
    nummoves.append(0)

  # special case if theres 1 disk
  if n == 1:
    nummoves[0] = nummoves[0] + 1

  else:
    towers(n - 1, nummoves)
    nummoves[0] = nummoves[0] + 1
    towers(n - 1, nummoves)

def main():
  for line in sys.stdin:
    line = line.strip()
    num_disks = int (line)
    print (num_moves (num_disks))

if __name__ == "__main__":
  main()
