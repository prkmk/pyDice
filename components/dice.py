import random

faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

class Dice:
  def __init__(self, printFace = True):
    self.value = 1
    self.face = faces[self.value - 1]
    self.printFace = printFace

  def shuffle(self):
    self.value = random.randint(1, 6)
    self.face = faces[self.value - 1]
    return self

  def setValue(self, value):
    if 1 <= value <= 6:
      self.value = value
      self.face = faces[self.value - 1]
    return self

  def getValue(self):
    return self.value
  
  def getFace(self):
    return self.face if self.printFace else str(self.value)
