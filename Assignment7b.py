#  Write a recursive function fibo_s(), which will take an integer as input(n) and show the Fibonacci Series up to n-terms. Make sure that the default value of n is 1

def fibo_s(a,b,n):
    if (n>0):
        print(a, end=' ')
        fibo_s(b,a+b,n-1)

n=int(input("Enter the number of terms: "))
print(f"The first {n} terms of the fibbonacci series are: ",end=' ')
fibo_s(0,1,n)