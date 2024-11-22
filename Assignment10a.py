#Create a class A. Define the constructor which will show “Class A object created”. Define a method show (), which will show “Showing Class A”. Define a destructor which will delete the object and show “Object deleted!!!”


class A:
    def __init__(self):
        print("Class a object created")
    def show(self):
        print("Showing class A")
    def _del_(self):
        print("Object deleted!!!")


a=A()
a.show()
del a