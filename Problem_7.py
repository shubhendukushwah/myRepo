x=int(input("Enter 1st digit: "))
y=int(input("Enter 2nd digit: "))
arr=[]
for l in range(x):
    ls=[]
    for m in range(y):
        ls.append(l*m)
    arr.append(ls)

print(arr)
