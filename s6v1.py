sum_of_squares = 0
sum_of_terms = 0

for p in range(1,101):
  sum_of_squares += p*p
  sum_of_terms += p 
print(sum_of_terms**2 - sum_of_squares) 
