# write a python program to print all two digit automorphic numbers.
# automorphic number is a number whose square ends with the number itself. (25)**2=625

for i in range (10,100):
    if (((i**(2))%100)==i):
        print(f"{i} is an automorphic number")