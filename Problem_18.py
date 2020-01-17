password=input()
sym=['$','#','@']
ls=password.split(',')
for pwd in ls:
    f=0
    a=0
    n=0
    s=0
    if len(pwd) in range(6,13):
        for c in pwd:
            if c.isalpha():
                a=1
                continue
            elif c in sym :
                s=1
                continue
            elif c.isnumeric():
                n=1
                continue
            else:
                f=1
    if  a==1 and s==1 and n==1 and f==0:
        print(pwd)


