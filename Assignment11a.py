file_name="welcome.txt"
with open(file_name,"w") as file:
    file.write("Welcome to Python Programming")
print(f'Text "Welcome to python" has been written to {file_name}')