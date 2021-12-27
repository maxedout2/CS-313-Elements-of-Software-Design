#  File: Hull.py

#  Description: Using Graham's scan algorithm, draw the largest
#  convex shape around a given number of points. For the points
#  that make up the convex shape, print out each of the coordinates
#  in clockwise order. Then find the total area of this shape.

#  Student Name: Anna Dougharty

#  Student UT EID: amd5933

#  Course Name: CS 313E

#  Unique Number: 52600

#  Date Created: 9/26/2021

#  Date Last Modified: 9/26/2021


import sys
import math


class Point(object):
    # constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # equality tests of two Points
    def __eq__(self, other):
        tol = 1.0e-8
        return (abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol)

    def __ne__(self, other):
        tol = 1.0e-8
        return (abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol)

    def __lt__(self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return False
            else:
                return self.y < other.y
        return self.x < other.x

    def __le__(self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return True
            else:
                return self.y <= other.y
        return self.x <= other.x

    def __gt__(self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return False
            else:
                return self.y > other.y
        return self.x > other.x

    def __ge__(self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return True
            else:
                return self.y >= other.y
        return self.x >= other.x


# # Input: p, q, r are Point objects
# # Output: compute the determinant and return the value
def det(p, q, r):
    # calculate the determinant of 3 x 3 matrix with 1s on the leftmost column
    deter1 = q.y * (p.x - r.x)
    deter2 = r.y * (q.x - p.x)
    deter3 = p.y * (r.x - q.x)
    deter = deter1 + deter2 + deter3
    return deter


# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull(sorted_points):
    # create empty lists for both upper and lower hulls
    upper_hull = []
    lower_hull = []

    # append first 2 points into upper hull
    upper_hull.append(sorted_points[0])
    upper_hull.append(sorted_points[1])
    # append rest of points to upper hull and verify if only convex points
    for i in range(2, len(sorted_points)):
        upper_hull.append(sorted_points[i])
        # loop checks for both min. 3 Points in list and if last 3 points are NOT turning right
        while len(upper_hull) >= 3 and (det(upper_hull[-3], upper_hull[-2], upper_hull[-1]) >= 0):
            del upper_hull[-2]

    # append last 2 points into lower hull
    lower_hull.append(sorted_points[-1])
    lower_hull.append(sorted_points[-2])
    # append rest of points to lower hull and verify if only convex points
    for i in range(len(sorted_points) - 3, -1, -1):
        lower_hull.append(sorted_points[i])
        # loop checks for both min. 3 Points in list and if last 3 points are NOT turning right
        while len(lower_hull) >= 3 and (det(lower_hull[-3], lower_hull[-2], lower_hull[-1]) >= 0):
            del lower_hull[-2]
    # remove first and last points from lower hull to prevent duplicating with upper hull
    del lower_hull[0]
    del lower_hull[-1]

    # append lower hull to upper hull
    for i in range(len(lower_hull)):
        upper_hull.append(lower_hull[i])
    convex_hull_list = upper_hull
    return convex_hull_list


# # Input: convex_poly is a list of Point objects that define the
# #        vertices of a convex polygon in order
# # Output: computes and returns the area of a convex polygon
def area_poly(convex_poly):
    total_area = 0

    # area calculation is done with a two-part equation
    # 1. calculate total over-summed area (including gaps)
    for i in range(len(convex_poly) - 1):
        total_area += float(convex_poly[i].x * convex_poly[i + 1].y)
    total_area += float(convex_poly[-1].x * convex_poly[0].y)

    # 2. calculate extra over-summed area (gaps) and subtract to result in net area
    for i in range(len(convex_poly) - 1):
        total_area -= float(convex_poly[i].y * convex_poly[i + 1].x)
    total_area -= float(convex_poly[-1].y * convex_poly[0].x)

    # find half of the net total area to get the true area
    total_area = 0.5 * abs(total_area)
    return total_area


# # Input: no input
# # Output: a string denoting all test cases have passed
def test_cases():
    # write your own test cases
    return "all test cases passed"


def main():
    # create an empty list of Point objects
    points_list = []

    # read number of points
    line = sys.stdin.readline()
    line = line.strip()
    num_points = int(line)

    # read data from standard input
    for i in range(num_points):
        line = sys.stdin.readline()
        line = line.strip()
        line = line.split()
        x = int(line[0])
        y = int(line[1])
        points_list.append(Point(x, y))

    # sort the list according to x-coordinates
    sorted_points = sorted(points_list)

    # get the convex hull
    convex_shape = convex_hull(sorted_points)

    # run your test cases
    # test_cases()

    # print your results to standard output
    # print the convex hull
    print("Convex Hull")
    for point in convex_shape:
        print(point)
    print()
    # get the area of the convex hull
    convex_area = area_poly(convex_shape)
    # print the area of the convex hull
    print("Area of Convex Hull =", convex_area)


if __name__ == "__main__":
    main()
