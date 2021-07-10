# Find the sum of all the multiples of 3 or 5 below 1000.


# Natural numbers: 1,2,3,4......
# Range given: [1, 1000)

multiple_3 = set()
multiple_5 = set()

for _ in range(1,1000):
  if 0 == _%3:
    multiple_3.add(_)
  if 0 == _%5:
    multiple_5.add(_)

result = multiple_3.union(multiple_5)
print(sum(result))
