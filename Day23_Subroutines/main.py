print("Replit Login System")

def loginsystem():
  while True:
    username = input("Enter username: ")
    password = input("Enter Passoword: ")
    
    if username == "mayuresh" and password == "job123":
      print("Welcome", username)
      break
    else:
      print("There is something wrong with login details",
      "Please check and try again")
      continue
     
loginsystem( )