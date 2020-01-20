class Shape():
    def area(self,l):
        return 0


class Square(Shape):
    def __init__(self,l):
        self.length=l
    
    def area(self):
        return self.length*self.length

obj = Square(22)

print(obj.area())

