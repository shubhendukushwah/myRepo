ls=input()
ls=ls.split(',')
ans = [x for x in ls if int(x) % 2 != 0]
for a in ans:
    if a != ans[len(ans)-1]:
        print(a,end=',')
    else:
        print(a)
 