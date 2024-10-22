#Given a list of numbers (integers), find second maximum and second minimum in this list.

val=input("Enter the numbers here: ").split()
valint=[int(v) for v in val]
#print(valint)
sortedval=sorted(valint)
print(sortedval)

print(f"2nd lowest element is the list is {sortedval[1]}")
print(f"2nd highest element is the list is {sortedval[-2]}")