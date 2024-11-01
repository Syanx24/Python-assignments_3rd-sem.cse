# Write a recursive function fibo_n(), which will take an integer as input(n) and returns the n-th term of Fibonacci Series. Make sure that the default value of n is 1

def fibo_n(n):
    if n==1:
        return 0
    if n==2:
        return 1
    if n>2:
        return fibo_n(n-1)+fibo_n(n-2)
    

n=int(input("Enter the num of term: "))
print(f"The {n}th term of fibbonacci series is: {fibo_n(n)}")