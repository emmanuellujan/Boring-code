# Generate indexes.
# Example
#	input: 2, 3, 3
#	output: 
#			0 [0, 0, 0]
#			1 [0, 0, 1]
#			2 [0, 1, 0]
#			3 [0, 1, 1]
#			4 [0, 2, 0]
#			5 [0, 2, 1]
#			6 [1, 0, 0]
#			7 [1, 0, 1]
#			8 [1, 1, 0]
#			9 [1, 1, 1]
#			10 [1, 2, 0]
#			11 [1, 2, 1]
#			12 [2, 0, 0]
#			13 [2, 0, 1]
#			14 [2, 1, 0]
#			15 [2, 1, 1]
#			16 [2, 2, 0]
#			17 [2, 2, 1]

def generate_indexes(l_limits):
	n = len(l_limits)

	m = 1
	for i in range(n):
		m = m * l_limits[i]

	l_idx = [-1] + [0] * (n - 1)

	for i in range(m):

		l_idx[0] = l_idx[0] + 1

		j = 0
		while j < n - 1 and l_idx[j] == l_limits[j]:
			l_idx[j] = 0
			l_idx[j + 1] = l_idx[j + 1] + 1
			j = j + 1

		if l_idx[n - 1] == l_limits[n - 1]:
			l_idx[n - 1] = 0

		print i, l_idx[::-1] 


# Simple test

#l_limits = [2, 2, 2, 2, 2, 2, 2, 2]
l_limits = [ 2, 3, 3 ]
print "input: ", l_limits
print "output: "
generate_indexes(l_limits)
