
#  File: Boxes.py

#  Description: You will read your input from standard input.
#  The list of boxes will be in a file called boxes.in. The
#  first line gives the number of boxes n. The next n lines gives a
#  set of three integers separated by one or more spaces.
#  These integers represent the 3 dimensions of a box. Since you
#  can rotate the boxes, the order of the dimensions does not matter.
#  It may be to your advantage to sort the dimensions in ascending order.


#  Student Name: Anna Dougharty

#  Student UT EID: amd5933

#  Course Name: CS 313E

#  Unique Number: 52600

#  Date Created: 10/14/2021

#  Date Last Modified:

import sys

# generates all subsets of boxes, stores them in all_box_subsets
# box_list is a list of boxes thats already been sorted
# sub_set is a list of the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes
def sub_sets_boxes(box_list, sub_set, idx, all_box_subsets):
    list_length = len(box_list)
    # base case once full box_list has been fully iterated through
    if idx == list_length:
        all_box_subsets.append(sub_set)
        return all_box_subsets
    else:
        # make a copy to track which box was recently appended
        # for implicit backtracking purposes
        sub_set_copy = sub_set[:]
        sub_set.append(box_list[idx])

        # recursively check both updated sub_set list and its copy w/o newest append
        sub_sets_boxes(box_list, sub_set, idx + 1, all_box_subsets)
        sub_sets_boxes(box_list, sub_set_copy, idx + 1, all_box_subsets)


# goes through all the subset of boxes; only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track of the largest subset 
def largest_nesting_subsets(all_box_subsets):
    # init counter to track if subset does not fit inside next subset
    counter = 0
    # tracks real nested boxes
    nested_boxes = []

    for subset in all_box_subsets:
        # use enumerate to track both index and value of each subset
        for index, val in enumerate(subset):
            # adds one to counter if subset does not fit
            if index + 1 != len(subset) and not does_fit(val, subset[index + 1]):
                counter += 1
        # append subset to nested list only if does fit returns true
        if counter == 0:
            nested_boxes.append(subset)
        # reset the counter for each subsequent subset
        counter = 0

    # parse through nested_boxes to find max length
    max_length = 0
    for subset in nested_boxes:
        if len(subset) >= max_length:
            max_length = len(subset)

    # iterate through and append only the largest subsets to
    # largest_subset_list
    largest_subset_list = []
    for subset in nested_boxes:
        if len(subset) == max_length:
            largest_subset_list.append(subset)

    return largest_subset_list


# returns True if box1 fits inside box2
def does_fit(box1, box2):
    return box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2]


def main():
    # read the number of boxes
    line = sys.stdin.readline()
    line = line.strip()
    num_boxes = int(line)

    # create an empty list for the boxes
    box_list = []

    # read the boxes from the file
    for i in range(num_boxes):
        line = sys.stdin.readline()
        line = line.strip()
        box = line.split()
        for j in range(len(box)):
            box[j] = int(box[j])
        box.sort()
        box_list.append(box)

    '''
    # print to make sure that the input was read in correctly
    print(box_list)
    print()
    '''

    # sort the box list
    box_list.sort()

    '''
    # print the box_list to see if it has been sorted.
    print(box_list)
    print()
    '''

    # create an empty list to hold all subset of boxes
    all_box_subsets = []

    # create a list to hold a single subset of boxes
    sub_set = []

    # generate all subsets of boxes and store them in all_box_subsets
    sub_sets_boxes(box_list, sub_set, 0, all_box_subsets)

    # all_box_subsets should have a length of 2^n where n is the number
    # of boxes

    # go through all the subset of boxes and only store the
    # largest subsets that nest in all_nesting_boxes
    all_nesting_boxes = largest_nesting_subsets(all_box_subsets)

    # print the largest number of boxes that fit
    print(len(all_nesting_boxes[0]))
    # print the number of sets of such boxes
    print(len(all_nesting_boxes))


if __name__ == "__main__":
    main()

