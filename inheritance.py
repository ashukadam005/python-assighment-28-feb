class Product:

    def __init__(self):
        self.id= 78
        self.name= "Amul"

    def display(self):
        print("id:",self.id)
        print("Name:",self.name)


class A(Product):

    def __init__(self):
        super().__init__()
        self.count = 50
        self.category="butter"

    def display(self):
        super().display()
        print("count:",self.count)
        print("category",self.category)


class B(Product):

    def __init__(self):
        super().__init__()
        self.count = 90
        self.category = "Milk"

    def display(self):
        super().display()
        print("count:", self.count)
        print("category:",self.category)


class C(Product):
    def __init__(self):
        super().__init__() 
        self.count=56
        self.category="choco"

    def display(self):
        super().display()   
        print("Count",self.count)
        print("category",self.category)


print("-------------------------")

obj1 = A()
obj1.display()

print("-------------------------")


obj2 = B()
obj2.display()
print("-------------------------")

obj3 = C()
obj3.display()

print("-------------------------")
