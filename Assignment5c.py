#program to calculate uppercase & lowercase number in a string

print("Program to calculate uppercase & lowercase number in a string")
string1=input("Enter any sentence here: ")

uc=lc=0 #uppercase and lowercase taking initially ZERO

for i in string1:
    if(i.isupper()):
        uc+=1
    if(i.islower()):
        lc+=1

print(f"Total number of uppercase letter is {uc}")
print(f"Total number of lowercase letter is {lc}")