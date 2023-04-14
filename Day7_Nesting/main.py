movie = input("Which movie do you like most: Sarfarosh or Namaste London? ")
if movie == "Sarfarosh":
    print("It is a great movie")
    topic = input("Its based on which topic?")
    if topic =="Country":
     print("You got it")
    else:
     print("You are wrong")
     actor = input("Who is the Actor?")
     if actor == "Amir Khan":
      print("You are right.")
     else:
       print("You are fake fan of movie")

elif movie == "Namaste London":
    print("It is a fantastic movie")
    topic = input("Its based on which topic?")
    if topic =="Love":
     print("You got it")
    else:
     print("You are wrong")
     actor = input("Who is the Actor?")
     if actor == "Akshay Kumar":
      print("You are right.")
     else:
       print("You are fake fan of movie")
