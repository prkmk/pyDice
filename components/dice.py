import random

faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

class Dice:
  def __init__(self):
    self.value = 1
    self.face = faces[self.value - 1]

  def shuffle(self):
    self.value = random.randint(1, 6)
    self.face = faces[self.value - 1]
    return self

  def getValue(self):
    return self.value
  
  def getFace(self):
    return self.face
