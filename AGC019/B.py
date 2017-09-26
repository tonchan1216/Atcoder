A = input("")
num = 1
for i in range(len(A)-1):
	num += len(A[i+1:].replace(A[i],''))
print(num)