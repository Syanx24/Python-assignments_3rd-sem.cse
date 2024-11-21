# #Import numpy module in your source code. Create m X n matrix (A) integer by taking user inputs. Also, create a n X m matrix (B) with random numbers between 1 to 20. Generate a C matrix where C = A X B. Show the C matrix.

import numpy
import random

a = []
b = []

m = int(input("Row= "))
n = int(input("Col= "))

for i in range(m):
    tem = []
    for j in range(n):
        tem.append(int(input()))
    a.append(tem)

for i in range(n):
    tem = []
    for j in range(m):
        tem.append(random.randint(1, 20))
    b.append(tem)

print(numpy.dot(a, b))

