from collections import Counter
import re

def find_index(char, text):
	pattern = r""+char
	iterator = re.finditer(pattern, text)
	temp = []
	for match in iterator:
		temp.append(match.start())
	return temp

origin = input()
t_len = len(origin)
counter = Counter(origin)
max_num = max([(v,k) for k,v in counter.items()])[0]
max_list = [k for k,v in counter.items() if v == max_num]



if max_num == t_len:
	result = 0
else:
	r_list = []
	for c in max_list:
		t = origin
		t_len = len(origin)
		calc = 0
		while t_len > 0:
			temp = ""
			for i in range(t_len-1):
				if t[i] == c or t[i+1] == c:
					temp += c
				else:
					temp += t[i]
			t = temp
			t_len = len(t)
			calc += 1
			#Check
			if t.count(c) == t_len:
				break
		r_list.append(calc)
		result = min(r_list)
print(result)
