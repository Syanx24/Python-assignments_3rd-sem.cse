#Create a class B. Define the constructor with one argument (integer type) which will show “Class B object created”. Define a method show (), which will show “Showing Class B object having value val1”


class B:
    def __init__(self,val1:int):
        self.val1 = val1
        print("Class B object created")
    def show(self):
        print(f"Showing class B object having value {self.val1}")

l=B(10)
l.show()