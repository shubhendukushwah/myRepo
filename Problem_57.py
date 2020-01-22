ls1=[1,3,6,78,35,55]
ls2=[12,24,35,24,88,120,155]
temp=[]
for x in ls1:
	if x in ls2:
		temp.append(x)
print(temp)		
