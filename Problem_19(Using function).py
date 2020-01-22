li=[]
for x in range(5):
    st=input()
    tu=tuple(st.split(','))
    li.append(tu)

li = sorted(li , key=lambda tup:tup[2])
li = sorted(li , key=lambda tup:tup[1])
li = sorted(li , key=lambda tup:tup[0])

print(li)