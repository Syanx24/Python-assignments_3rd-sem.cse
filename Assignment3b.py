# Write a python program to check whether a year is Leap Year.

year=int(input("Enter a year: "))
if (year<1000 or year>9999):
    print("Invalid Input")
else:
    if((year%400==0) or ((year%100!=0) and (year%4==0))):
        print(f"The year {year} is leap year")
    else:
        print(f"{year} is not leap year")