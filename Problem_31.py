def maxlen(str1,str2):
    if len(str1) > len(str2):
        print(str1)
    
    elif len(str2) > len(str1):
        print(str2)
    
    else:
        print(str1,'\n',str2,sep='')


maxlen('Hello','World')