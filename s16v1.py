import math

num1 = int(math.pow(2,1000))

out = 0
while num1 > 0:
  rem = num1%10
  out += rem
  num1 = num1//10
print(out)
