class dog():
    def __init__(self,name,age,coatcolor):
        self.name=name
        self.age=age
        self.coatcolor=coatcolor
    def description(self):
        print("Name: ",self.name)
        print("Age : ",self.age)
    def get_info(self):
        print("coat color: ",self.coatcolor)
class JackRussellTerrier(dog):
    def speed(self):
        print("He runs really fast")
    def eyes(self):
        print("His eyes are black")
class Bulldog(dog):
    def speed(self):
        print("He likes to walk")
    def eyes(self):
        print("His eyes are blue")
obj1=JackRussellTerrier("mickey",4,"white")
obj1.description()
obj1.get_info()
obj1.speed()
obj1.eyes()

obj2=Bulldog("sky",4,"black")
obj2.description()
obj2.get_info()
obj2.speed()
obj2.eyes()