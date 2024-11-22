#Create a class C inheriting class B. Define the constructor which will take two arguments (integer type) which will initialize a class B object with 1st argument and show “Class C object created”. Define a method show (), which will show “Showing Class C with val1, val2.”


class B:
    def __init__(self,val1:int):
        self.val1 = val1
        print("Class B object created")
    def show(self):
        print(f"Showing class B object having value {self.val1}")

l=B(10)
l.show()



class C(B):
    def __init__(self,val1:int,val2:int):
        super().__init__(val1)
        self.val2=val2
        print("Class C object created")

    def show(self):
        print(f"Showing class C with {self.val1},{self.val2}")


c=C(10,20)
c.show()