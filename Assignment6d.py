#Take a string as input.
# Form a dictionary which will have each unique word present in the string as key and frequency of the word as value.

s=input("Enter a string: ")
print(s)
s1=set(s.split())
d=dict()
for i in s1:
    d[i]=s.count(i)
print(d)
