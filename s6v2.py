# 1 + 2 + 3 + 4 + ........... + 100 = 100*(100+1)/2 using the formula ( n*(n+1) )/2
# 1^2 + 2^2 + 3^2 + .......+ 100^2 = ( 100 * (100 + 1) * (2*100 + 1) )/6 using the formula (( n*(n+1) )/2) * ( (2 * n + 1)/3 )
n = 100 # given
sum_of_terms = int( (( n*(n+1) )/2)**2 )
sum_of_squares = int( ( n*(n+1) * (2*n + 1) )/6 )

print(sum_of_terms - sum_of_squares)
