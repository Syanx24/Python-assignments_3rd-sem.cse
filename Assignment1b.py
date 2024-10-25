# Write a Python program to take radius of a circle from the user. Calculate the area and perimeter of the circle and show the values up to 3 decimal points.
# E.g. Area = xx.xxx and Perimeter = yy.yyy

x=eval(input("Enter circle radius here: "))
area=3.14*(x*x)
perimeter=2*3.14*x
print(f"Area is: {area:0.3f}")   #use 0.2f if want to show upto 2 decimal
print(f"Perimeter is: {perimeter:0.3f}")     #use 0.2f if want to show upto 2 decimal