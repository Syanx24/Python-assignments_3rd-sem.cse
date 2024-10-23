# Take two statements from user as input and show

# a.  Unique and common words
# b.  All common words
# c.  All unique words present in 1st statement but not in second


input1=input("Enter 1st string: ")
input2=input("Enter 2nd string: ")

input1s=set(input1.split())
input2s=set(input2.split())

st1=input1s.union(input2s)
st2=input1s.intersection(input2s)
st3=input1s.difference(input2s)

print(st1)
print(st2)
print(st3)
