#seconds_year= 60*60*24*365
#print(seconds_year)

year = input("For which year do you want to calculate : Leap_year or Non_Leap_year ")
if year ==  "Leap_year":
  days=366
  seconds_year = 60*60*24*days
  print("There are",seconds_year,"in a one Leap Year")
elif year ==  "Non_Leap_year":
  days=365
  seconds_year = 60*60*24*days
  print("There are",seconds_year,"in a one Non_Leap Year")
  
  
