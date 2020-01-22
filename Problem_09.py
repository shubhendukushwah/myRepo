ls=[]

while True:
    str1=input()

    if str1:
        ls.append(str1.upper())
    else:
        break

for x in ls:
    print(x)
