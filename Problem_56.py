num=int(input())


def gen(num):
    for x in range(0,num):
        if x % 5 ==0 and x % 7 ==0:
            yield x 


for y in gen(num):
    print(y,end=',')