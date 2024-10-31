# write a python program to generate pattern
#              A
#            B A
#          C B A
#        D C B A
#      E D C B A

for i in range(65, 70):
    # Print leading spaces
    for j in range(70 - i):
        print(" ", end=" ")
    # Print characters in reverse order from the current character to 'A'
    for k in range(i, 64, -1):
        print(chr(k), end=" ")

    print() 