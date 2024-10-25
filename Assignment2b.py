# Consider the basic pay of an employee is given by the user. AGP is 50% of the basic pay. The company provides 50% DA and 15% HRA on the merged basic. Write a python program to calculate and display total salary of the employee.

bs=eval(input("Enter your basic salary: "))

agp=0.5*bs
print(f"Your total agp is {agp:0.2f}")

ms=bs+agp
print(f"Your total ms is {ms:0.2f}")

da=0.5*ms
print(f"Your total da is {da:0.2f}")

hra=0.15*ms
print(f"Your total hra is {hra:0.2f}")

total=ms+da+hra
print(f"Your total salary is {total:0.2f}")