heads = int(input("Enter number of heads "))
legs  =  int(input("Enter number of legs "))

hens = 0
rabbit = 0

rabbit = int((legs - (2*heads))/2)
hens   = int(heads - rabbit)

print("Rabbits ",rabbit)
print("hens    ", hens)