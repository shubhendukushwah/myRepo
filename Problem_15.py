num=input()
ex='a+aa+aaa+aaaa'
sum=0
ex=ex.replace('a',num)
ex=ex.split('+')
for x in ex:
    sum+=int(x)
print(sum)
