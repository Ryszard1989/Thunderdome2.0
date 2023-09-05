import random
from gameBoard import GameBoard

def wasd(userInput):
    if userInput == "w":
        return "up"
    elif userInput == "a":
        return "left"
    elif userInput == "s":
        return "down"
    elif userInput == "d":
        return "right"
    elif userInput == "q":
        return "quit"
    else:
        return "unknown"

class GameManager:
    def __init__(self, player, enemies, gameBoard):
        self.gameBoard = gameBoard # Assumes a square. Extend to something more flexible later
        self.player = player
        self.enemies = enemies
        self.gameOver = False

    def moveBlob(self, moveInput, blob, gameBoard):
        if moveInput == "up":
            if(gameBoard.isValidMove(blob.x, blob.y - 1)):
                blob.move(blob.x, blob.y - 1)
            else:
                print ("Invalid move. Try again.") #Return this so not always logging errors other calls
        elif moveInput == "left":
            if(gameBoard.isValidMove(blob.x - 1, blob.y)):
                blob.move(blob.x - 1, blob.y)
            else:
                print ("Invalid move. Try again.")
        elif moveInput == "down":
            if(gameBoard.isValidMove(blob.x, blob.y + 1)):
                blob.move(blob.x, blob.y + 1)
            else:
                print ("Invalid move. Try again.")
        elif moveInput == "right":
            if(gameBoard.isValidMove(blob.x + 1, blob.y)):
                blob.move(blob.x + 1, blob.y)
            else:
                print ("Invalid move. Try again.")
        elif moveInput == "quit":
            print ("Quitting game.")
            self.gameOver = True
        else:
            print ("Unknown command. Try again.")


    def blobFight(self, blob1, blob2): #TODO - move this to player/enemy class and go for custom definitions like entering keys to perform kill
        if blob1.size >= blob2.size:
            blob1.size += blob2.size
            blob2.size = 0
        else:
            blob2.size += blob1.size
            blob1.size = 0

    def start(self):

        # Standard intro and initial positions
        print ("WASD to move. Eat smaller blobs to grow bigger. Don't get eaten by bigger blobs. Good luck!")
        print ("Player: " + str(self.player.x) + ", " + str(self.player.y))
        
        # Main gameloop
        while self.gameOver is False:
            self.gameBoard.print(self.player, self.enemies)

            print ("Enter a move: ")
            
            #userInput = keyboard.is_pressed('left') #TODO - Move to arrow keys and not hitting enter
        
            userInput = input()
            moveInput = wasd(userInput)
            self.moveBlob(moveInput, self.player, self.gameBoard)

            #Enemy movement test cases
            #Move into a free space -> enemy moves 1 space
            #Move into a grid boundary -> prevented same as a player, misses turn
            #Move into a player -> initiates a fight. 
            #Move into another blob -> initiates a fight. 
            for enemy in self.enemies:
                enemyMovementInput = random.choice(['up','left','down','right','x','x','x','x']) # 'x' to "slow" enemy down with invalid moves
                self.moveBlob(enemyMovementInput, enemy, self.gameBoard)
            
            # Do everything resulting from a move
            # print ("Player: " + str(self.player.x) + ", " + str(self.player.y))
            for enemy in self.enemies:
                # print ("Enemy: " + str(enemy.x) + ", " + str(enemy.y))
                if self.player.x == enemy.x and self.player.y == enemy.y:
                    self.blobFight(self.player, enemy)

            #TODO - What will happen when 2 enemies and the player all land on same spot???? Look into later. --> Seem to end up with "X3X0". Investigate.
            for idx, enemy in enumerate(self.enemies):
                for idx2, enemy2 in enumerate(self. enemies):
                    if idx != idx2:
                        if enemy.x == enemy2.x and enemy.y == enemy2.y:
                            self.blobFight(enemy, enemy2)

            # Remove defeated enemies from the board
            for idx, x in enumerate(self.enemies):
                if x.size == 0:
                    self.enemies.pop(idx)
                    break
                                
            # Lose condition
            if self.player.size == 0:
                gameOver = True
                self.gameBoard.print(self.player, self.enemies)
                print("You lose.")
                break
            
            # Win condition
            enemySize = 0
            for enemy in self.enemies:
                enemySize += enemy.size
            if enemySize == 0:
                self.gameBoard.print(self.player, self.enemies)
                print("You win!")
                break

    def end(self):
        pass

    def restart(self):
        pass
