import os

def get_file_size(filename):
    try:
        size = os.path.getsize(filename)
        print(f"The size of {filename} is {size} bytes")

    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"An error occurred: {e}")


filename = input("Enter the name of the file: ")

get_file_size(filename)