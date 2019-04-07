# A thief will steal from a sequence of objects of different value. When stealing an object, he can not steal the two on its right or the two on its left. What objects must he steal to maximize his benefit?

def best_robbery(l,m):

	n = len(l)
	if n == 0:
		return m
	elif n == 1:
		return m + l[0]
	else:
		new_max = -1
		for i in range(n):
			max_aux = m + l[i]

			removed_elems = []
			window_size = 5
			j = -2
			while i + j < 0:
				j += 1
				window_size -= 1
			while i + j < len(l) and window_size > 0:
				removed_elems.append(l[i + j])
				l.pop(i + j)
				window_size -= 1

			max_aux = best_robbery(l,max_aux)
			if max_aux > new_max:
				new_max = max_aux

			while len(removed_elems) > 0:
				l.insert(i + j, removed_elems.pop(-1))

		return new_max

# Simple tests

print(best_robbery([],0))
print(best_robbery([10],0))
print(best_robbery([10,20],0))
print(best_robbery([10,20,10],0))
print(best_robbery([10,20,10,10,30,10],0))
print(best_robbery([0,1,2,3,4,5,6,7,8,9],0))
print(best_robbery([0,1,2,3,40,5,6,7,8,9],0))
print(best_robbery([0,1,2,3,40,5,6,6,7],0))



