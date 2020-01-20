ls=[1,2,3,4,5,6,7,8,9,10]

fil_map=list(map(lambda x: x*x,list(filter(lambda x: x%2==0,ls))))

print(fil_map)