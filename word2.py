import random

print("****************WELCOME TO WORD GUESSING GAME!****************")
print("--------------------------------------------------------------")
player = str(input("Enter your name>"))
print("Hello", player, "!" "\nReady to start?")


words = [
    "bat",
    "hello",
    "ice",
    "man",
    "girl",
    "python",
    "math",
    "code",
    "sun",
    "moon",
]
print("You have to choose between these words->", words)


truns = len(words)
steps = int(truns / 2)
print("you have", steps, "chances!")


ran = random.choice(words)
correct = ran

guess = str(input("Enter a word> "))
count = 1

while count < steps - 1:
    count += 1

    for ran in words:

        if guess not in ran:
            count + 1
            # print("wrong! Guess another!", "\nThis is your ", count - 1, "try!")
            break

    guess2 = str(input("Try another one> "))

    if guess2 == ran:
        print("Guessed right!")
        print("Congratulation!", player, " \nThe word is:", ran)
        print("You won!")

        break
    if count == steps - 1:
        print("This is your last try!")
        final = str(input("Try for a last time> "))
        if final == ran:
            print("congratulation")

        else:
            print("you loose! Better luck next time!")
            print("The correct number is> ", ran)
