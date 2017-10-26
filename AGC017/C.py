from collections import OrderedDict

input1 = list(map(int,input("").split(" ")))
A = list(map(int,input("").split(" ")))
N = input1[0]
M = input1[1]
temp = [ input() for _ in range(M) ]
XY = [None] * M
for i in range(M):
 	XY[i] = list(map(int,temp[i].split(" ")))

A_uniq = list(set(A))
magic = {}
# O(N)
for ball in A_uniq:
	ball_num = A.count(ball)
	magic[ball] = list(range((ball-ball_num+1), ball+1))

print(magic)

# O(M)
for m in range(M):
	i = A[XY[m][0]-1] #before
	j = XY[m][1] #after
	if len(magic[i]) > 1:
		magic[i].pop(0)
	else:
		del magic[i]
	if j in magic :
		magic[j].insert(0, min(magic[j])-1)
	else:
		magic[j] = [j]
	print(magic)
	temp = [flatten for inner in magic.values() for flatten in inner]
	#temp = map(lambda x: x+temp, magic.values())
	magic_uniq = list(set(temp))
	#print(len(temp) - len(magic_uniq))