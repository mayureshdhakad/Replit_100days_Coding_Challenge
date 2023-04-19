import random
print("Infiity Dice")
Playgame ="yes"
sides = int(input("How many sides?"))
def dice(sides):
  print("Roll Now",random.randint(1,sides))
while Playgame == "yes":
  dice(sides)
  Playgame = input("Roll again: ")
    

  