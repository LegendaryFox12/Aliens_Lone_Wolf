import random
import game_data as gs
import game_data as gd
from game_data import red, green, reset

def updateInventory():
    gs.inventory = {
        "Marine Points": gs.marinePoints,
        "Ammo": gs.ammo,
        "Weapon": gs.weaponList[gs.weapon],
        "Money": gs.money,
        "Medkits": gs.medkits,
        "Grenades": gs.grenades,
    }


def updateHealth():
    gs.health = [f"{red}*{reset}"] * (15 - gs.healthNum) + [f"{green}*{reset}"] * gs.healthNum
    missing = red + "*" * (15 - gd.healthNum) + reset
    current = green + "*" * gd.healthNum + reset
    gd.health = missing + current

def dead():
    print(" ")
    print(f"              {red}GAME OVER, MAN.{reset}              ")
    print(f"                 {red}GAME OVER.{reset}                ")
    print("                                           ")
    print("            ________     ____              ")
    print("           (________)==<(-_- )             ")
    print("             /|__|\\     /|__|\\           ")
    print("           __/|  |       |  |              ")
    print(" ")
    raise SystemExit


def updateRank():
    if gs.currentRank == gs.rankD[1] and gs.marinePoints >= 300:
        print(" ")
        print("|=========================================|")
        print("|---------------- RANK UP ----------------|")
        print("|=========================================|")
        gs.currentRank = gs.rankD[2]
        print(f"| Congratulations, {gs.currentRank:<20}|")
        print("|=========================================|")

    elif gs.currentRank == gs.rankD[2] and gs.marinePoints >= 650:
        print(" ")
        print("|=========================================|")
        print("|---------------- RANK UP ----------------|")
        print("|=========================================|")
        gs.currentRank = gs.rankD[3]
        print(f"| Congratulations, {gs.currentRank:<20}|")
        print("|=========================================|")

def showInventory():
    updateInventory()
    print(" ")
    print("|=========================================|")
    print("|--------------- INVENTORY ---------------|")
    print("|=========================================|")

    for item, quantity in gs.inventory.items():
        print(f"| {item:<15} {str(quantity):>23} |")

    print(f"| {'Health'}                   {gd.health}|")
    print("|=========================================|")

def shop():
    while True:
        print(" ")
        print("|=========================================|")
        print("|------------------ SHOP -----------------|")
        print("|=========================================|")
        print(f"| {green}Money: ${gs.money:<31}{reset} |")
        print(f"| Marine Points: {gs.marinePoints:<24} |")
        print("|=========================================|")
        print("| 1 | Ammunition                          |")
        print("| 2 | Weapons                             |")
        print("| 3 | Medkits                             |")
        print("| 4 | Grenades                            |")
        print("| 5 | Exit                                |")
        print("|=========================================|")

        try:
            shopChoice = int(input("| Select an option: "))
            print(" ")

            if shopChoice == 1:
                print(" ")
                print("|=========================================|")
                print("|-------------- AMMUNITION ---------------|")
                print("|=========================================|")
                print(f"| {green}Money: ${gs.money:<31}{reset} |")
                print(f"| Maximum rounds: {int(gs.money / 0.10):<18}      |")
                print("|=========================================|")

                amount = int(input("| Rounds to purchase: "))
                print(" ")

                if amount < 0:
                    print(f"| {red}INVALID INPUT{reset}                       ")
                    continue

                ammoPrice = amount * 0.10

                if gs.money < ammoPrice:
                    print(f"| {red}You don't have enough money.{reset}            ")
                else:
                    gs.money -= ammoPrice
                    gs.ammo += amount
                    updateInventory()
                    print("| Rounds purchased. ")

            elif shopChoice == 2:
                while True:
                    print(" ")
                    print("|=========================================|")
                    print("|-------------- WEAPON SHOP --------------|")
                    print("|=========================================|")
                    print("| 1 | M240 Incinerator                    |")
                    print(f"|   | {green}$2000{reset} + 125 Marine Points           |")
                    print("|-----------------------------------------|")
                    print("| 2 | M56 Smartgun                        |")
                    print(f"|   | {green}$3500{reset} + 350 Marine Points           |")
                    print("|-----------------------------------------|")
                    print("| 3 | Exit                                |")
                    print("|=========================================|")

                    try:
                        purchaseWeapon = int(input("| Select a weapon: "))
                        print(" ")

                        if purchaseWeapon == 1:
                            if gs.ownGun1:
                                print("| You already own this weapon.            ")
                            elif gs.money >= 2000 and gs.marinePoints >= 125:
                                gs.money -= 2000
                                gs.ownGun1 = True
                                updateInventory()
                                print("| M240 Incinerator purchased. ")
                            else:
                                print(f"| {red}You don't have enough resources.{reset}        ")
                                print(" ")

                        elif purchaseWeapon == 2:
                            if gs.ownGun2:
                                print("| You already own this weapon.            ")
                            elif gs.money >= 3500 and gs.marinePoints >= 350:
                                gs.money -= 3500
                                gs.ownGun2 = True
                                updateInventory()
                                print("| M56 Smartgun purchased. ")
                            else:
                                print(f"| {red}You don't have enough resources.{reset}        ")

                        elif purchaseWeapon == 3:
                            break

                        else:
                            print("| Please enter 1, 2, or 3.                ")

                    except ValueError:
                        print(f"| {red}INVALID INPUT{reset}                           ")

            elif shopChoice == 3:
                print(" ")
                print("|=========================================|")
                print("|---------------- MEDKITS ----------------|")
                print("|=========================================|")
                print(f"| {green}Money: ${gs.money:<31}{reset} |")
                print(f"| Maximum medkits: {int(gs.money / 25):<16}       |")
                print("|=========================================|")

                amount = int(input("| Medkits to purchase: "))
                print(" ")

                if amount < 0:
                    print(f"| {red}INVALID INPUT{reset}                        ")
                    continue

                medPrice = amount * 25

                if gs.money < medPrice:
                    print(f"| {red}You don't have enough money.{reset}            ")
                else:
                    gs.money -= medPrice
                    gs.medkits += amount
                    updateInventory()
                    print("| Medkits purchased.                      ")

            elif shopChoice == 4:
                print(" ")
                print("|=========================================|")
                print("|---------------- GRENADES ---------------|")
                print("|=========================================|")
                print(f"| {green}Money: ${gs.money:<31}{reset} |")
                print(f"| Maximum grenades: {int(gs.money / 45):<16}      |")
                print("|=========================================|")

                amount = int(input("| Grenades to purchase: "))
                print(" ")

                if amount < 0:
                    print(f"| {red}INVALID INPUT{reset}                        ")
                    continue

                grenPrice = amount * 45

                if gs.money < grenPrice:
                    print(f"| {red}You don't have enough money.{reset}            ")
                else:
                    gs.money -= grenPrice
                    gs.grenades += amount
                    updateInventory()
                    print("| Grenades purchased. ")

            elif shopChoice == 5:
                return

            else:
                print("| Please enter 1, 2, 3, or 4.             ")

        except ValueError:
            print(f"| {red}INVALID INPUT{reset}                           ")


def weaponSelect():
    while True:
        print(" ")
        print("|=========================================|")
        print("|------------- WEAPON SELECT -------------|")
        print("|=========================================|")
        print("| 1 | M41A Pulse Rifle                    |")

        if gs.ownGun1:
            print("| 2 | M240 Incinerator                    |")

        if gs.ownGun2:
            print("| 3 | M56 Smartgun                        |")

        print("| 4 | Exit                                |")
        print("|=========================================|")

        try:
            weaponChoice = int(input("| Select a weapon: "))

            if weaponChoice == 1:
                gs.weapon = 0
                updateInventory()
                print(" ")
                print("| M41A Pulse Rifle equipped.              ")
                return

            elif weaponChoice == 2 and gs.ownGun1:
                gs.weapon = 1
                updateInventory()
                print(" ")
                print("| M240 Incinerator equipped.              ")
                return

            elif weaponChoice == 3 and gs.ownGun2:
                gs.weapon = 2
                updateInventory()
                print(" ")
                print("| M56 Smartgun equipped.                  ")
                return

            elif weaponChoice == 4:
                return

            else:
                print("| You do not own that weapon.              ")

        except ValueError:
            print(f"| {red}INVALID INPUT{reset}                           ")

def choice():
    while True:
        print(" ")
        print("|=========================================|")
        print("|----------------- OPTIONS ---------------|")
        print("|=========================================|")
        print("| 1 | Check Inventory                     |")
        print("| 2 | Use Medkit                          |")
        print("| 3 | Weapon Select                       |")
        print("| 4 | Shop                                |")
        print("| 5 | Continue                            |")
        print("|=========================================|")

        try:
            decision = int(input("| Select an option: "))

            if decision == 1:
                showInventory()

            elif decision == 2:
                if gs.medkits > 0:
                    gs.medkits -= 1
                    gs.healthNum = min(15, gs.healthNum + 7)
                    updateInventory()
                    updateHealth()
                    print(" ")
                    print("| You used a medkit.                      ")
                else:
                    print("| You have no medkits.                    ")

            elif decision == 3:
                weaponSelect()

            elif decision == 4:
                shop()

            elif decision == 5:
                return

            else:
                print("| Please enter 1, 2, 3, 4, or 5. ")

        except ValueError:
            print(f"| {red}INVALID INPUT{reset} ")


def encounter():
    print(" ")
    print("|=========================================|")
    print("|--------------- ENCOUNTER ---------------|")
    print("|=========================================|")
    print("| 1 | Run                                 |")
    print("| 2 | Hide                                |")
    print("| 3 | Fight                               |")
    print("| 4 | Use Grenade                         |")
    print("|=========================================|")

    while True:
        try:
            ambush = int(input("| Select an option: "))
            print(" ")

            if ambush in [1, 2, 3, 4]:
                break

            print(f"| {red}INVALID INPUT{reset} ")

        except ValueError:
            print(f"| {red}INVALID INPUT{reset} ")

    if ambush == 1:
        pick = random.randint(1, 3)

        if pick == 1:
            print(
                "You decide it's best not to pick fights. You "
                "turn and run, but it's too late. The Xenomorph "
                "spotted you and, with your back turned, it "
                "pounces."
            )
            dead()
        else:
            print(
                "You decide it's best not to pick fights. You "
                "turn and run into the nearest room, and it "
                "worked. You stay there until the sound of heavy "
                "and fast footsteps trails out of earshot."
            )

    elif ambush == 2:
        pick = random.randint(1, 3)

        if pick == 1:
            print(
                "You know running will only make the thing see you, "
                "so you decide to hide. You make your way to a nearby "
                "locker that fits you perfectly. Through the slits, "
                "you see it right there. Your anxiety gets the better "
                "of you and your breathing escalates. You're just "
                "loud enough to be detected."
            )
            dead()
        else:
            print(
                "You know running will only make the thing see you, "
                "so you decide to hide. You make your way to a nearby "
                "locker that fits you perfectly. Through the slits, "
                "you see it right there. It looks around for a moment "
                "before running off. You go unnoticed."
            )

    elif ambush == 3:
        if gs.ammo <= 0:
            print("| Your weapon clicks empty.                ")
            dead()

        if gs.weapon == 0:
            pick = random.randint(1, 3)
        elif gs.weapon == 1:
            pick = random.randint(1, 4)
        else:
            pick = random.randint(1, 5)

        if gs.cheat:
            pick = 2

        ammoLoss = min(random.randint(10, 20), gs.ammo)
        gs.ammo -= ammoLoss

        if pick == 1:
            print(
                "You fire your weapon, unloading round after round "
                "of ammunition, but keep missing, giving the creature "
                "just enough time to catch up."
            )
            dead()
        else:
            if gs.cheat:
                damage = 0
            else:
                damage = random.randint(1, 2)

            acid = random.randint(1, 2)

            print(
                "It took a couple of bursts, and it got some hits "
                "on you, but you killed it."
            )

            gs.marinePoints += 25
            gs.healthNum -= damage
            gs.money += 500

            updateInventory()
            updateHealth()

            if gs.healthNum <= 0:
                dead()

            if acid == 1:
                acidDamage = random.randint(1, 2)

                print(
                    "Some acid splashed on you in the process "
                    "and you lost some health."
                )

                if not gs.cheat:
                    gs.healthNum -= acidDamage

                updateInventory()
                updateHealth()

                if gs.healthNum <= 0:
                    dead()

    elif ambush == 4:
        if gs.grenades >= 1:
            pick = random.randint(1, 5)

            if gs.cheat:
                pick = 5

            if pick == 1:
                print(
                    "Your grenade went off, but it was your "
                    "fault in the end. Throwing it farther is "
                    "ideal. "
                )
                dead()

            elif pick == 2:
                print(
                    "It dodges, running on the wall and barely "
                    "avoiding the grenade. The deafening boom "
                    "silences everything as the Xenomorph pounces. "
                )
                dead()
            else:
                print(
                    "You feel the heat on your face as a severed "
                    "Xenomorph head is propelled toward you and lands "
                    "by your feet. "
                )
                gs.grenades -= 1
                gs.marinePoints += 50
                gs.money += 500
                updateInventory()
        else:
            print(
                "You feel your pockets for a grenade, but find nothing "
                "but dead space."
            )
            dead()


def heavyEncounter():
    xenomorphs = random.randint(5, 10)
    deadXenomorphs = 0

    if gs.weapon == 0:
        killChance = 40
        ammoMinimum = 3
        ammoMaximum = 6
    elif gs.weapon == 1:
        killChance = 50
        ammoMinimum = 4
        ammoMaximum = 7
    else:
        killChance = 60
        ammoMinimum = 5
        ammoMaximum = 8

    print(" ")
    print("|=========================================|")
    print("|------------ HEAVY ENCOUNTER ------------|")
    print("|=========================================|")
    print(f"| Xenomorphs detected: {xenomorphs:<19}|     ")
    print("|=========================================|")
    print(f"| 1 | {gs.weaponList[gs.weapon]:<24}            |")
    print("| 2 | Grenade                             |")
    print("|=========================================|")

    while True:
        try:
            useOfWeapon = int(input("| Select an option: "))

            if useOfWeapon in [1, 2]:
                break
            else:
                print("| Please enter 1 or 2.")

        except ValueError:
            print(f"| {red}INVALID INPUT{reset}")

        print(" ")

    if useOfWeapon == 1:
        for _ in range(xenomorphs):
            if gs.ammo <= 0:
                print(
                    "You gave everything you had, but the "
                    "click of an empty gun is the last thing  "
                    "you hear. "
                )
                dead()

            ammoLoss = random.randint(ammoMinimum, ammoMaximum)
            ammoLoss = min(ammoLoss, gs.ammo)
            gs.ammo -= ammoLoss

            hit = random.randint(1, 100)

            if hit <= killChance:
                deadXenomorphs += 1

    elif useOfWeapon == 2:
        if gs.grenades <= 0:
            print(
                "You reach for a grenade, but find nothing but "
                "dead space. "
            )
            dead()

        gs.grenades -= 1

        grenadeKills = random.randint(2, 7)
        grenadeKills = min(grenadeKills, xenomorphs)
        deadXenomorphs = grenadeKills

        print(
            f"The grenade detonates in the middle of the swarm, "
            f"taking {grenadeKills} Xenomorphs with it."
        )

    survivingXenomorphs = xenomorphs - deadXenomorphs

    print(" ")
    print("|=========================================|")
    print(f"| Xenomorphs killed: {deadXenomorphs:<21}|")
    print(f"| Xenomorphs surviving: {survivingXenomorphs:<18}|")
    print(f"| Ammo remaining: {gs.ammo:<24}|")
    print(f"| Grenades remaining: {gs.grenades:<20}|")
    print("|=========================================|")
    print(" ")

    for _ in range(deadXenomorphs):
        if useOfWeapon == 1:
            gs.marinePoints += 25
        elif useOfWeapon == 2:
            gs.marinePoints += 50

        gs.money += 500

    if survivingXenomorphs > xenomorphs / 2:
        if useOfWeapon == 1:
            print(
                "You fire round after round into the crowd, "
                "but your efforts aren't enough."
            )
            dead()
        elif useOfWeapon == 2:
            print(
                "You got a few, but you severely overestimated "
                "the blast radius of your grenade."
            )
            dead()

    elif survivingXenomorphs == 0:
        print("You got them all. Good aim.")
    else:
        print(
            "You were able to get most of them, and the surviving "
            "Xenomorphs disappeared into the darkness."
        )

        damage = random.randint(1, survivingXenomorphs)
        gs.healthNum -= damage
        print(f"You take {damage} damage before they retreat.")

        if gs.healthNum <= 0:
            dead()

    updateInventory()
    updateHealth()
