# write a python program to generate fibonacci series upto n terms, using loop

print("Program for Fibonacci Series ")
n=int(input("Enter for upto which term you want to print: "))
a,b=0,1

if(n<=0):
    print("Enter term greater than 0")
else:
    print(a,end=' ')
    print(b,end=' ')
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c,end=' ')