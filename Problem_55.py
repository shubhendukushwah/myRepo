num=int(input())


def gen(num):
    for y in range(0,num,2):
        yield y

for x in gen(num):
    print(x,end=',')


