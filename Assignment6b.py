#Given a list L write a program to make a new list and match the numbers inside list L to its respective index in the new list. Put 0 at remaining indexes. Also print the elements of the new list in the single line.
val=input("Enter the numbers: ").split()
valint=[int(v) for v in val]
zerolist=[0]*(max(valint)+1)

for num in valint:
    zerolist[num]=num
print(zerolist)