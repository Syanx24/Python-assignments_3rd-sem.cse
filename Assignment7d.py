# Use the concept of lambda function list all the Leap years in the range 2024 to 3010

leapyear=list(filter(lambda x: (x%400)==0 or (x%100!=0 and x%4==0),range(2024,3010)))
print(f"All leapyears between 2024 to 3010 are: {leapyear}")