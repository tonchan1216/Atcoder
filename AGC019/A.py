input1 = input("").split(" ")
Q = int(input1[0])
H = int(input1[1])
S = int(input1[2])
D = int(input1[3])
N = int(input(""))

print((N%2) * min(Q*4,H*2,S) + (N//2) * min(Q*8,H*4,S*2,D))