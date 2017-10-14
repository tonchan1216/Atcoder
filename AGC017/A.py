input1 = list(map(int,input("").split(" ")))
A = list(map(int,input("").split(" ")))
N = input1[0]
P = input1[1]

even = []
odd = []
for a in A:
	if a % 2 == 0:
		even.append(a)
	else:
		odd.append(a)

if len(odd) == 0:
	if P == 0:
		result = 2**N
	else:
		result = 0
else:
	result = 2**len(even) * 2**(len(odd)-1)

print(result)