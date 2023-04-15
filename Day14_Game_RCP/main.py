from getpass import getpass as input

print("EPIC GAME OF ROCK ,PAPER AND SCISSOR")
print("Select your move from R,P,S  "\
     "Rock= R, Paper= P, Scissor = S")

player1move = input("Player 1 >")
print()
player2move = input('Player 2 >')
print()

if player1move == "R":
    if player2move == "R":
        print("You both picked Rock, Match Draw!")
    elif player2move == "P":
        print("Player 1 Rock is wrapped by the Player 2 Paper")
    elif player2move == "S":
        print("Player 2 Scissor is smashed by the Player 1 Rock")
    else:
        print("Invalid move by player 2")

elif player1move == "P":
    if player2move == "R":
        print("Player 2 Rock is wrapped by the Player 1 Paper")
    elif player2move == "P":
        print("You both picked Paper, Match Draw")
    elif player2move == "S":
        print("Player 2 Scissor cut the Player 1 Paper")
    else:
        print("Invalid move by player 2")

elif player1move == "S":
    if player2move == "R":
        print("Player 1 Scissor is smashed by the Player 2 Rock")
    elif player2move == "P":
        print("Player 1 Scissor cut the Player 2 Paper")
    elif player2move == "S":
        print("You both picked Paper, Match Draw!")
    else:
        print("Invalid move by player 2")

else:
    print("Invalid move by player 1")
