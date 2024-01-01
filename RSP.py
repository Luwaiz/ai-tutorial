print("""lets play a game
rock, paper, scissors

""")

count=0
counter=int(input("How many rounds do u wants to play "))
while count<counter:
    count+=1
    print(f"round {count}")
    player1=input("player 1: ")
    player2=input("player 2: ")
    if player1.lower()=='scissors' and player2.lower()=="paper":
        print("Player 1 has won this round")
    elif player1.lower()=='scissors' and player2.lower()=="rock":
        print("Player 2 has won this round")
    elif player1.lower()=='paper' and player2.lower()=="rock":
        print("Player 1 has won this round")
    elif player1.lower()=='paper' and player2.lower()=="scissors":
        print("Player 2 has won this round")
    elif player1.lower()=='rock' and player2.lower()=="scissors":
        print("Player 1 has won this round")
    elif player1.lower()=='rock' and player2.lower()=="paper":
        print("Player 2 has won this round")
    elif player1.lower()=='Scissors' and player2.lower()=="scissors":
        print("Its a tie")
    elif player1.lower()=='rock' and player2.lower()=="rock":
        print("Its a tie")
    elif player1.lower()=='paper' and player2.lower()=="paper":
        print("Its a tie")
    else:
        print("I dont understand")
   