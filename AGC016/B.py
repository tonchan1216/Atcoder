N = int(input())
A = list(map(int,input("").split(" ")))

max_A = max(A)
min_A = min(A)

if (max_A - min_A) > 1:
	print("NO")
elif (max_A - min_A) == 1:
	x = A.count(max_A-1)
	y = A.count(max_A)
	if x < max_A and 2*(max_A-x) <= y:
		print("YES")
	else:
		print("NO")
else:
		if max_A == (N-1) or max_A*2 <= N:
			print("YES")
		else:
			print("NO")
	