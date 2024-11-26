def generate_fibonacci_upto(n):
    fibonacci_number = []
    a , b = 0 , 1
    while a <= n:
        fibonacci_number.append(a)
        a,b= b , a+b
    return fibonacci_number

def write_fibonacci_to_file(filename,fibonacci_numbers):
    with open(filename, "w") as file:
        for num in fibonacci_numbers:
            file.write(str(num) + "\n")

n= int(input("Enter the upper limit (n) for Fibbonacci numbers: "))

filename="fibonacci_number.txt"
fibonacci_numbers = generate_fibonacci_upto(n)
write_fibonacci_to_file(filename,fibonacci_numbers)

print(f"Fibonacci number up to {n} have been written to {filename}")