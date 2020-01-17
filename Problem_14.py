sent=input()
u=0
l=0
for x in sent:
    if ord(x) in range(65,91): 
        u+=1
    if ord(x) in range(97,123):
        l+=1
print("UPPER CASE ",u)
print("LOWER CASE ",l)