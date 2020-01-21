import math
ls=[]
for x in range(4):
    s=input()
    tup=tuple(s.split(' '))
    ls.append(tup)

def distance(ls):
    x=0
    y=0
    for z in ls:
        if z[0] == 'UP':
            x+=int(z[1])
        elif z[0] == 'DOWN':
            x-=int(z[1])

        elif z[0] == 'LEFT':
            y+=int(z[1])
        
        elif z[0] == 'RIGHT':
            y-=int(z[1])

    ans=math.sqrt((x**2)-(y**2))
    return round(ans)

print(distance(ls))


