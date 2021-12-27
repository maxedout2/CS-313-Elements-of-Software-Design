#  File: Graph.py

#  Description: Create a graph of cities and test out two types of search algorithms
#  as well as deleting edges and vertices.

#  Student Name: Anna Dougharty

#  Student UT EID: amd5933

#  Course Name: CS 313E

#  Unique Number: 52600

#  Date Created: 22 Nov 2021

#  Date Last Modified: 22 Nov 2021

import sys


class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty(self):
        return len(self.stack) == 0

    # return the number of elements in the stack
    def size(self):
        return len(self.stack)


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    # check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # return the size of the queue
    def size(self):
        return len(self.queue)


class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)


class Graph(object):
    def __init__(self):
        self.Vertices = []
        self.adjMat = []

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if label == (self.Vertices[i]).get_label():
                return True
        return False

    # given the label get the index of a vertex
    def get_index(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if label == (self.Vertices[i]).get_label():
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        if self.has_vertex(label):
            return

        # add vertex to the list of vertices
        self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        nVert = len(self.Vertices)
        for i in range(nVert - 1):
            (self.adjMat[i]).append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(nVert):
            new_row.append(0)
        self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight(self, fromVertexLabel, toVertexLabel):
        # if both vertexes (i.e. edge) doesn't exist, return -1
        if self.has_vertex(fromVertexLabel) is False or self.has_vertex(toVertexLabel) is False:
            return -1
        else:
            # find indexes for both vertices
            fromVertexIndex = self.get_index(fromVertexLabel)
            toVertexIndex = self.get_index(toVertexLabel)
            # find weight of the edge
            weight = self.adjMat[fromVertexIndex][toVertexIndex]
            # if weight is 0, then edge doesn't exist, so return -1
            if weight == 0:
                return -1

        return weight

    # get a list of immediate neighbors that you can go to from a vertex
    # return a list of indices or an empty list if there are none
    def get_neighbors(self, vertexLabel):
        # get number of vertices and assign index to specific vertex passed through method
        nVert = len(self.Vertices)
        vertexIndex = self.get_index(vertexLabel)

        # create empty list to track any neighbors
        neighbors = []
        for i in range(nVert):
            if self.adjMat[vertexIndex][i] > 0:
                # make sure to append the label of the neighboring vertices
                neighbors.append(self.Vertices[i].label)

        return neighbors

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # get a copy of the list of Vertex objects
    def get_vertices(self):
        return self.Vertices[:]

    # do a depth first search in a graph
    def dfs(self, v):
        # create the Stack
        theStack = Stack()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theStack.push(v)

        # visit all the other vertices according to depth
        while not theStack.is_empty():
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            if u == -1:
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theStack.push(u)

        # the stack is empty, let us rest the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # do the breadth first search in a graph
    def bfs(self, v):
        theQueue = Queue()

        # label first vertex as visited to track visited vertices
        self.Vertices[v].visited = True
        theQueue.enqueue(v)

        while not theQueue.is_empty():
            # dequeued is the vertex at the front of the queue that was just popped
            dequeued = theQueue.dequeue()
            print(self.Vertices[dequeued])
            # find the next unvisited vertex
            next_vertex = self.get_adj_unvisited_vertex(dequeued)
            # loop while indexes are found
            while next_vertex != -1:
                # add to end of queue
                theQueue.enqueue(next_vertex)
                self.Vertices[next_vertex].visited = True
                # find next unvisited vertex
                next_vertex = self.get_adj_unvisited_vertex(dequeued)

        # if theQueue is empty, reset 'visited' booleans to False
        nVert = len(self.Vertices)
        for i in range(nVert):
            self.Vertices[i].visited = False

        return

    # delete an edge from the adjacency matrix
    # delete a single edge if the graph is directed
    # delete two edges if the graph is undirected
    def delete_edge (self, fromVertexLabel, toVertexLabel):
        # find index for both vertices
        fromVertexIndex = self.get_index(fromVertexLabel)
        toVertexIndex = self.get_index(toVertexLabel)

        # if graph is undirected, delete both edges
        if self.adjMat[fromVertexIndex][toVertexIndex] == self.adjMat[toVertexIndex][fromVertexIndex]:
            self.adjMat[fromVertexIndex][toVertexIndex] = 0
            self.adjMat[toVertexIndex][fromVertexIndex] = 0
        # if graph is directed, delete only one edge
        else:
            self.adjMat[fromVertexIndex][toVertexIndex] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex (self, vertexLabel):
        vertexIndex = self.get_index(vertexLabel)

        # delete index itself
        self.Vertices.pop(vertexIndex)

        # delete edges to vertex
        for i in self.adjMat:
            i.pop(vertexIndex)

        # delete the entire row associated with vertex
        self.adjMat.pop(vertexIndex)

    # method to print adjacency matrix
    def print_adj_mat(self, nVert):
        for i in range(nVert):
            for j in range(nVert):
                # exclude whitespace after printing last value in row
                if j == nVert - 1:
                    print(self.adjMat[i][j], end='')
                # print whitespace if NOT last value in row
                else:
                    print(self.adjMat[i][j], end=' ')
            print()
        print()


def main():
    # create the Graph object
    cities = Graph()

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    num_vertices = int(line)

    # read the vertices to the list of Vertices
    for i in range(num_vertices):
        line = sys.stdin.readline()
        city = line.strip()
        cities.add_vertex(city)

    # read the number of edges
    line = sys.stdin.readline()
    line = line.strip()
    num_edges = int(line)

    # read each edge and place it in the adjacency matrix
    for i in range(num_edges):
        line = sys.stdin.readline()
        edge = line.strip()
        edge = edge.split()
        start = int(edge[0])
        finish = int(edge[1])
        weight = int(edge[2])

        cities.add_directed_edge(start, finish, weight)

    # read the starting vertex for dfs and bfs
    line = sys.stdin.readline()
    start_vertex = line.strip()

    # get the index of the starting vertex
    start_index = cities.get_index(start_vertex)

    # do the depth first search
    print("Depth First Search")
    cities.dfs(start_index)
    print()

    # do the breadth first search
    print("Breadth First Search")
    cities.bfs(start_index)
    print()

    # TEST deletion of an edge
    # read edge vertices to delete
    edge_vertices = sys.stdin.readline().strip().split()
    fromVertexLabel = edge_vertices[0]
    toVertexLabel = edge_vertices[1]
    cities.delete_edge(fromVertexLabel, toVertexLabel)
    # print adjacency matrix to console
    print("Deletion of an edge")
    print()
    print("Adjacency Matrix")
    cities.print_adj_mat(num_vertices)

    # TEST deletion of a vertex
    vertexLabelDelete = sys.stdin.readline().strip()
    cities.delete_vertex(vertexLabelDelete)
    # print list of cities and corresponding adjacency matrix
    print("Deletion of a vertex")
    print()
    print("List of Vertices")
    for city in cities.Vertices:
        print(city)

    print()
    print("Adjacency Matrix")
    # account for recently deleted vertex by subtracting 1
    cities.print_adj_mat(num_vertices - 1)
    print()



    # test deletion of a vertex

if __name__ == "__main__":
    main()
