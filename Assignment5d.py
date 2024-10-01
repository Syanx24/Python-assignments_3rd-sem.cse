#Program to extract the sub-string between the specified positions(user given) also check it's palindrom or not
string1=input("Enter a string here: ")
pos=input("Enter position to slice: ")
index=pos.split(" ")
sliced=string1[int(index[0])-1:int(index[1])]
# print(sliced)

if sliced==sliced[::-1]:
    print(f"{sliced} is palindrome")
else:
    print(f"{sliced} is not palindrome")