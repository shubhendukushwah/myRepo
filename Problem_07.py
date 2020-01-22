ip=input("Enter Digit ")
ip=ip.split(',')
x=int(ip[0])
y=int(ip[1])
arr=[]
for l in range(x):
    ls=[]
    for m in range(y):
        ls.append(l*m)
    arr.append(ls)

print(arr)
