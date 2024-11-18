#Create module called ‘numberCheck’, with two functions called ‘is_prime()’ (return true if prime else false) and  ‘is_palindrome()’  (return true if palindrome else false). Import the following module in your source code. Take an integer input in your current source code and call the ‘numberCheck’ module’s functions to check the number is prime and/or Palindrome number or not.

import Assignment8a_numcheck

a = int(input("Enter A number: "))
print(Assignment8a_numcheck.is_prime(a), Assignment8a_numcheck.is_palindrome(str(a)))
