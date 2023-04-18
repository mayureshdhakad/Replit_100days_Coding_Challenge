from getpass import getpass as input

print("EPIC GAME OF ROCK ,PAPER AND SCISSOR")
print("Select your move from R,P,S  "\
     "Rock= R, Paper= P, Scissor = S")

player1_score = 0
player2_score = 0
while True:
 player1move = input("Player 1 >")
 print()
 player2move = input('Player 2 >')
 print()
 if player1move == "R":
        if player2move == "R":
            print("You both picked Rock, Match Draw!")
        elif player2move == "P":
            print("Player 1 Rock is wrapped by the Player 2 Paper")
            player2_score +=1
        elif player2move == "S":
            print("Player 2 Scissor is smashed by the Player 1 Rock")
            player1_score +=1
        else:
            print("Invalid move by player 2")
            
 elif player1move == "P":
        if player2move == "R":
            print("Player 2 Rock is wrapped by the Player 1 Paper")
            player1_score +=1
        elif player2move == "P":
            print("You both picked Paper, Match Draw")
        elif player2move == "S":
            print("Player 2 Scissor cut the Player 1 Paper")
            player2_score +=1
        else:
            print("Invalid move by player 2")
        
 elif player1move == "S":
        if player2move == "R":
            print("Player 1 Scissor is smashed by the Player 2 Rock")
            player2_score +=1
        elif player2move == "P":
            print("Player 1 Scissor cut the Player 2 Paper")
            player1_score +=1
        elif player2move == "S":
            print("You both picked Scissor, Match Draw!")
        else:
            print("Invalid move by player 2")
        
 else:
        print("Invalid move by player 1")
 print()
 print("Player 1 has",player1_score,"wins")
 print("Player 2 has",player2_score,"wins")

 if player1_score == 3 :
  print("Player 1 won the game")
  print("Thanks for playing!!")
  break
  print()
 elif player2_score ==3:
  print("Player 2 won the game")
  print("Thanks for playing!!")
  break
  


  
