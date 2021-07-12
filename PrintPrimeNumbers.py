count = 0
num = 100

# iterating through the range till where we need to print numbers
for i in range(1,num):
  
  # checking the number if it is divisible by 1 & itself only; to qualify to be a prime no.
  for j in range(1,i+1):
    if i%j == 0 :
      count += 1
  
    # if it is divisible by more than 2 numbers, no need to check further; it won't be a prime 
    if count > 2:
      count = 0
      break
  
  if 2 == count:
    print(i,end=', ')
  count = 0

