'''
Python Challenge 10
Aria Outten 20190226
'''
a = ['1']

for no in range(0,31):
	temp = a[no]
	new = ''
	count = 1
	for i in range(0,len(temp)):
		if i != 0:
			try:
				if temp[i] == temp[i+1]:
					count += 1
				else:
					new += (str(count) + temp[i])
					count = 1
			except Exception:
				new += (str(count) + temp[i])
				count = 1
		else:
			try:
				if temp[i] == temp[i+1]:
					count += 1
				else:
					new += (str(count) + temp[i])
					count = 1
			except Exception:
				new += (str(count) + temp[i])
				count = 1
	a.append(new)
#print(a)
print(len(a[30]))
