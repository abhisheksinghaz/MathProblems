# First two terms of the Faboncii series: 1 & 2 
# last term should be less than 4,000,000
# find the sum of the even numbers in this series

term1 = 1
term2 = 2
output_sum = 2
next_number = term1+term2 # 3

while True:
  term1 = term2
  term2 = next_number
  next_number = term1+term2
  if next_number > 4000000:
    break
  if next_number%2 == 0:
    output_sum += next_number

print(output_sum)
