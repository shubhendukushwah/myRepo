li=[]
for x in range(5):
    st=input()
    tu=tuple(st.split(','))
    li.append(tu)
    
def sortByScore(li):
    for x in range(len(li)-1):
        for y in range(x,len(li)):
            if li[x][2] >= li[y][2]:
                li[x],li[y]=li[y],li[x]
                
    return sortByAge(li)

def sortByAge(sortByScore):
    for x in range(len(li)-1):
        for y in range(x,len(li)):
            if li[x][1] >= li[y][1]:
                li[x],li[y]=li[y],li[x]
                
    return sortByName(li)

def sortByName(sortByAge):
    for x in range(len(li)-1):
        for y in range(x,len(li)):
            if li[x][0] >= li[y][0]:
                li[x],li[y]=li[y],li[x]
    
    return li

print(sortByScore(li))

