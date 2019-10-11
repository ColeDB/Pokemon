import random
import time
import sys
attack=["attack","Attack"]
claw=["Claw","claw"]
Bite=["Bite","bite"]
growl=["Growl","growl"]
kick=["Kick","kick"]
punch=["Punch","punch"]
catch=["Catch","catch"]
run=["Run","run"]
human=input("What is your name? ")
humanhp=20
humanmindamagepunch=5
humanmaxdamagepunch=12
humanattacks="Punch"
humansize=2
humansound="ARAAAARGH!"
pokeballs=10
pokemon=("Bear")
pokemonhp=35
mindamage=5
maxdamage=20
attacks=("Claw")
size=3
cp=40
sound="GROOOWL"
print("The Bear looks easy to catch!")
catchit=input("Do you catch it? ")
pokeballs=pokeballs-1
time.sleep(.2)
print("You have successfully caught the "+ pokemon +"")
pokemon1=pokemon
pokemonhp1=pokemonhp
mindamage1=mindamage
maxdamage1=maxdamage
attacks1=attacks
size1=size
cp1=cp
sound1=sound
time.sleep(.2)
print("Another Rabbit!")
pokemon=("Rabbit")
pokemonhp=20
mindamage=10
maxdamage=15
attacks=("Bite")
size=1
cp=25
sound="KNKNKNK"
input("Do you Catch it? ")
pokeballs=pokeballs-1
time.sleep(.2)
print("You have successfully captured the "+ pokemon +"")
pokemon2=pokemon
pokemonhp2=pokemonhp
mindamage2=mindamage
maxdamage2=maxdamage
attacks2=attacks
size2=size
cp2=cp
sound2=sound
time.sleep(.7)
print("Suddenly a Wild Boar comes out of the water!")
pokemonbad="Boar"
pokemonbadhp=25
mindamagebad=5
maxdamagebad=15
attackbad="Horns"
sizebad=2
cpbad=40
soundbad="OIINNNK!"
lolwhat=1
time.sleep(.5)
print(soundbad)
time.sleep(.4)
while lolwhat==1:
    lolwhat=0
    select=input("Which pokemon will you select? "+ pokemon1 +", "+ pokemon2 +" ")
    if(select==pokemon1):
        pokemon=pokemon1
        pokemonhp=pokemonhp1
        mindamage=mindamage1
        maxdamage=maxdamage1
        attacks=attacks1
        size=size1
        cp=cp1
        sound=sound1
        time.sleep(.2)
        print("You Select " + pokemon + "!")
    elif(select==pokemon2):
        pokemon=pokemon2
        pokemonhp=pokemonhp2
        mindamage=mindamage2
        maxdamage=maxdamage2
        attacks=attacks2
        size=size2
        cp=cp2
        sound=sound2
        time.sleep(.2)
        print("You Select "+ pokemon +"!")
    else:
        print("ERROR: You must choose either a creature that you have!")
        lolwhat=lolwhat+1
print(""+ pokemonbad +" = "+ str(pokemonbadhp)+"hp")
print("" + str(pokemon) + " = "+ str(pokemonhp) +"hp")
time.sleep(.4)
print(sound)
pokemonstathp1=pokemonhp1
pokemonstathp2=pokemonhp2
while pokemonhp >= 1 and pokemonbadhp >= 1:
    attack1=0
    attack1 = random.randint(mindamagebad, maxdamagebad)
    pokemonhp = pokemonhp - attack1
    time.sleep(.3)
    print("The "+ pokemonbad +" uses "+ attackbad +"")
    print("It deals "+ str(attack1) +"dmg!")
    print("" + str(pokemon) + " = " + str(pokemonhp) + "hp")
    if (attack1 >= 10):
        print("It was super effective!")
    if (attack1 <= 6):
        print("It was not that effective")
    (sound)
    if(pokemonhp<=0 and pokemon==human):
        print("You have been knocked out!")
        sys.exit()
    if(pokemonhp<=0 and (pokemonstathp1>=1 or pokemonstathp2>=1)):
        time.sleep(.4)
        print("Your "+ pokemon +" has fainted!")
        time.sleep(.3)
        if(pokemon==pokemon2 and pokemonstathp1>=1):
            pokemonstathp2=0
            pokemon = pokemon1
            pokemonhp = pokemonhp1
            mindamage = mindamage1
            maxdamage = maxdamage1
            attacks = attacks1
            size = size1
            cp = cp1
            sound = sound1
            print("You select " + pokemon + "")
        if(pokemon==pokemon1 and pokemonstathp2>=1):
            pokemonstathp1=0
            pokemon = pokemon2
            pokemonhp = pokemonhp2
            mindamage = mindamage2
            maxdamage = maxdamage2
            attacks = attacks2
            size = size2
            cp = cp2
            sound = sound2
            print("You select "+ pokemon +"")
        else:
            print("All you creatures are dead, it is up to you!")
            pokemon = human
            pokemonhp = humanhp
            mindamage = humanmindamagepunch
            maxdamage = humanmaxdamagepunch
            attacks = humanattacks
            size = humansize
            sound = humansound
    do1=input("What will you do? Attack, Catch or Run? ")
    if(do1 in attack):
        time.sleep(.4)
        attackem=input("What will you do? "+ attacks +"")
        if(attackem in attacks):
            print(""+ str(pokemon) +" uses "+ attacks +"")
            boom=random.randint(mindamage,maxdamage)
            pokemonbadhp = pokemonbadhp - boom
            print("It deals " + str(boom) + "dmg!")
            print(""+ str(pokemonbad) +" = "+ str(pokemonbadhp) +"hp")
            if(boom>=10):
                print("It was super effective!")
            if(boom<=6):
                print("It was not that effective")
            (soundbad)
            if (pokemonbadhp <= 0):
                print("The " + pokemonbad + " has fainted!")
    if(do1 in catch):
        pokeball=random.randint(1,4)
        time.sleep(.4)
        print("You throw a net at the "+ pokemonbad +"!")
        pokeballs=pokeballs-1
        time.sleep(.4)
        print("You have "+ str(pokeballs) +" left")
        if(pokeball==1 or 2):
            time.sleep(.6)
            print("Bum")
            time.sleep(.6)
            print("Bing")
            time.sleep(.6)
            print("BOOM!")
            time.sleep(.4)
            print("You have successfully caught the "+ pokemonbad +"")
            print(""+ pokemonbad +" has been added to your team!")
            pokemon3 = pokemonbad
            pokemonhp3 = pokemonbadhp
            mindamage3 = mindamagebad
            maxdamage3 = maxdamagebad
            attacks3 = attackbad
            size3 = sizebad
            cp3 = cpbad
            sound3 = soundbad
            pokemonbadhp=0
        else:
            time.sleep(.6)
            print("Bum")
            time.sleep(.6)
            print("Bing")
            time.sleep(.6)
            print("BRRUOM")
            print("The "+ pokemonbad +" broke out!")
    if(do1 in run):
        print("You try to run, but the "+ pokemonbad +" is faster")
print("Done")







