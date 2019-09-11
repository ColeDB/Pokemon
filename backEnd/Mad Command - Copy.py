import random
import sys

Computerhp = 25

userhp = 30
name = input("what is your name")


print("Computer = 25hp")
print("" + name + " = 30hp")

# Port = random.randint(1, 10)
# userhp = userhp - Port
# print("" + str(name) + " = " + str(userhp) + "hp")
# if(Port>6):
#     print("It was Super Effective!")
# elif(Port<4):
#     print("It was not that Effective")
#     do=input("What will you do?,Attack or Run?")
#     if(do=="Attack"):
#         a=input("Punch, Kick, or Throw")
#         if(a=="Punch"):
#             print("You punch the computer")
#             punch1 = random.randint(1,15)
#             Computerhp = Computerhp - punch1
#             print("Computer= " + str(Computerhp) + "hp")
#             if(punch1>6):
#                 print("Your fist goes straight through the computer")
#                 print("It was Super Effective!")
#             if(punch1<4):
#                 print("It was not that Effective")
#         elif (a=="Kick"):
#             print("You Kick the computer")
#             kick1 = random.randint(5, 10)
#             Computerhp = Computerhp - kick1
#             print("Computer= " + str(Computerhp) + "hp")
#             if (kick1 > 8):
#                 print("Your fist goes straight through the computer")
#                 print("It was Super Effective!")
#             if (kick1 < 6):
#                 print("It was not that Effective")
#         elif (a=="Throw"):
#             print("You throw the computer")
#             throw1 = random.randint(3, 12)
#             Computerhp = Computerhp - throw1
#             print("Computer= " + str(Computerhp) + "hp")
#             if (throw1 > 6):
#                 print("Your fist goes straight through the computer")
#                 print("It was Super Effective!")
#             if (throw1 < 4):
#                 print("It was not that Effective")
#         elif(do=="Run"):
#             print("You run away")
#             sys.exit()
# else:
#     print("You hurt your brain deciding and die")
#     print("The computer attacks!")
#     print("It Whips you with a mouse!")
attack = ["attack", "Attack"]
kick = ["kick", "Kick"]
punch = ["punch", "Punch"]
throw = ["throw", "Throw"]
run = ["run", "Run"]

while userhp >= 1 and Computerhp >= 1:
    mouse1 = random.randint(1, 10)
    userhp = userhp - mouse1
    print("The computer attacks!, It zaps you with its port!")
    print("" + str(name) + " = " + str(userhp) + "hp")
    if(mouse1>6):
        print("It was Super Effective")
    elif(mouse1<4):
        print("It was not very Effective")
    do1 = input("What will you do?,Attack or Run?")
    if (do1 in attack):
        b = input("Punch, Kick, or Throw")
        if (b in punch):
            print("You punch the computer")
            punch2 = random.randint(1, 15)
            Computerhp = Computerhp - punch2
            print("Computer= " + str(Computerhp) + "hp")
            if (punch2 > 6):
                print("Your fist goes straight through the computer")
                print("It was Super Effective!")
            if (punch2 < 4):
                print("It was not that Effective")
        elif (b in kick):
            print("You Kick the computer")
            kick2 = random.randint(5, 10)
            Computerhp = Computerhp - kick2
            print("Computer= " + str(Computerhp) + "hp")
            if (kick2 > 8):
                print("Your fist goes straight through the computer")
                print("It was Super Effective!")
            if (kick2 < 6):
                print("It was not that Effective")
        elif (b in throw):
            print("You throw the computer")
            throw2 = random.randint(3, 12)
            Computerhp = Computerhp - throw2
            print("Computer= " + str(Computerhp) + "hp")
            if (throw2 > 6):
                print("Your fist goes straight through the computer")
                print("It was Super Effective!")
            if (throw2 < 4):
                print("It was not that Effective")
    if(do1 in run):
        print("You run away. Pussy")
        sys.exit()
    if(userhp <= 0):
        print("Lmao, you died")
    elif(Computerhp <= 0):
        print("Great job, you almost died while trying to eliminate a non-animate object.")


print("done")