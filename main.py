import pygame
from levels import Level
from window import Window
from entities.player import Player


def startGame(window, player):
    win = True
    players = ["moto.png", "jogging.png", "spaceship.png"]
    mobs = ["car.png", "medicine-ball.png", "asteroid.png"]
    backgrounds = ["calle3.jpg", "Cancha3.jpg", "planeta1.jpg"]
    for i in range(1, 4):
        final = False
        if i == 3:
            final = True
        player.setImage(players[i - 1])
        if not Level(window, player, backgrounds[i - 1], mobs[i - 1], final=final).start(2 * i, 2 * i):
            print("Lost")
            win = not win
            break
    if win:
        # Do the wining stuff
        print("WIN")
    else:
        # Do the loosing stuff
        print("LOST")


def about(window):
    # Poner imágenes y texto del about.
    # <<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return


def main():
    window = Window()
    # Poner imagen del background y textos
    # pygame.image.load("images/...")
    listening = True
    while listening:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    listening = False
                    break
                if event.key == pygame.K_p:
                    about(window)

                elif event.key == pygame.K_ESCAPE:
                    return False
    player = Player(window)
    startGame(window, player)


if __name__ == '__main__':
    main()
