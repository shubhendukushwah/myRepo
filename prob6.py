import math
d=input()
i=[]
s=''
for x in d:
	if x is ',':
		s=int(s)
		i.append(s)
		s=''
		continue
	s=s+x
s=int(s)
i.append(s)

def sqr_fun(*i):
	ans=''
	c=50
	h=30
	for x in i:
		ans=ans+str(round(math.sqrt((2*c*x)/h)))
		if x!=i[len(i)-1]:
			ans=ans+','
	return ans

print(sqr_fun(*i))



