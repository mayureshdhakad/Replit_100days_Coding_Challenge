print("Fill in the blank lyrics")
counter =1
while True:
  word = input("Enter a word: ")
  if word == "give":
    print("Never going to",word,"you up")
    #print("Well Done! It only took you 3 attempts")
    break
  else:
    print("Nope, try again")
    counter +=1
print("Well Done! It only took you",counter,"attempts")
    
    
