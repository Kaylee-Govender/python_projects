import random
comp_ans = ["r", "p", "s"]
comp_score = 0
user_score = 0

game_over = False

while game_over != True:

    round = int(input("Enter number of rounds: "))

    for x in range(round):
        user_ans = input("Enter rock(r), paper(p) or scissors(s): ").lower()
        comp_choice = random.choice(comp_ans)
        print("Computer's turn: ", comp_choice)
        if user_ans == "s" and comp_choice == "r":
            comp_score += 1
        elif user_ans == "s" and comp_choice == "p":
            user_score += 1
        elif user_ans == "p" and comp_choice == "r":
            user_score += 1
        elif user_ans == "p" and comp_choice == "s":
            comp_score += 1
        elif user_ans == "r" and comp_choice == "s":
            user_score += 1
        elif user_ans == "r" and comp_choice == "p":
            comp_score += 1

    if user_score > comp_score:
        print("Congratulations you won!")
    elif user_score < comp_score:
        print("You lost!")
    else:
        print("It's a draw!")

    print("Your score:" ,user_score , "Computer's score:" ,comp_score)

    contin = input("Continue Playing? (y/n)")
    if(contin == "n"):
        game_over = True
