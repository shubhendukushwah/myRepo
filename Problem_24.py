def sqr(first_value,last_value):
    """sqr Function squares the values provided to it.
    It accept two arguments first in the initial value and second in the last value"""
    f=first_value
    l=last_value
    for x in range(f,l+1):
        yield x*x

print(end='\n \n')
print('Documentaion of abs function \n',abs.__doc__)
print(end='\n \n')
print('Documentaion of range function \n',range.__doc__)
print(end='\n \n')
print('Documentaion of print function \n',print.__doc__)
print(end='\n \n')
print('Documentaion of int \n',int.__doc__)
print(end='\n \n')
print('Documentaion of sqr function \n',sqr.__doc__)
