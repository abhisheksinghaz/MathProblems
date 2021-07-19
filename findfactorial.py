# find factorial recursively

def fact(num):
  if num is 1:
    return 1
  else:
    return num * fact(num - 1)
  
if __name__ == "__main__":
  num = int(input("Enter the number: "))
  print(fact(num))
