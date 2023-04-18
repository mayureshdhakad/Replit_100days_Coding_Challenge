number= int(input("Enter your multiples: "))
print()

counter = 0
for i in range (1,11):
  right_answer = i*number
  print(number,"x",i)
  answer = int(input(">"))

  if answer == right_answer:
    print("Your answer is right")
    counter+=1
  else:
    print("It is not correct answer")
if counter ==10:
  print("All answers are right")

else:
  print("Your score is ",counter )