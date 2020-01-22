class A:
    string='This is class parameter'

    def __init__(self,var):
        string="This is Instance Parameter,"
        print(string,var)

print(A.string)

obj1 = A("This is obj 1")

obj2 = A("This is obj 2")

obj3 = A("This is obj 3")

