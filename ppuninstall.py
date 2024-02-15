import random

while True:
    pp = 150
    balls = 2
    no = 0
    average = 0
    print(f"You have {balls} balls and a {pp}cm long banana.")
    print("1) Cut off a part of your banana")
    print("2) Quit the game")
    while pp != 0:
        home = input("What would you like to do? Input the number.")
        print(f"Banana length: {pp}cm")
        print(f"Balls: {balls}")
        if home == "1":
            cut = input("Press enter to lock your decision.")
            cut = random.randint(0, pp)
            print(f"{cut}cm of your banana is cut off.")
            pp -= cut
            print(f"You now have {pp}cm left.")
            no += 1
            if pp == 0:
                average = 150 / no
                print(f"Average pp length cut off: {average}cm.")
        elif home == "2":
            print("You tried to leave the room but your fingers accidentally pushed the scissors off the table. It sliced through your entire banana.")
            print(f"Average pp length cut off: {150 / (no+1)}cm")
            print(f"Tries survived: {no + 1}")
            pp = 0
