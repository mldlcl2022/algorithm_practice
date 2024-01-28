n = int(input())

import math
num = math.factorial(n)

z = 0
for i in range(len(list(str(num)))) :
    if list(str(num))[-(i+1)] != '0' :
        break
    if list(str(num))[-(i+1)] == '0' :
        z += 1
print(z)