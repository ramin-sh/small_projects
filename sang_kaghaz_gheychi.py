import random

player = input("یکی رو انتخاب کن:(سنک,کاغذ,قیچی):")

possible_actions = ["سنگ","کاغذ","قیچی"]

computer = random.choice(possible_actions)
print(f"\n تو {player} انتخاب کردی و کامپیوتر  {computer}  انتخاب کرد.\n")

if player == computer :
    print("مساوی شدی")
else:
    if player == "سنگ":
        if computer == "قیچی":
            print("بردی")
        else:
            print("کامپیوتر برد")
    else:
        if player == "کاغذ":
            if computer ==  "قیچی":
                print("کامپیوتر برد")

            else:
                print("بردی")
        if player == "قیچی":
            if computer == "کاغذ":
                print("بردی")
            else:
                print("کامپیوتر برد")