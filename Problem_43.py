tu=(1,2,3,4,5,6,7,8,9,10)

def gen(tu):
    return tuple(x for x in tu if x%2==0)

print(gen(tu))