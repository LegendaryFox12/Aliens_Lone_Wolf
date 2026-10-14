import game_data as gs
import game_data as gd
from game_data import red, yellow, cyan, reset
import gameplay
import os
import random

def selectMission():
    while True:
        try:
            print(" ")
            print("|=========================================|")
            print("|-------------- MISSION SELECT -----------|")
            print("|=========================================|")
            print("| 1 | Rescue Dr. Johns                    |")
            print("| 2 | Search For the Colony               |")
            print("| 3 | Evacuate the Colonists              |")
            print("| 4 | Destroy the Hive                    |")
            print("| 5 | Kill the Queen                      |")
            print("|=========================================|")
            gs.mission = int(input("| Select a mission: "))

            if 1 <= gs.mission <= 5:
                return

            elif gs.mission == 12:
                gs.name = "Chao Mein"
                gs.money += 99999999999
                gs.marinePoints += 99999999999
                gs.ammo += 99999999999
                gs.grenades += 99999999999
                gs.medkits += 99999999999
                gs.ownGun1 = True
                gs.ownGun2 = True
                gs.cheat = True
                gameplay.updateInventory()
                print("| CHEAT CODE ACTIVATED.                   ")

            else:
                print("| Please enter a number between 1 and 5. ")

        except ValueError:
            print(f"| {red}INVALID INPUT{reset}                           ")

def missionOne():
    os.system('clear' if os.name == 'nt' else 'clear')
    print(" ")
    print("|=========================================|")
    print("|-------------- MISSION ONE --------------|")
    print("|=========================================|")
    print("| Rescue Dr. Johns                        |")
    print("|=========================================|")
    print(" ")

    print(
        "The mission is simple. Dr. Johns and his group "
        "landed on planet LV-426 in order to conduct research "
        "on the Xenomorphs. They are now trapped and need your "
        "assistance. Good luck Marine, and stay frosty."
    )

    print(" ")

    print(
        "You have arrived on LV-426. You see the transport "
        "ship used by Dr. Johns and his crew to arrive. It "
        "is eerily quiet. Just beyond the ship is a building. "
        "If he and his crew are taking refuge anywhere, it's "
        "in there."
    )

    print(" ")
    print(
        "You step into the building, your dim flashlight "
        "doing little to illuminate the dark hallway. "
        "A Xenomorph screeches somewhere in the distance. "
        "Already, you know this won't be good."
    )

    print(" ")
    print(
        "You hear something ahead of you. And then, you see "
        "the slender figure."
    )

    print(" ")

    gameplay.encounter()
    gameplay.choice()

    print(" ")
    print(
        "You continue deeper into the building. Dark blue "
        "vines creep from a vent at floor level. The vines "
        "you know all too well. A hive is nearby."
    )

    print(" ")
    print(
        "You notice something caught by your flashlight. A "
        "trail of blood turns the corner just ahead of you. "
        "You hesitate, at first, but remember your mission. "
        "That could be the blood of Dr. Johns, or one of his "
        "members. Regardless, it's someone who needs help. "
        "The light reflects off of the shiny surface. It's "
        "fresh."
    )

    print(" ")
    print(
        "Around the corner, there it is. The hive. You don't "
        "plan on sticking around long. There's not a single "
        "part of you that wants to be there, so you decide to "
        "get the civilian and leave. As soon as possible. "
    )

    print(" ")
    print(
        "You walk through the hive, occasionally tripping "
        "over an extra-terrestrial tube. You use the blood "
        "as a pinpoint. You pass by multiple corpses strung "
        "up in the nest with gaping holes in their chest. "
        "Telling by the freshness of the blood, the person "
        "should still be alive. At least, you hope. "
    )

    print(" ")
    print(
        "However, your search is interrupted by the "
        "unmistakable sound of a Xenomorph screech. "
    )

    gameplay.encounter()
    gameplay.choice()

    print(" ")
    print(
        "You reach the end of the hive. Your flashlight scans "
        "across the back wall and finds Dr. Johns. You cut him "
        "out of the vines and he collapses to the ground. "
    )

    print(" ")

    while True:
        try:
            print(f"{yellow}|=========================================|{reset}")
            print(f"{yellow}|------------------ You ------------------|{reset}")
            print(f"{yellow}|=========================================|{reset}")
            if not gd.asked_about_okay:
                print(f"{yellow}| 1 | Are you okay?                       |{reset}")
            if not gd.asked_about_others:
                print(f"{yellow}| 2 | Where is everyone else?             |{reset}")
            if not gd.asked_about_goodbye:
                print(f"{yellow}| 3 | Goodbye.                            |{reset}")
            print(f"{yellow}|=========================================|{reset}")
            dialogue = int(input(f"{yellow}| What do you say? {reset}"))
            print(" ")

            if dialogue == 1 and not gd.asked_about_okay:
                gd.asked_about_okay = True
                print(f"{cyan}|=========================================|{reset}")
                print(f"{cyan}|--------------- Dr. Johns ---------------|{reset}")
                print(f"{cyan}|=========================================|{reset}")
                print(f"{cyan}| Yes, I am fine. But barely. We need to  |{reset}")
                print(f"{cyan}| find the others before it's too late.   |{reset}")
                print(f"{cyan}|=========================================|{reset}")
                print(" ")

            elif dialogue == 2 and not gd.asked_about_others:
                gd.asked_abut_others = True
                print(f"{cyan}|=========================================|{reset}")
                print(f"{cyan}|--------------- Dr. Johns ---------------|{reset}")
                print(f"{cyan}|=========================================|{reset}")
                print(f"{cyan}| We got turned around in the hive...     |{reset}")
                print(f"{cyan}| I believe the others went deeper into   |{reset}")
                print(f"{cyan}| LV-426. I was heading to find them when |{reset}")
                print(f"{cyan}| this... creature found me.              |{reset}")
                print(f"{cyan}|=========================================|{reset}")
                break

            elif dialogue == 3 and not gd.asked_about_goodbye:
                gd.asked_about_goodbye = True
                print(f"{cyan}|=========================================|{reset}")
                print(f"{cyan}|--------------- Dr. Johns ---------------|{reset}")
                print(f"{cyan}|=========================================|{reset}")
                print(f"{cyan}| Wait! Where are you going? You need to  |{reset}")
                print(f"{cyan}| hear this!                              |{reset}")
                print(f"{cyan}|=========================================|{reset}")
                print(" ")

            elif dialogue > 3:
                print("| Please enter 1, 2, or 3. ")
                print(" ")

            else:
                print("| That option is no longer availible. ")
                print(" ")
                
        except ValueError:
            print(" ")
            print(f"| {red}INVALID INPUT{reset} ")
            print(" ")

    print(" ")

    print(
        "Dr. Johns grabs his chest. He looks to be in pain. "
        "His sharp exhales are the only confirmation you need. "
    )

    print(" ")

    print(
        "Something erupts from his chest in a bloody splatter. "
        "You look back over to the section of the wall that "
        "previously held him captive. A dead facehugger lay "
        "on the ground. It's too late. "
    )

    selectMission()
    runMission()

def missionTwo():
    os.system('clear' if os.name == 'nt' else 'clear')
    print(" ")
    print("|=========================================|")
    print("|-------------- MISSION TWO --------------|")
    print("|=========================================|")
    print("| Search For the Colony                   |")
    print("|=========================================|")
    print(" ")

    print(
        "You failed your first mission. Not off to a great start "
        "so far. Make up for it this time. Dr. Johns gave you "
        "everything you need to know to accomplish this next one. "
        "You have no excuse to fail. "
    )

    print(" ")

    print(
        "You start off deeper into the core of the planet. You hear "
        "The shrieks of Xenomorphs get louder the further you decsend. "
        "Every few steps, you see parts of the underground bunker peek "
        "out of the hive, just a reminder of what this place once was. "
    )

    print(" ")

    print(
        "Out of the corner of your eye, you see a figure leap in your "
        "direction. You move to the side, barely avoiding it. "
    )

    gameplay.encounter()
    gameplay.choice()

    print(
        "A little shaken, you carry on. You scan the hallway. There's no "
        "sign of colonists. At least, non that are alive. "
    )

    print(" ")

    print(
        "The smell and sight of corpses makes your stomach turn every which "
        "way. So far, you haven't seen any Xenomorphs. This concerns you."
    )

    print(" ")

    print(
        "The wet vines let out a squeak with every step you take. You don't know "
        "what they're made of, but maybe it's best that way. The overhead lights "
        "don't help much. You make a right, then take a flight of stairs even further "
        "into the planet. Then you see them. "
    )

    print(" ")

    print(
        "In the corner of the large, open room you've just entered, a group of people "
        "huddle in the corner, shivering and trying to stay quiet. "
        )

    print(" ")

    while True:
        try:
            print(f"{yellow}|=========================================|{reset}")
            print(f"{yellow}|------------------ You ------------------|{reset}")
            print(f"{yellow}|=========================================|{reset}")
            if not gd.asked_about_retreat:
                print(f"{yellow}| 1 | I'm gonna get you out of here.      |{reset}")
            if not gd.asked_about_hurt:
                print(f"{yellow}| 2 | Is anyone hurt?                     |{reset}")
            if not gd.asked_about_goodbye2:
                print(f"{yellow}| 3 | Goodbye.                            |{reset}")
            print(f"{yellow}|=========================================|{reset}")
            dialogue = int(input(f"{yellow}| What do you say? {reset}"))
            print(" ")

            if dialogue == 1 and not gd.asked_about_retreat:
                gd.asked_about_retreat = True
                print(f"{cyan}|=========================================|{reset}")
                print(f"{cyan}|---------------- Colonist ---------------|{reset}")
                print(f"{cyan}|=========================================|{reset}")
                print(f"{cyan}| Thank you! We've been stuck here for... |{reset}")
                print(f"{cyan}|=========================================|{reset}")
                break

            elif dialogue == 2 and not gd.asked_about_hurt:
                gd.asked_about_hurt = True
                print(f"{cyan}|=========================================|{reset}")
                print(f"{cyan}|---------------- Colonist ---------------|{reset}")
                print(f"{cyan}|=========================================|{reset}")
                print(f"{cyan}| No, we're fine. The only ones who got   |{reset}")
                print(f"{cyan}| got hurt are...                         |{reset}")
                print(f"{cyan}|=========================================|{reset}")
                print(" ")

            elif dialogue == 3 and not gd.asked_about_goodbye2:
                gd.asked_about_goodbye2 = True
                print(
                    "You turn to leave when a wet squish and the crunching "
                    "of bones stops you cold. You look back and see the sharp "
                    "end of a Xenomorph tail penetrate the chest of the colonist. "
                    "You raise your weapon, but the Xenomorph is already there. "
                    )

                gameplay.dead()

            elif dialogue > 3:
                print("| Please enter 1, 2, or 3. ")
                print(" ")

            else:
                print("| That option is no longer availible. ")
                print(" ")
                
        except ValueError:
            print(" ")
            print(f"| {red}INVALID INPUT{reset} ")
            print(" ")

    print(" ")

    print(
        "Multiple Xenomorphs surround you in an instant. The creatures taunt "
        "you, hissing and flashing their inner jaw. Protect the colonists. "
        f"At {red}ALL{reset} costs. "
        )

    gameplay.heavyEncounter()
    gameplay.choice()

    killedColonists = random.randint(0, gd.colonists)
    gd.remainingColonists = max(0, gd.remainingColonists - killedColonists)

    if gd.remainingColonists == 0:
        print(
        "You tried your best, but the Xenomorphs tried harder. You died protecting "
        "the colonists. At least you went out with honor. "
        )

        gameplay.dead()

    print(" ")

    print(
        f"{gd.remainingColonists} colonists remain. In the fight, you lost {gd.colonists - gd.remainingColonists} "
        "colonists. Bring the rest of them to safety."
    )

    selectMission()
    runMission()

def missionThree():
    os.system('clear' if os.name == 'nt' else 'clear')
    print(" ")
    print("|=========================================|")
    print("|------------- MISSION THREE -------------|")
    print("|=========================================|")
    print("| Evacuate the Colonists                  |")
    print("|=========================================|")
    print(" ")

    print(
        "As you continue to exit the hive, you hear a low hiss as somethig "
        "drips onto your shoulder. Looking up, the face of a Xenomorph looks "
        "back at you. It drops down to your level. This fight won't be easy. "
    )

    gameplay.encounter()
    gameplay.choice()

    killedColonists = random.randint(1, 3)

    print(" ")

    gd.remainingColonists = max(0, gd.remainingColonists - killedColonists)

    if killedColonists == 1:
        print(f"The Xenomorph took 1 down. {gd.remainingColonists} remain.")
    else:
        print(f"The Xenomorph took {killedColonists} down. {gd.remainingColonists} remain.")

    if gd.remainingColonists == 0:
        print(
            "You tried your best, but the Xenomorphs tried harder. You died protecting "
            "the colonists. At least you went out with honor. "
        )
        gameplay.dead()

    print(" ")

    print(
        "You reach a fork in the path. Which way did you come from? You stop and start "
        "second-guessing yourself. Giving a group of Xenomorphs enough time to creep up "
        "on you. "
        )

    gameplay.heavyEncounter()
    gameplay.choice()

    killedColonists = random.randint(1, 3)
    
    print(" ")
    
    gd.remainingColonists = max(0, gd.remainingColonists - killedColonists)
    
    if killedColonists == 1:
        print(f"The Xenomorph took 1 down. {gd.remainingColonists} remain.")
    else:
        print(f"The Xenomorph took {killedColonists} down. {gd.remainingColonists} remain.")
    
    if gd.remainingColonists == 0:
        print(
            "You tried your best, but the Xenomorphs tried harder. You died protecting "
            "the colonists. At least you went out with honor. "
        )
        gameplay.dead()

    print(
        "You bring the remaining colonists back to the surface. A military aircraft "
        "lands, allowing the colonists to board."
    )

    print(" ")

    print(f"{cyan}|=========================================|{reset}")
    print(f"{cyan}|------------------ Pilot ----------------|{reset}")
    print(f"{cyan}|=========================================|{reset}")
    print(f"{cyan}| Are you coming {gd.currentRank} {gd.name}?        |{reset}")
    print(f"{cyan}|=========================================|{reset}")

    print(" ")

    print(
        "You look back. You know you could end the hive. End all of this."
    )

def runMission():
    if gs.mission == 1:
        missionOne()
    elif gs.mission == 2:
        missionTwo()
    elif gs.mission == 3:
        print("|=========================================|")
        print("|------------- MISSION THREE -------------|")
        print("|=========================================|")
        print("| Mission under construction.              |")
        print("|=========================================|")
    elif gs.mission == 4:
        print("|=========================================|")
        print("|-------------- MISSION FOUR -------------|")
        print("|=========================================|")
        print("| Mission under construction.              |")
        print("|=========================================|")
    elif gs.mission == 5:
        print("|=========================================|")
        print("|-------------- MISSION FIVE -------------|")
        print("|=========================================|")
        print("| Mission under construction.              |")
        print("|=========================================|")
