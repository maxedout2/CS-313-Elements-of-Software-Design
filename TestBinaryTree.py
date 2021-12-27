#  File: TestBinaryTree.py

#  Description: Create various methods to test functionality of a binary tree.

#  Student Name: Anna Dougharty

#  Student UT EID: amd5933

#  Course Name: CS 313E

#  Unique Number: 52600

#  Date Created: Nov 14 2021

#  Date Last Modified: Nov 15 2021


import sys


class Node(object):
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


class Tree(object):
    def __init__(self):
        self.size = 0
        self.height = 0
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        # if root does not exist/is empty, set to new node
        if self.root is None:
            self.root = new_node
            return
        # otherwise iterate through tree
        else:
            # init current and parent tracking nodes
            current = self.root
            parent = self.root

            # loop until end of tree is reached
            while current is not None:
                # parent node moves down to current node
                parent = current
                if data < current.data:
                    # assign left child if data is less than current node data
                    current = current.lChild
                else:
                    # assign right child if data is greater than or equal to
                    # current node data
                    current = current.rChild

            # once final node has been reached, assign correct child node (L/R)
            # depending on size of data compared to parent node data
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node

            # once node has been added, increment tree size by 1
            self.size += 1

    # Returns true if two binary trees are similar
    def is_similar(self, pNode):
        current_1 = self.root
        current_2 = pNode.root
        return self.is_similar_node(current_1, current_2)

    # Helper method to compare individual current nodes
    # Utilizes recursion to iterate through tree
    def is_similar_node(self, current_1, current_2):
        # if both nodes are empty, then they are similar
        if current_1 is None and current_2 is None:
            return True

        # if one of the nodes is empty, but other is not,
        # then they are not similar
        if current_1 is None and current_2 is not None:
            return False
        elif current_1 is not None and current_2 is None:
            return False
        # if data between both nodes is different, then they are not similar
        elif current_1.data != current_2.data:
            return False
        # iterate through children using recursion
        else:
            return self.is_similar_node(current_1.lChild, current_2.lChild) and \
                   self.is_similar_node(current_1.rChild, current_2.rChild)

    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        current = self.root
        # init list of nodes
        nodes = []
        # helper function takes care of empty tree
        self.get_level_helper(current, 0, level, nodes)
        # return the list of nodes
        return nodes

    # Utilize recursion to traverse levels of tree
    def get_level_helper(self, node, current_level, level, nodes):
        # if node is empty, nothing to return
        if node is None:
            return
        # if level has been reached, append current node to nodes list
        elif current_level == level:
            nodes.append(node)
        # iterate through left and right children until level is reached
        else:
            self.get_level_helper(node.lChild, current_level + 1, level, nodes)
            self.get_level_helper(node.rChild, current_level + 1, level, nodes)

    # Returns the height of the tree
    def get_height(self):
        current = self.root
        # create list to track heights as recursion occurs
        height_list = [0]
        self.get_height_helper(current, 0, height_list)

        # sort from least to greatest and return largest
        height_list.sort()
        return height_list[-1] - 1

    def get_height_helper(self, node, height, height_list):
        # if node is empty, append length to height list
        if node is None:
            height_list.append(height)
        # iterate through left and right children and track heights
        else:
            height += 1
            self.get_height_helper(node.lChild, height, height_list)
            self.get_height_helper(node.rChild, height, height_list)

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes (self):
        current = self.root
        # if tree size is 0, then 0 nodes exist
        if self.size == 0:
            return 0
        else:
            return self.num_nodes_helper(current)

    def num_nodes_helper(self, node):
        # if node is empty
        if node is None:
            return 0
        # move to children nodes and add 1 for count of current node
        else:
            return 1 + self.num_nodes_helper(node.lChild) + self.num_nodes_helper(node.rChild)


def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line))  # converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line))  # converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line))  # converts elements into ints

    # insert values into tree1
    tree1 = Tree()
    for num in tree1_input:
        tree1.insert(num)

    # insert values into tree2
    tree2 = Tree()
    for num in tree2_input:
        tree2.insert(num)

    # insert values into tree3
    tree3 = Tree()
    for num in tree3_input:
        tree3.insert(num)

    # Test your method is_similar()
    if tree1.is_similar(tree2):
        print("1 and 2 are similar!")
    else:
        print("tree1 & tree2 are NOT similar")

    if tree1.is_similar(tree3):
        print("tree1 & tree3 are similar")
    else:
        print("tree1 & tree3 are NOT similar")

    # Print the various levels of two of the trees that are different
    print("tree1 lvl 2:", tree1.get_level(2))
    print("tree2 lvl 2:", tree2.get_level(2))

    # Get the height of the two trees that are different
    print("1 height:", tree1.get_height())
    print("3 height:", tree3.get_height())

    # Get the total number of nodes a binary search tree
    print('1 num nodes:', tree1.num_nodes())
    print('2 num nodes:', tree2.num_nodes())
    print('3 num nodes:', tree3.num_nodes())


if __name__ == "__main__":
    main()
