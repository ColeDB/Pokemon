import random
import sys
Computerhp = 25
userhp = 30
Good=["Good","good","Great","great","Fantastic","fantastic","Fine","fine"]
Bad=["Bad","bad","Not Good","not good","Horrible","horrible","sad","Sad"]
Yes=["Yes","yes","yea","Yea","Yeah","yeah","Sure","sure","Of course","Of Course","of course","of Course"]
No=["No","no"]
Madmeter = 0
name=input("What is your name?")
Hello=input("How are you?")
if(Hello in Good):
    print("Ok, I get mad easily so dont tip me off!")
if(Hello in Bad):
    print("Ok, I get mad easily so dont tip me off!")
    Madmeter = +2
print(Madmeter)
say=input("Tell me something")
if(say in Bad):
    Madmeter = +3
    print("AY, What did I SAY!")
elif(say in Good):
    Madmeter = -1
    print("Alright That cooled me down")
else:
    print("I have NO idea what you said!")
    Madmeter = +2
print("Please dont make me angry! When I am angry, I start to fight!")
Can=input("Can you do that for me? ")
if(Can in Yes):
    print("Thank you sir, I believe you")
if(Can in No):
    print("Now you will see what is coming!")
    print("Computer = 25hp")
    print("" +name+ " = 30hp")
    print("The computer attacks!, It zaps you with its port!")
    Port = random.randint(1, 10)
    userhp = userhp - Port
    print("" + str(name) + " = " + str(userhp) + "hp")
    if(Port>6):
        print("It was Super Effective!")
    elif(Port<4):
        print("It was not that Effective")
    do=input("What will you do?,Attack or Run?")
    if(do=="Attack"):
        a=input("Punch, Kick, or Throw")
        if(a=="Punch"):
            print("You punch the computer")
            punch1 = random.randint(1,15)
            Computerhp = Computerhp - punch1
            print("Computer= " + str(Computerhp) + "hp")
            if(punch1>6):
                print("Your fist goes straight through the computer")
                print("It was Super Effective!")
            if(punch1<4):
                print("It was not that Effective")
        elif (a=="Kick"):
            print("You Kick the computer")
            kick1 = random.randint(5, 10)
            Computerhp = Computerhp - kick1
            print("Computer= " + str(Computerhp) + "hp")
            if (kick1 > 8):
                print("Your fist goes straight through the computer")
                print("It was Super Effective!")
            if (kick1 < 6):
                print("It was not that Effective")
        elif (a=="Throw"):
            print("You throw the computer")
            throw1 = random.randint(3, 12)
            Computerhp = Computerhp - throw1
            print("Computer= " + str(Computerhp) + "hp")
            if (throw1 > 6):
                print("Your fist goes straight through the computer")
                print("It was Super Effective!")
            if (throw1 < 4):
                print("It was not that Effective")
    elif(do=="Run"):
        print("You run away")
        sys.exit()
    else:
        print("You hurt your brain deciding and die")
    print("The computer attacks!")
    print("It Whips you with a mouse!")
    mouse1 = random.randint(1, 10)
    userhp = userhp - mouse1
    print("" + str(name) + " = " + str(userhp) + "hp")
    if(mouse1>6):
        print("It was Super Effective")
    elif(mouse1<4):
        print("It was not very Effective")
    do1 = input("What will you do?,Attack or Run?")
    if (do1 == "Attack"):
        b = input("Punch, Kick, or Throw")
        if (b == "Punch"):
            print("You punch the computer")
            punch2 = random.randint(1, 15)
            Computerhp = Computerhp - punch2
            print("Computer= " + str(Computerhp) + "hp")
            if (punch2 > 6):
                print("Your fist goes straight through the computer")
                print("It was Super Effective!")
            if (punch2 < 4):
                print("It was not that Effective")
        elif (b == "Kick"):
            print("You Kick the computer")
            kick2 = random.randint(5, 10)
            Computerhp = Computerhp - kick2
            print("Computer= " + str(Computerhp) + "hp")
            if (kick2 > 8):
                print("Your fist goes straight through the computer")
                print("It was Super Effective!")
            if (kick2 < 6):
                print("It was not that Effective")
        elif (b == "Throw"):
            print("You throw the computer")
            throw2 = random.randint(3, 12)
            Computerhp = Computerhp - throw2
            print("Computer= " + str(Computerhp) + "hp")
            if (throw2 > 6):
                print("Your fist goes straight through the computer")
                print("It was Super Effective!")
            if (throw2 < 4):
                print("It was not that Effective")
    if(do1=="Run"):
        print("You run away")
        sys.exit()
    else:
        print("I do not understand")
        sys.exit()


print("....a.d.s...d.g.es..f.n")
