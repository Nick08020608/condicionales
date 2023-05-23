#Write a Python program that accepts the two-player option in

Player_one= input("Selection Paper(P), Stone(S), Scissors(T)")
Player_two= input("Selection Paper(P), Stone(S), Scissors(T)")

if Player_one.upper()=="P" and Player_two.upper()=="S":
    print("The win is the player one for the paper covers the stone.")
elif Player_one.upper()=="P" and Player_two.upper()=="T":
    print("Player two wins because scissors cuts paper.")
elif Player_one.upper()=="S" and Player_two.upper()=="P":
    print("The win is the player two for the paper covers the stone.")
elif Player_one.upper()=="S" and Player_two.upper()=="T":
    print("The win is the player for the stone damage scissors.")
elif Player_one.upper()=="T" and Player_two.upper()=="P":
    print("The win is the player two for the paper covers the stone.")
elif Player_one.upper()=="T" and Player_two.upper()=="S":
    print("The win is the player two for the stone damage scissors.")
else:
    print("The player one and the player two are tied.")