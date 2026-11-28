while True :
    print("===== Number Guessing Game =====")
    difficulty = input("Choose difficulty: ").lower()

    if difficulty == "easy":
        max_number = 10
        attempt = 7

    elif difficulty == "medium":
        max_number = 20
        attempt = 5

    elif difficulty == "hard":
        max_number = 50
        attempt = 3

    else:
        print("Invalid difficulty!")
        continue
    import random
    number=random.randint(1,max_number)
    count=1
    won=False
    while(attempt!=0) :
        key=int(input(f"Attempt {count} : "))
        if key==number :
            print("you won")
            print("Congratulations!!")
            print(f"you guessed it in {count} attempts")
            count+=1
            won=True
            break
        elif key<number :
            print("too low")
        else :
            print("too high")
        count+=1
        attempt-=1
    if not won :
        print("game over!!")
        print(f"the correct anwser was {number} ")
    choice=input("play again (yes/no) :").lower()
    if choice!='yes' :
        print("thank you for playing ")
        break