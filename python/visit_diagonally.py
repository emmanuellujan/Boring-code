# Prints matrix diagonally

def visit_diagonally(A):
	n = len(A)
	m = len(A[0])

	for i in range(n):
		j = 0
		while 0 <= i and i < n and 0 <= j and j < m:
			print(A[i][j])
			i -= 1
			j += 1

	for j in range(1,m):
		i = n - 1
		while 0 <= i and i < n and 0 <= j and j < m:
			print(A[i][j])
			i -= 1
			j += 1


# Simple tests

print("test 0")
A = [[]]
visit_diagonally(A)

print("test 1")
A = [[1]]
visit_diagonally(A)

print("test 1x3")
A = [[1,2,3]]
visit_diagonally(A)

print("test 3x1")
A = [[1],
	 [2],
	 [3]]
visit_diagonally(A)

print("test 3x4")
A = [[1, 3, 6, 9],
	 [2, 5, 8, 11],
	 [4, 7, 10, 12]]
visit_diagonally(A)

print("test 6x3")
A = [[1, 3, 6],
	 [2, 5, 9],
	 [4, 8, 12],
	 [7, 11, 15],
	 [10, 14, 17],
	 [13, 16, 18]]
visit_diagonally(A)

print("test 3x6")
A = [[1, 3,  6,  9, 12, 15],
	 [2, 5,  8, 11, 14, 17],
	 [4, 7, 10, 13, 16, 18]]
visit_diagonally(A)




