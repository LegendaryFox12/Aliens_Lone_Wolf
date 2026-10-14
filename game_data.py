import random

reset = '\033[0m'
red = '\033[31m' 
green = '\033[32m' 
yellow = '\033[33m' 
blue = '\033[34m' 
cyan = '\033[36m' 
bold = '\033[1m'

print(" ")

rankD = {
    1: "Private",
    2: "Corporal",
    3: "Sergeant"
}

marinePoints = 0
weapon = 0
ammo = 99
money = 0
healthNum = 10
medkits = 3
grenades = 3
ownGun1 = False
ownGun2 = False
cheat = False
colonists = random.randint(5, 15)
remainingColonists = colonists

currentRank = rankD[1]

weaponList = [
    "M41A Pulse Rifle",
    "M240 Incinerator",
    "M56 Smartgun"
]

inventory = {
    "Marine Points": marinePoints,
    "Ammo": ammo,
    "Weapon": weaponList[weapon],
    "Money": money,
    "Medkits": medkits,
    "Grenades": grenades
}

inventory = {}
health = ["*"] * healthNum + [" "] * (15 - healthNum)   

asked_about_okay = False
asked_about_others = False
asked_about_goodbye = False
asked_about_retreat = False
asked_about_hurt = False
asked_about_goodbye2 = False