ls=[]
for x in range(1,21):
    ls.append(x)

fil_list=list(filter(lambda y:y%2==0 ,ls))


print(fil_list)