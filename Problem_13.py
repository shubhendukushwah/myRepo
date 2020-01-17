string=input()
alpha=0
numeric=0
for s in string:
    if ord(s) in range(65,91) or ord(s) in range(97,123):
        alpha+=1
    if ord(s) in range(48,58):
        numeric+=1

print('LETTERS ',alpha)
print('DIGITS ',numeric)
