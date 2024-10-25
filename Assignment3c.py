# In general, an equation of the form  where a ≠ 0, is known as quadratic equation. Accept the values of a, b, and c from the user and write a python program to calculate the roots of the given quadratic equation.

print("General equation for Quadradic equation is a**2x+bx+c=0")

a=int(input("Enter value for 'a' (a1=0) : "))
b=int(input("Enter value for 'b' : "))
c=int(input("Enter value for 'c' : "))

print(f"Results for the equation {a}**2x+{b}x+c=0")

d=(b**2)-(4*a*c)

if(a==0):
    print("Invalid Input ('a' should be !=0)")
elif(d==0):
    print("Roots are real and equal")
    root1=(-b)/(2*a)
    print(f"Roots are {root1:0.4f} and {root1:0.4f}")
elif(d>0):
    print("Roots are real and distinct")
    root2=(-b+(d**0.5)/(2*a))
    root3=(-b-(d**0.5)/(2*a))
    print(f"Roots are {root2:0.4f} and {root3:0.4f}")
else:
    print("Roots are Imaginary")

