# First version to make those clickbait mobile games of blobs eating each other to grow bigger

from gameManager import GameManager
from gameBoard import GameBoard
import random
import math

import pygame

def testPygame():
    # Example file showing a circle moving on screen

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720)) # Means 1280 to right. 720 down.
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    player_size = 40

    enemy1_pos = pygame.Vector2(100, 100)
    enemy1_size = 20
    enemy1_initial_direction = random.randint(1,360)
    enemy1_vel_x = math.cos(enemy1_initial_direction) * 5
    enemy1_vel_y = math.sin(enemy1_initial_direction) * 5

    enemy2_pos = pygame.Vector2(900, 500)
    enemy2_size = 50
    enemy2_initial_direction = random.randint(1,360)
    enemy2_vel_x = math.cos(enemy2_initial_direction) * 3
    enemy2_vel_y = math.sin(enemy2_initial_direction) * 3


    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        pygame.draw.circle(screen, "red", player_pos, player_size)
        pygame.draw.circle(screen, "blue", enemy1_pos, enemy1_size)
        pygame.draw.circle(screen, "green", enemy2_pos, enemy2_size)

        #player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if player_pos.y > 0 + player_size:
                player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            if player_pos.y < screen.get_height() - player_size:
                player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            if player_pos.x > 0 + player_size:
                player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            if player_pos.x < screen.get_width() - player_size:
                player_pos.x += 300 * dt

        #check if enemy has hit wall and needs to change direction
        enemy1_pos.y -= enemy1_vel_y
        enemy1_pos.x += enemy1_vel_x

        if enemy1_pos.x - enemy1_size < 0 or enemy1_pos.x + enemy1_size > screen.get_width():
            enemy1_vel_x *= -1 
        if enemy1_pos.y - enemy1_size < 0 or enemy1_pos.y + enemy1_size > screen.get_height():
            enemy1_vel_y *= -1

        enemy2_pos.y -= enemy2_vel_y
        enemy2_pos.x += enemy2_vel_x

        if enemy2_pos.x - enemy2_size < 0 or enemy2_pos.x + enemy2_size > screen.get_width():
            enemy2_vel_x *= -1 
        if enemy2_pos.y - enemy2_size < 0 or enemy2_pos.y + enemy2_size > screen.get_height():
            enemy2_vel_y *= -1 

        # works for grid nicely, not good for real time. Maybe some element later?
        # enemy2MovementInput = random.choice(['up','left','down','right','x','x','x','x']) # 'x' to "slow" enemy down with invalid moves
        # if enemy2MovementInput is 'up':
        #     if enemy2_pos.y > 0:
        #         enemy2_pos.y -= 300 * dt
        # if enemy2MovementInput is 'down':
        #     if enemy2_pos.y < screen.get_height():
        #         enemy2_pos.y += 300 * dt
        # if enemy2MovementInput is 'left':
        #     if enemy2_pos.x > 0:
        #         enemy2_pos.x -= 300 * dt
        # if enemy2MovementInput is 'right':
        #     if enemy2_pos.x < screen.get_width():
        #         enemy2_pos.x += 300 * dt

        #player/enemy collisions
        if player_pos.distance_to(enemy1_pos) < ((player_size + enemy1_size) * 0.9):
            player_size += enemy1_size
            enemy1_size = 0
        if player_pos.distance_to(enemy2_pos) < ((player_size+enemy2_size) * 0.9):
            player_size += enemy2_size
            enemy2_size = 0
            

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

    testPygame()

    #gameManager = GameManager(player, enemies, GameBoard(6,6))
    #gameManager.start()



if __name__ == "__main__":
    main()