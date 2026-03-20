player_1 = int(input("player_1, Enter Your Secrute Number: "))
player_2 = int(input("player_2, Enter Your Secrute Number: "))

print("Game Start!")

while True:

    p1_guess = int(input("Guess Player 2's number: "))

    if p1_guess == player_2:
        print("player 1 Win!")
        break

    elif p1_guess < player_2:
        print("Higher")

    else:
        print("Lower")

#-----------------------------------------------------------------------------------------

    p2_guess = int(input("Guess Player 1's number: "))

    if p2_guess == player_1:
        print("player Win!")
        break

    elif p2_guess < player_1:
        print("Higher")

    else:
        print("Lower")