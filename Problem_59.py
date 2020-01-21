class Person():
    def getGender(self):
        print("In ")

class Male(Person):
    def getGender(self):
        print("Male")

class Female(Person):
    def getGender(self):
        print("Female")


objMale = Male()
objFemale = Female()

objMale.getGender()
objFemale.getGender()

