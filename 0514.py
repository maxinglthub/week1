import random
num = random.randint(1,10)

print("I have a sercrt number between 1 and 10")
guess = int(input("guess my number"))

if guess == num:
    print("got it")
elif guess < num:
        print("too small")
elif guess > num:
        print("too high")

print ("the number is", num)