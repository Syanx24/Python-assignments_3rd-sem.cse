# Write a python program which will take a single character from the user and check if the character is a vowel or consonant. If the input is neither a vowel nor consonant, then the code will show it is invalid input.

char=input("Enter any character: ")
match char:
    case ('A'|'a') | ('E'|'e') | ('I'|'i') | ('O'|'o') | ('U'|'U'):
        print(f"This '{char}' is a vowel")
    case _ if char.isalpha() and len(char)==1:
        print(f"This '{char}' is consonant")
    case _: print("This input is Invalid")