# First two terms of the Faboncii series: 1 & 2 
# last term should be less than 4,000,000
# find the sum of the even numbers in this series

class Faboncii_series:

  def __init__(self):
    self.t1 = 1
    self.t2 = 2
    self.next_num = self.t1 +self.t2
    self.output_sum = 2
    return self.create_faboncii()

  # checking if the number is less than 4000000 i.e., it is in range
  def check_range(self):
    if self.next_num > 4000000:
      return False
    else:
      return True
  
  # checking if the no. is even then adding it
  def calculate_sum(self):
    if 0 == self.next_num%2:
      self.output_sum += self.next_num

  def create_faboncii(self):
    while True:
      self.t1 = self.t2 # 2
      self.t2 = self.next_num # 3

      if self.check_range():
        self.next_num = self.t1 + self.t2
        self.calculate_sum()
      else:
        break

   
if __name__ == "__main__":
  obj = Faboncii_series()
  print(obj.output_sum)
