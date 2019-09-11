import random
pokemon1=("Golbat")
combatlvl=10
print("A wild Golbat appears!")
pokeball=input("Do you want to catch him?")
if(pokeball=="yes"):
    print("You throw a ball!")
    if(combatlvl<=15):
        catchrate = random.randint(1, 4)
        if(catchrate==4):
            print(""+ pokemon1 + " Broke out")
        else:
            print("Golbat was caught, Congratulations!")



