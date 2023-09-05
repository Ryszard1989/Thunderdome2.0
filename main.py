# First version to make those clickbait mobile games of blobs eating each other to grow bigger

from gameManager import GameManager
from gameBoard import GameBoard

import pygame

def testPygame():
    # Example file showing a circle moving on screen

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        pygame.draw.circle(screen, "red", player_pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
             player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
             player_pos.x += 300 * dt

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()

class Blob:
    def __init__(self, color, size, x=0, y=0):
        self.color = color
        self.size = size
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

def main():

    # Define player and enemies
    player = Blob("red", 1, 0, 0)
    enemies = []
    enemies.append(Blob("blue", 1, 1, 2))
    enemies.append(Blob("green", 2, 4, 3))
    enemies.append(Blob("green", 2, 3, 2))
    enemies.append(Blob("blue", 1, 2, 1))       
    enemies.append(Blob("blue", 1, 2, 2))

    #testPygame()

    gameManager = GameManager(player, enemies, GameBoard(6,6))
    gameManager.start()



if __name__ == "__main__":
    main()