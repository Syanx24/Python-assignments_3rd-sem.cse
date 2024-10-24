#Given a list of strings, write a program to write sort the list of strings based on last character of each string.

def get_position(sub):
    return sub[-1]
list=['ram', 'shyam', 'lakshami']
print(f"The original list is: "+str(list))

list.sort(key=get_position)
print("Sorted list:"+str(list))