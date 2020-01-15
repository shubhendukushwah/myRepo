ls=[12,24,35,24,88,120,155,88,120,155]
temp=[]
for x in ls:
	if x not in temp:
		temp.append(x)
print(temp)