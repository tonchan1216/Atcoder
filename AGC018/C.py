import math

##関数##
def sum_coin(a,b):
	#転置して該当列を合算
	temp1 = list(map(list, zip(*a)))
	temp2 = list(map(list, zip(*b)))
	coins =	sum(temp1[2][:Y]) + sum(temp1[3][Y:]) + sum(temp2[3][:(-X)]) + sum(temp2[1][(-X):])
	return coins

###入力###
input1 = input("").split(" ")
X = int(input1[0])
Y = int(input1[1])
Z = int(input1[2])
N = X + Y + Z
temp = [ input() for _ in range(N) ]
matrix = [None]*N
for i in range(N):
	a = int(temp[i].split(" ")[0])
	b = int(temp[i].split(" ")[1])
	c = int(temp[i].split(" ")[2])
	matrix[i] = [i, a, b, c, (a-b), (b-c), (c-a)]

###処理###
matrix.sort(key=lambda k: k[4]) #(金-銀)で昇順ソート
head = sorted(matrix[:Y], key=lambda k: k[5], reverse=True) #(銀-銅)で降順ソート
tail = sorted(matrix[Y:], key=lambda k: k[6], reverse=True) #(銅-金)で降順ソート
result = sum_coin(head, tail)

# Y<=k<=(N-X)の中でコイン最大値を求める
for k in range(Y,N-X):
	#headにmatrix[Y+1]を追加
	if head[0][5] < matrix[k][5]:
		p = 0
	elif head[-1][5] > matrix[k][5]:
		p = len(head) - 1
	else:
		#二分探索
		start = 0
		last = len(head) - 1
		p = last
		while (last-start) > 1:
			j = math.ceil((start+last)/2)
			if head[j][5] < matrix[k][5] :
				last = j
			elif head[j][5] > matrix[k][5]:
				start = j
			else:
				p = j
				break
			p = last
	head.insert(p,matrix[k])
	
	#tailからmatrix[Y+1]を削除
	tail.pop(tail.index(matrix[k]))
	coins = sum_coin(head, tail)
	#暫定１位更新
	if result < coins:
		result = coins

###出力###
print(result)