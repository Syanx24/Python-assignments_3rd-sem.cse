# write a python program to generate all prime numbers within a range, where range is user input.

l=int(input("Enter the lower limit: "))
u=int(input("Enter the upper limit: "))
c=0
for i in range(l,u+1):
    if(i>1):
        for j in range  (2,i):
            if(i%j==0):
                break
            else:
                print(i)
                c=c+1
print("The total Numbers in this range:",c)