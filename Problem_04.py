seq=input()
lis=[]

var=''
for x in seq:
	if x ==',':
		lis.append(var)
		var=''
		continue
		

	var=var+x

lis.append(var)
print(lis)
print(tuple(lis))

