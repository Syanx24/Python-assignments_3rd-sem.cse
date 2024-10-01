#split from a string
print("Enter your roll numner with college name in the following format 11603219005@mckvie.edu.in,then find roll number and collge name in separate")
string=input("Enter input in the following format: ")
list1=string.split('@')

# print(list1) [initial checking]

list2=list1[1].split(".")

# print(list2) [checking]

print(f"Your roll number is {list1[0]} and your college name is {list2[0].upper()}")