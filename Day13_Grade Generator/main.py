print("Exam Grade Calculator")
Exam_name = input("Name of the Exam: ")
max_marks= float(input("Enter Max.Possible Score: ")) 
marks_obtained = float(input("Enter Your marks: "))
Percentage = float((marks_obtained/max_marks)/100)
Score = round(Percentage,2)
if 90<=marks_obtained and marks_obtained<100:
  print("You got",marks_obtained,"% which is A+")
elif 80<=marks_obtained and marks_obtained<90:
  print("You got",marks_obtained,"% which is A-")
elif 70<=marks_obtained and marks_obtained<80:
  print("You got",marks_obtained,"% which is B")
elif 60<=marks_obtained and marks_obtained<70:
  print("You got",marks_obtained,"% which is C")
elif 50<=marks_obtained and marks_obtained<60:
  print("You got",marks_obtained,"% which is D")
elif 40<=marks_obtained and marks_obtained<50:
  print("You got",marks_obtained,"% which is U")
else:
  print("Bad Luck! You are failed. Try next time")