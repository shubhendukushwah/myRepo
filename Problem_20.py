class Gen():

    def get(self):
        return int(input())


    def genrate(self):
        n=self.get()
        for x in range(0,n+1):
            if x % 7==0:
                yield x


obj = Gen()

obj
for x in obj.genrate():
    print(x,end=' ')

