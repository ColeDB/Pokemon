import random
import sys
import time
attack = ["attack", "Attack"]
kick = ["kick", "Kick"]
punch = ["punch", "Punch"]
throw = ["tackle", "Tackle"]
run = ["run", "Run"]
print("Duh Duh Duh Duh Duh")
name=input("What is your Name? ")
park = random.randint(1,4)
if (park == 1):
    pokemon1=("Squirrel")
    pokemonhp=15
    mindamage=2
    maxdamage=10
    attacks="Nibbles You"
    size=1
elif(park == 2):
    pokemon1=("Mole")
    pokemonhp=20
    mindamage=3
    maxdamage=10
    attacks="Nips you"
    size=1
elif(park == 3):
    pokemon1=("Skunk")
    pokemonhp=25
    mindamage=4
    maxdamage=13
    attacks="Bites You!"
    size=2
elif(park == 4):
    pokemon1=("Bear")
    pokemonhp=35
    mindamage=5
    maxdamage=20
    attacks="Claws You!"
    size=3
print("You are walking through the forest, minding your own business")
time.sleep(1)
print("Suddenly")
time.sleep(.4)
print("A wild "+ pokemon1 +" Appears")
time.sleep(.7)
print("The "+ pokemon1 +" Looks very angry!")
time.sleep(.6)
ok=input("What will you do? ")
time.sleep(.6)
print("It Attacks!")
time.sleep(.5)
userhp = 30
print(""+ pokemon1 +" = "+ str(pokemonhp)+"")
print("" + name + " = 30hp")
while userhp >= 1 and pokemonhp >= 1:
    attack1=0
    attack1 = random.randint(mindamage, maxdamage)
    userhp = userhp - attack1
    print("The "+ pokemon1 +" "+ attacks +"")
    print("" + str(name) + " = " + str(userhp) + "hp")
    if (attack1 > 6):
        print("It was Super Effective")
    elif (attack1 < 4):
        print("It was not very Effective")
    if(userhp<=0):
        print("You Died!")
        time.sleep(.6)
        print("The "+ pokemon1 +" was too strong!")
        sys.exit()
    do1 = input("What will you do?,Attack or Run? ")
    if (do1 in attack):
        b = input("Punch, Kick, or Tackle ")
        if (b in punch):
            print("You punch the "+ pokemon1 +"")
            punch2=0
            punch2 = random.randint(1, 15)
            pokemonhp = pokemonhp - punch2
            print("" + str(pokemon1) + " = " + str(pokemonhp) + "hp")
            if (punch2 > 6):
                print("You punch "+ pokemon1 +"")
                print("It was Super Effective!")
            if (punch2 < 4):
                print("It was not that Effective")
        elif (b in kick):
            print("You Kick "+ pokemon1 +"")
            kick2=0
            kick2 = random.randint(5, 10)
            if (kick2 == 10 and size == 1):
                print("You kick the " + pokemon1 + " it goes flying")
                time.sleep(1)
                print("You have defeated the " + pokemon1 + "")
                sys.exit()
            pokemonhp = pokemonhp - kick2
            print("" + str(pokemon1) + " = " + str(pokemonhp) + "hp")
            if (kick2 > 8):
                print("You kick at the "+ pokemon1 +"")
                print("It was Super Effective!")
            if (kick2 < 6):
                print("It was not that Effective")
        elif (b in throw):
            if(size==3):
                print("Lmao, what are you trying to do")
                time.sleep(.6)
                print("It stares at you")
                time.sleep(.5)
                print("It barely budges")
                throw2=0
                throw2 = random.randint(1,8)
            else:
                print("You tackle the "+ pokemon1 +"")
                throw2=0
                throw2 = random.randint(3, 12)
            pokemonhp = pokemonhp - throw2
            print(""+ str(pokemon1) +" = "+ str(pokemonhp) + "hp")
            if (throw2 > 6):
                print("It Gets knocked down!")
                print("It was Super Effective!")
            if (throw2 < 4):
                print("It was not that Effective")
    if (do1 in run):
        print("You run away. Pussy")
        sys.exit()
    if (userhp <= 0):
        print("Lmao, you died")
    elif (pokemonhp <= 0):
        print("Great job, "+ pokemon1 +" fainted")

print("done")
