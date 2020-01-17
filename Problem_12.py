ip=input()
ip=ip.split(',')
num1=ip[0]
num2=ip[1]

f=0
for x in range(int(num1),int(num2)):
    temp=str(x)
    for y in temp:
        if int(y)%2!=0:
            f=1
            break
    if f==0:
        print(temp,end=',')
    f=0