import random
import sys
attack = ["attack", "Attack"]
kick = ["kick", "Kick"]
punch = ["punch", "Punch"]
throw = ["throw", "Throw"]
run = ["run", "Run"]
print("Duh Duh Duh Duh Duh")
name=input("What is your Name? ")
type = input("What is your job?"
             "Chef, Businessman, Mechanic")
cave = random.randint(1, 4)
if (cave == 1):
    pokemon1=("Golbat")
    print("A wild "+ pokemon1 +" Appears")
    pokemonhp = 15
    userhp = 25
    print(""+ pokemon1 +" = 25hp")
    print("" + name + " = 30hp")

    while userhp >= 1 and pokemonhp >= 1:
        if type == "Chef" or "chef":
            attack1 = random.randint(6, 10)
        else:
            attack1 = random.randint(1, 6)
        userhp = userhp - attack1
        print(""+ pokemon1 +"uses Slam!")
        print("" + str(name) + " = " + str(userhp) + "hp")
        if (attack1 > 6):
            print("It was Super Effective")
        elif (attack1 < 4):
            print("It was not very Effective")
        do1 = input("What will you do?,Attack or Run?")
        if (do1 in attack):
            b = input("Punch, Kick, or Throw")
            if (b in punch):
                print("You punch the "+ pokemon1 +"")
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
                kick2 = random.randint(5, 10)
                pokemonhp = pokemonhp - kick2
                print("" + str(pokemon1) + " = " + str(pokemonhp) + "hp")
                if (kick2 > 8):
                    print("You kick at the "+ pokemon1 +"")
                    print("It was Super Effective!")
                if (kick2 < 6):
                    print("It was not that Effective")
            elif (b in throw):
                print("You shove the "+ pokemon1 +"")
                throw2 = random.randint(3, 12)
                pokemonhp = pokemonhp - throw2
                print(""+ str(pokemon1) +" = "+ str(pokemonhp) + "hp")
                if (throw2 > 6):
                    print("You shove it hard!")
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
if (cave == 2):
    pokemon1 = ("Zubat")
    print("A wild " + pokemon1 + " Appears")
    pokemonhp = 10
    userhp = 25
    print("" + pokemon1 + " = 25hp")
    print("" + name + " = 30hp")

    while userhp >= 1 and pokemonhp >= 1:
        attack1 = random.randint(1, 10)
        userhp = userhp - attack1
        print("" + pokemon1 + " uses Slam!")
        print("" + str(name) + " = " + str(userhp) + "hp")
        if (attack1 > 6):
            print("It was Super Effective")
        elif (attack1 < 4):
            print("It was not very Effective")
        do1 = input("What will you do?,Attack or Run?")
        if (do1 in attack):
            b = input("Punch, Kick, or Throw")
            if (b in punch):
                print("You punch the " + pokemon1 + "")
                punch2 = random.randint(1, 15)
                pokemonhp = pokemonhp - punch2
                print("" + str(pokemon1) + " = " + str(pokemonhp) + "hp")
                if (punch2 > 6):
                    print("You punch " + pokemon1 + "")
                    print("It was Super Effective!")
                if (punch2 < 4):
                    print("It was not that Effective")
            elif (b in kick):
                print("You Kick " + pokemon1 + "")
                kick2 = random.randint(5, 10)
                pokemonhp = pokemonhp - kick2
                print("" + str(pokemon1) + " = " + str(pokemonhp) + "hp")
                if (kick2 > 8):
                    print("You kick at the " + pokemon1 + "")
                    print("It was Super Effective!")
                if (kick2 < 6):
                    print("It was not that Effective")
            elif (b in throw):
                print("You shove the " + pokemon1 + "")
                throw2 = random.randint(3, 12)
                pokemonhp = pokemonhp - throw2
                print("" + str(pokemon1) + " = " + str(pokemonhp) + "hp")
                if (throw2 > 6):
                    print("You shove it hard!")
                    print("It was Super Effective!")
                if (throw2 < 4):
                    print("It was not that Effective")
        if (do1 in run):
            print("You run away. Pussy")
            sys.exit()
        if (userhp <= 0):
            print("Lmao, you died")
        elif (pokemonhp <= 0):
            print("Great job, " + pokemon1 + " fainted")
if (cave == 3):
    pokemon1 = ("Ekans")
    print("A wild " + pokemon1 + " Appears")
    pokemonhp = 18
    userhp = 25
    print("" + pokemon1 + " = 25hp")
    print("" + name + " = 30hp")

    while userhp >= 1 and pokemonhp >= 1:
        attack1 = random.randint(1, 10)
        userhp = userhp - attack1
        print("" + pokemon1 + " uses Slam!")
        print("" + str(name) + " = " + str(userhp) + "hp")
        if (attack1 > 6):
            print("It was Super Effective")
        elif (attack1 < 4):
            print("It was not very Effective")
        do1 = input("What will you do?,Attack or Run?")
        if (do1 in attack):
            b = input("Punch, Kick, or Throw")
            if (b in punch):
                print("You punch the " + pokemon1 + "")
                punch2 = random.randint(1, 15)
                pokemonhp = pokemonhp - punch2
                print("" + str(pokemon1) + " = " + str(pokemonhp) + "hp")
                if (punch2 > 6):
                    print("You punch " + pokemon1 + "")
                    print("It was Super Effective!")
                if (punch2 < 4):
                    print("It was not that Effective")
            elif (b in kick):
                print("You Kick " + pokemon1 + "")
                kick2 = random.randint(5, 10)
                pokemonhp = pokemonhp - kick2
                print("" + str(pokemon1) + " = " + str(pokemonhp) + "hp")
                if (kick2 > 8):
                    print("You kick at the " + pokemon1 + "")
                    print("It was Super Effective!")
                if (kick2 < 6):
                    print("It was not that Effective")
            elif (b in throw):
                print("You shove the " + pokemon1 + "")
                throw2 = random.randint(3, 12)
                pokemonhp = pokemonhp - throw2
                print("" + str(pokemon1) + " = " + str(pokemonhp) + "hp")
                if (throw2 > 6):
                    print("You shove it hard!")
                    print("It was Super Effective!")
                if (throw2 < 4):
                    print("It was not that Effective")
        if (do1 in run):
            print("You run away. Pussy")
            sys.exit()
        if (userhp <= 0):
            print("Lmao, you died")
        elif (pokemonhp <= 0):
            print("Great job, " + pokemon1 + " fainted")
if (cave == 4):
    pokemon1 = ("Sableye")
    print("A wild " + pokemon1 + " Appears")
    pokemonhp = 15
    userhp = 25
    print("" + pokemon1 + " = 25hp")
    print("" + name + " = 30hp")

    while userhp >= 1 and pokemonhp >= 1:
        attack1 = random.randint(1, 10)
        userhp = userhp - attack1
        print("" + pokemon1 + " uses Slam!")
        print("" + str(name) + " = " + str(userhp) + "hp")
        if (attack1 > 6):
            print("It was Super Effective")
        elif (attack1 < 4):
            print("It was not very Effective")
        do1 = input("What will you do?,Attack or Run?")
        if (do1 in attack):
            b = input("Punch, Kick, or Throw")
            if (b in punch):
                print("You punch the " + pokemon1 + "")
                punch2 = random.randint(1, 15)
                pokemonhp = pokemonhp - punch2
                print("" + str(pokemon1) + " = " + str(pokemonhp) + "hp")
                if (punch2 > 6):
                    print("You punch " + pokemon1 + "")
                    print("It was Super Effective!")
                if (punch2 < 4):
                    print("It was not that Effective")
            elif (b in kick):
                print("You Kick " + pokemon1 + "")
                kick2 = random.randint(5, 10)
                pokemonhp = pokemonhp - kick2
                print("" + str(pokemon1) + " = " + str(pokemonhp) + "hp")
                if (kick2 > 8):
                    print("You kick at the " + pokemon1 + "")
                    print("It was Super Effective!")
                if (kick2 < 6):
                    print("It was not that Effective")
            elif (b in throw):
                print("You shove the " + pokemon1 + "")
                throw2 = random.randint(3, 12)
                pokemonhp = pokemonhp - throw2
                print("" + str(pokemon1) + " = " + str(pokemonhp) + "hp")
                if (throw2 > 6):
                    print("You shove it hard!")
                    print("It was Super Effective!")
                if (throw2 < 4):
                    print("It was not that Effective")
        if (do1 in run):
            print("You run away. Pussy")
            sys.exit()
        if (userhp <= 0):
            print("Lmao, you died")
        elif (pokemonhp <= 0):
            print("Great job, " + pokemon1 + " fainted")