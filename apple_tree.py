from apple import Apple
from random import randint
class AppleTree:
  def __init__(self):
      self.age = 0
      self.height = 0
      self.apples = []
  
  def age_tree(self):
      self.age += 1
      self.height += 1.5
      if self.age >= 10:
            self.apples.clear()
            for i in range(randint(80,120)):
                self.apples.append(Apple())
   
  def is_dead(self):
        return self.age >= 100
              
    
  def any_apples(self):
        return len(self.apples) > 0

  def pick_an_apple(self):
      if self.any_apples():
        return self.apples.pop()
      raise Exception('No apples on your tree')
      # Read the tests before coding.
