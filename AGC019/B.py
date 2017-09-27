def conbi(n):
	return int(n*(n-1)/2)

A = input("")
num = 1 + conbi(len(A)) #l_C_2
uniq = list(set(A))
for i in uniq:
	num -= conbi(A.count(i))
print(num)
