import random
import os.path

# Define Character Variables
# Name, Race, Level, CurrentHP, Potions
characterData = ['name', 'Human', 1, 100, 3]

# Define Game Variables
damage = 4
maxHP = 20
hitChance = 65

potionPoints = 25
isDead = False

orcDamage = 3
bossDamage = 5

isDead = False




def saveCharacter(characterData):
    #creates new filefor your characters data
    oFile = open(characterData[0] + ".txt", 'w')

    for var in characterData:
        oFile.write(str(var) + "\n")

    oFile.close()


def loadCharacter(characterName):
    #Finds your characters data if you've created a character before
    oFile = open(characterName + ".txt", 'r')

    characterData = oFile.readlines()

    oFile.close()
    
    #Assigns the race and modifiers that your loaded character had
    race = characterData[1]
    assignRaceModifiers(race)

    return characterData


def assignRaceModifiers(race):
    #Assigns the different modifiers for the different races
    if race == "Human":
        damage = 5
        maxHP = 105
    elif race == "Elf":
        hitChance = 70
        maxHP = 98
    elif race == "Dwarf":
        hitChance = 70
        damage = 5
    elif race == "Hobbit":
        damage = 3
        hitChance = 75


def createCharacterMenu():
    #fancy menu to create a new character and pick a race
    print("|===========================================|")
    print("|          Name Your New Character          |")
    print("|===========================================|")
    print("")
    characterData[0] = str(input(""))

    while True:
        print("|===========================================|")
        print("|               Select a Race               |")
        print("|===========================================|")
        print("|       1) Human          2) Elf            |")
        print("|       3) Dwarf          4) Hobbit         |")
        print("|===========================================|")
        print("")
        selection = int(input(''))

        #Assigns correct race and attributes for selection picked
        if selection == 1:
            characterData[1] = 'Human'
            break
        elif selection == 2:
            characterData[1] = 'Elf'
            break
        elif selection == 3:
            characterData[1] = 'Drawf'
            break
        elif selection == 4:
            characterData[1] = 'Hobbit'
            break
        else:
            print ("Invalid Selection...")

    race = characterData[1]
    assignRaceModifiers(race)

    # Assign Current HP to maxHP that was assigned in assignRaceModifiers method.
    characterData[3] = maxHP

    saveCharacter(characterData)

#Main menu to pick new character, load character, or quit
def startMenu():
    while True:
        print("|===========================================|")
        print("|           Battle of Helms Deep            |")
        print("|===========================================|")
        print("|       1)  Create New Character            |")
        print("|       2)     Load Character               |")
        print("|       3)         Quit                     |")
        print("|===========================================|")
        print("")

        selection = int(input(''))

        # Create New Character
        if selection == 1:
            createCharacterMenu()
            battle()

        # Load Character
        elif selection == 2:
            print ("Enter the Name of the Character you wish to load")
            characterName = str(input(""))

            if os.path.isfile(characterName + ".txt"):
                characterData = loadCharacter(characterName)
                battle()
            else:
                print ("No saved character by that name...")

        # Quit
        elif selection == 3:
            quit()
            break


def battle():

    isDead = False

    currentHP = characterData[3]
    potions = characterData[4]

    while isDead == False:

        # Fight 4 Regular Orcs
        for x in range(0, 4):
            # Set New Orc Health
            orcHP = 12

            print("|===========================================|")
            print("|        You have encountered an orc!       |")
            print("|===========================================|")

            # While we are both alive
            while currentHP > 0 and orcHP > 0:
                print("|===========================================|")
                print("|  My HP: " + str(currentHP) + " | Potions: " + str(potions) + " | Orc HP: " + str(orcHP))
                print("|===========================================|")

                print("1) Attack  2) Drink Potion 3) Save and Quit")
                option = int(input())

                # Attack
                if option == 1:
                    playerHit = random.randint(1,100)

                    if playerHit <= hitChance:
                        print ("You hit!\n")
                        orcHP = orcHP - damage
                    else:
                        print ("You missed!")
                        print ("Orc laughs in your face\n")

                # Drink Potion
                elif option == 2:
                    potions = potions - 1
                    currentHP = currentHP + potionPoints

                    # Limit currentHP to maxHP
                    if currentHP > maxHP:
                        currentHP = maxHP
                elif option == 3:
                    characterData[3] = currentHP
                    characterData[4] = potions
                    saveCharacter(characterData)
                    quit()
                else:
                    print("Invalid Option")
                    continue


                # Orc Attack
                orcHit = random.randint(1,100)

                if orcHit <= 35:
                    print ("You have been hit!\n")
                    currentHP = currentHP - orcDamage
                else:
                    print ("The Orc missed!")

            # Check if we are alive or dead
            if currentHP <= 0:
                isDead = True




        # Fight Boss Orc
        print("|===========================================|")
        print("|      You have encountered Uruk-hai!       |")
        print("|===========================================|")
        # Set New Orc Health
        orcHP = 12

        # While we are both alive
        while currentHP > 0 and orcHP > 0:
            print("|===========================================|")
            print("|  My HP: " + str(currentHP) + " | Potions: " + str(potions) + " | Orc HP: " + str(orcHP))
            print("|===========================================|")

            print("1) Attack  2) Drink Potion 3) Save and Quit")
            option = int(input())

            # Attack
            if option == 1:
                playerHit = random.randint(1,100)

                if playerHit <= hitChance:
                    print ("You hit!\n")
                    orcHP = orcHP - damage
                else:
                    print ("You missed!")
                    print ("Orc laughs in your face\n")

            # Drink Potion
            elif option == 2:
                potions = potions - 1
                currentHP = currentHP + potionPoints

                # Limit currentHP to maxHP
                if currentHP > maxHP:
                    currentHP = maxHP
            # Save and Quit
            elif option == 3:
                characterData[3] = currentHP
                characterData[4] = potions
                saveCharacter(characterData)
                quit()
            else:
                print("Invalid Option")
                continue


            # Orc Attack
            orcHit = random.randint(1,100)

            if orcHit <= 45:
                print ("You have been hit!\n")
                currentHP = currentHP - bossDamage
            else:
                print ("The Orc missed!")

        # Check if we are alive or dead
        if currentHP <= 0:
            isDead = True
        else:
            break

    if isDead == True:
        print("You Lost...")
    else:
        print("\n\nYou Win!\n\n")

    startMenu()


def main():
    startMenu()

# Start Script
main()
