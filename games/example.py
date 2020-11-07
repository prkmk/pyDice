from components.dice import *

def example():
  while (True):
    print("Montako noppaa?")
    print("L - lopeta")
    inp = input("> ")
    if inp == "l" or inp == "L":
      return
    elif inp.isdigit:
      dices = []
      for i in range(int(inp)):
        dices.append(Dice())
      
      while (True):
        print()
        inp = "0"
        sum = 0
        for dice in dices:
          dice.shuffle()
          sum += dice.getValue()
          print(dice.getFace(), end=" ")
        print("\nTulos: " + str(sum))

        while (inp != "H" and inp != "L"):
          print("H - heitä")
          print("L - lopeta")
          inp = input("> ").upper()
          
        if inp == "L":
          return