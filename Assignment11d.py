def read_and_display_file(filename):
    try:
        with open(filename, "r") as file:
            lines=file.readliness()
            print("Contents of this file: ")
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print(f"The file {filename} does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")

filename =input("Enter the name of the file you want to read: ")

read_and_display_file(filename)