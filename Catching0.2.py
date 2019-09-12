import random
pokemon1=("Golbat")
combatlvl=20
print("A wild "+ pokemon1 +" appears!")
pokeball=input("Do you want to catch him?")
if(pokeball=="yes")
    print("You throw a ball!")
    if (combatlvl >= 80): #80+:20%
        catchrate = random.randint(1, 5)
        if (catchrate == 5):
            print("" + pokemon1 + " was caught, Congratulations!")
        else:
            print("" + pokemon1 + " Broke Out!")
    elif(combatlvl >=50): #50-80:50%
        catchrate = random.randint(1, 4)
        if(catchrate==4):
            print(""+ pokemon1 + " was caught, Congratulations!")
        else:
            print(""+ pokemon1 +" Broke Out!")
    elif (combatlvl >= 16):#16-40:50%
        catchrate = random.randint(1, 4)
        if (catchrate == 4 or 5):
            print("" + pokemon1 + " Broke out")
        else:
            print("" + pokemon1 + " was caught, Congratulations!")
    elif (combatlvl >= 40): #15:75%
        catchrate = random.randint(1, 4)
        if (catchrate == 4):
            print("" + pokemon1 + " Broke out")
        else:
            print("" + pokemon1 + " was caught, Congratulations!")

    #15:75%
    #16-40:50%
    #40-80:30%
    #80+:25%



