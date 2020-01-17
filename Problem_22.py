st=input()
st=st.split()
st.sort()
ans=[]
count2=0
for x in range(len(st)):
    count=1
    if st[x]==None:
            continue
    for y in range(x+1,len(st)-1):
        
        if st[x]==st[y]:
            st[y]=None
            count+=1
    print(st[x],':',count,sep='')

