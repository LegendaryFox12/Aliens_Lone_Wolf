import game_data as gs
import gameplay
import missions
import os

def intro():
    os.system('clear' if os.name == 'nt' else 'clear')
    print(" ")
    print("|=========================================|")
    print("|------------ MARINE DATABASE ------------|")
    print("|=========================================|")
    print("| Welcome, Colonial Marine.               |")
    print("|=========================================|")
    gs.name = input("| Enter your name: ")

def startGame():
    intro()
    missions.selectMission()

    gs.healthNum = max(0, min(15, gs.healthNum))
    gameplay.updateHealth()
    gameplay.updateInventory()

    print(" ")
    print("|=========================================|")
    print("|------------- MARINE STATUS -------------|")
    print("|=========================================|")
    print(f"| Marine: {gs.name:<32}|")
    print(f"| Rank: {gs.currentRank:<34}|")
    print("|=========================================|")

    missions.runMission()


if __name__ == "__main__":
    startGame()
