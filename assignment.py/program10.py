n=42
while True:
    guess=int(input("Guess the number:"))
    if(guess > n):
        print("Too high")
    elif(guess < n):
        print("Too low")
    else:
        print("You win!")
        break        