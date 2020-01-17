def gen():
    lis= [num**2 for num in range(1,21)]
    return lis[len(lis)-5:]
print(gen())