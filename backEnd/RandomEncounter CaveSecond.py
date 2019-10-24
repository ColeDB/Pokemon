import random
import sys
attack = ["attack", "Attack"]
kick = ["kick", "Kick"]
punch = ["punch", "Punch"]
throw = ["throw", "Throw"]
run = ["run", "Run"]
badnames = ["Jakob", "Craig", "Jean", "Ezra", "Angus", "Trevor"]
realjobs = ["chef", "Chef", "businessman", "Businessman", "mechanic", "Mechanic", "crackhead", "Crackhead"]
xp = 1
print("Duh Duh Duh Duh Duh")
name=input("What is your Name? ")

if (name in badnames):
    print("Jesus christ, did your parents just want to doom you from the start?")
else:
    print("Nice to meet you " + name + "")
cont = 0
while cont == 0:
    type = input("What is your job? Chef, Businessman, Mechanic")
    if type in realjobs :
        cont = 1
    else:
        print("That wasn't an option")
        cont=0

print("You wander into a small cave and notice a figure!")
cave = random.randint(1, 4)
if (cave == 1):
    pokemon1=("Golbat")
    print("A wild "+ pokemon1 +" Appears")
    pokemonhp = 15
    userhp = 25
    print(""+ pokemon1 +" = 25hp")
    print("" + name + " = 30hp")

    while userhp >= 1 and pokemonhp >= 1:
        if type == "crackhead" or "Crackhead":
            attack1 = 10
        elif type == "Chef" or "chef":
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
        do1 = input("What will you do? Attack or Run?")
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
            xp+=75
            print("xp 0 --> xp" + str(xp))


    print("done")
if (cave == 2):
    pokemon1 = ("Zubat")
    print("A wild " + pokemon1 + " Appears")
    pokemonhp = 10
    userhp = 25
    print("" + pokemon1 + " = 25hp")
    print("" + name + " = 30hp")

    while userhp >= 1 and pokemonhp >= 1:
        if type == "crackhead" or "Crackhead":
            attack1 = 10
        elif type == "Mechanic" or "mechanic":
            attack1 = random.randint(6,10)
        else:
            attack1 = random.randint(1, 6)
        userhp = userhp - attack1
        print("" + pokemon1 + " uses Slam!")
        print("" + str(name) + " = " + str(userhp) + "hp")
        if (attack1 > 6):
            print("It was Super Effective")
        elif (attack1 < 4):
            print("It was not very Effective")
        do1 = input("What will you do? Attack or Run?")
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
            xp+=75
            print("xp 0 --> xp" + str(xp))

if (cave == 3):
    pokemon1 = ("Ekans")
    print("A wild " + pokemon1 + " Appears")
    pokemonhp = 18
    userhp = 25
    print("" + pokemon1 + " = 25hp")
    print("" + name + " = 30hp")

    while userhp >= 1 and pokemonhp >= 1:
        if type == "crackhead" or "Crackhead":
            attack1 = 10
        elif type == "Buisnessman" or "buisnassman":
            attack1 = random.randint(6,10)
        else:
            attack1 = random.randint(1,6)
        userhp = userhp - attack1
        print("" + pokemon1 + " uses Slam!")
        print("" + str(name) + " = " + str(userhp) + "hp")
        if (attack1 > 6):
            print("It was Super Effective")
        elif (attack1 < 4):
            print("It was not very Effective")
        do1 = input("What will you do? Attack or Run?")
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
            xp += 75
            print("xp 0 --> xp" + str(xp))


if (cave == 4):
    pokemon1 = ("Sableye")
    print("A wild " + pokemon1 + " Appears")
    pokemonhp = 15
    userhp = 25
    print("" + pokemon1 + " = 25hp")
    print("" + name + " = 30hp")

    while userhp >= 1 and pokemonhp >= 1:

        attack1 = random.randint(1, 10)
        if type == "crackhead" or "Crackhead":
            attack1 = 10
        userhp = userhp - attack1
        print("" + pokemon1 + " uses Slam!")
        print("" + str(name) + " = " + str(userhp) + "hp")
        if (attack1 > 6):
            print("It was Super Effective")
        elif (attack1 < 4):
            print("It was not very Effective")
        do1 = input("What will you do? Attack or Run?")
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
            xp += 75
            print("xp 0 --> xp" + str(xp))
print("Having defeated the pokemon guarding the entrance of the cave, you decide to venture inside")
direction = input("Which way do you go? Forwards, Left, or Right")
if direction.lower() == "left":
    print("You walk straight into a man in a preist's outfit. He promptly attempts to baptise you")
    userhp = 25
    pokemonhp = 20
    while userhp >= 1 and pokemonhp >= 1:
        pokemon1 = "Not So Kind Old Man"
        attack1 = random.randint(1, 10)
        if type == "crackhead" or "Crackhead":
            attack1 = 10
        userhp = userhp - attack1
        print("" + pokemon1 + " uses Slam!")
        print("" + str(name) + " = " + str(userhp) + "hp")
        if (attack1 > 6):
            print("It was Super Effective")
        elif (attack1 < 4):
            print("It was not very Effective")
        do1 = input("What will you do? Attack or Run?")
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
            print("Lmao, you died and you corpse was never found.")
        elif (pokemonhp <= 0):
            print("Great job, " + pokemon1 + " fainted, and you are able to rescue the children within his abode, along with a quart of holy water. This may come in useful, so you decide to keep it")
            xp += 200
            print("xp 0 --> xp" + str(xp))
            print("After defeating the old man, you discover that he was Sean Connery's half brother. A bounty is placed onto your head as you are forced to flee. ")
            print()
            print("After a long and arduous chase, you finally escape his assasins, only to come face to face with the man himself.")
            print()
            print("He pulls out a silenced pistol and starts firing. Thankfully, in true movie fashion, the first three shots go into the ground where you are standing")
            print()
            print("As you cower in fear behind a nearby rock he suddenly has a stroke, colapsing on the ground. you approach, picking up his gun, and promptly flee to venezuela, where you live out the rest of your life")