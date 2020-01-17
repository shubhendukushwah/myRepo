binary=input()
binary=binary.split(',')
for x in binary:
    temp=x
    x=int(x,2)
    if x % 5 == 0:
        print(temp)

