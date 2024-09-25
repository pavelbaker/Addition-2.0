import random

def quiz(questions):
    score= 0
    for j in range(questions):
        a = random.randint(0,100)
        b = random.randint(0,100)
        answer = a+b

        while True:
            try:
                user_answer = input(f"what is {a} + {b}? ")
                if answer == int(user_answer):
                    print("you are correct")
                    score+=1
                    break
                else:
                    print("incorrect")
                    break
            except ValueError:
                print("This is not a number, try again")

    print(f"You got {score} out of {questions}")
