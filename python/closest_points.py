# Returns the k points closer to the origin, given a list of points (x,y)

import math 

def closest_points(points,epsilon):
	s = []
	for p in points:
		r = math.sqrt(p[0] * p[0] + p[1] * p[1])
		if r <= epsilon:
			s.append(p)
	return s


# Simple test

points = []
points.append([0,0])
points.append([1,0])
points.append([0,1])
points.append([0,-1])
points.append([-1,0])
points.append([0.5,0.5])
points.append([0.5,-0.5])
points.append([-0.5,0.5])

points.append([1,0.5])
points.append([0.5,1])
points.append([0.5,-1])
points.append([-1,0.5])
points.append([2,0])
points.append([0,2])
points.append([0,-2])
points.append([-2,0])
points.append([3,0])
points.append([0,3])
points.append([0,-3])
points.append([-3,0])

epsilon = 1
print(closest_points(points,epsilon))

