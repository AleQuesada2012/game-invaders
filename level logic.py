# 3 levels
import time
import keyboard
import threading


class Player:
    def __init__(self):
        self.points = 0
        self.lives = 3
        self.name = ""

    def hit(self):
        if self.lives != 0:
            self.lives -= 1
            print("hit player with 1HP.")
        else:
            print("player is already at 0 HP.")
player1 = Player()


def level_1():
    try:

        pps = 1  # points per second
        player1.name = "Messi"
        t = 60
        while t != 0:
            if player1.lives > 0:
                print("Time: " + str(t))
                player1.points += pps
                print("points: " + str(player1.points))
                t -= 1
                time.sleep(1)
            else:
                break
        print(player1.name + " got: " + str(player1.points) + " and had " + str(player1.lives) + " lives remaining.")
    except:
        print("no se pudo")


def hitmarker(player):
    while True:
        if keyboard.read_key() == "x":
            player.hit()
            print("player got hit!")
            time.sleep(0.2)


T_level1 = threading.Thread(target=level_1, args= [])
T_damageTracker = threading.Thread(target=hitmarker, args=[player1])
T_level1.start()
T_damageTracker.start()
