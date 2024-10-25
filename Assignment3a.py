# Write a python program to find the greatest among three numbers.

a=eval(input("Input value for 'a': "))
b=eval(input("Input value for 'b': "))
c=eval(input("Input value for 'c': "))

maxval=a if (a>b and a>c) else (b if b>c else c)

print(f"The max value is {maxval}")