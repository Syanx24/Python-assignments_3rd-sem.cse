#Write a python program to swap two variables using and without using third variable (use concept of Tuple Unpacking)

a=eval(input("Input value for 'a': "))
b=eval(input("Input value for 'b': "))
print(f"Before swap value is a={a} and b={b}")

#Using third variable
# c=a
# a=b
# b=c

#Using tuple unpacking
a,b=b,a

print(f"After swap value is a={a} and b={b}")