# First two terms of the Faboncii series: 1 & 2 
# last term should be less than 4,000,000
# find the sum of the even numbers in this series

class Faboncii_series:
  def __init__(self):#, self.t1 = 1, self.t2 = 2):
    self.t1 = 1
    self.t2 = 2
    self.next_num = self.t1 +self.t2
    self.output_sum = 2

  def create_faboncii(self):
    while True:
      self.t1 = self.t2 # 2
      self.t2 = self.next_num # 3
      if self.next_num > 4000000:
        break
      else:
        self.next_num = self.t1 + self.t2
      if 0 == self.next_num%2:
        self.output_sum += self.next_num
   
if __name__ == "__main__":
  obj = Faboncii_series()
  obj.create_faboncii()
  print(obj.output_sum)
