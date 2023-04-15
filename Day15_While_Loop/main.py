exit="no"

while exit =="no":
  animal_sound = input("Which animal sound do you want to hear? ")
  if animal_sound == "cow" or animal_sound =="Cow":
    print("Moo")
  elif animal_sound == "Lemur" or animal_sound == "lemur":
    print("awooga")
  else:
    print("I am not aware about that animal")
  exit = input("Do you want to exit?: ")

