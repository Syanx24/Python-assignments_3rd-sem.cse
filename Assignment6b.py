val=input("Enter the numbers: ").split()
valint=[int(v) for v in val]
zerolist=[0]*(max(valint)+1)

for num in valint:
    zerolist[num]=num
print(zerolist)