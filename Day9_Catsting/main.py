Year=int(input("Enter your year of birth: "))
#if Year>=1883 and Year<=1900:
if 1883<=Year<=1900:
  print("Lost Geneartion")
elif 1901<=Year<=1927:
  print("Greatest Geneartion")
elif 1928<=Year<=1945:
  print("Silent Geneartion")
elif 1946<=Year<=1964:
  print("Baby Boomers")
elif 1965<=Year<=1980:
  print("Generation X")
elif 1981<=Year<=1996:
  print("Millenial")
elif 1997<=Year<=2012:
  print("Generation Z")
elif 2012<=Year<=2024:
  print("Generation Alpha")
