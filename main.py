# First version to make those clickbait mobile games of blobs eating each other to grow bigger

class Blob:
    def __init__(self, color, size, x=0, y=0):
        self.color = color
        self.size = size
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

class GameBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class GameManager:
    def __init__(self):
        self.gameBoard = GameBoard(5, 5)
        self.player = None
        self.enemies = []

    # prints board and all players in game to console
    def printGameBoard(self):
        for i in range(self.gameBoard.height):
            for j in range(self.gameBoard.width):
                loopBreak = False
                print ("|", end="")
                # TODO - Having enemies print first results in X3P0 due to nesting. Fix.
                if self.player.x == j and self.player.y == i:
                    print("P" + str(self.player.size), end="")
                    continue
                for enemy in self.enemies:
                    if enemy.x == j and enemy.y == i:
                        print("X" + str(enemy.size), end="")
                        loopBreak = True
                        continue
                if loopBreak is False:
                    print("--", end="")
                
            print("")

    def blobFight(self, blob1, blob2):
        if blob1.size >= blob2.size:
            blob1.size += blob2.size
            blob2.size = 0
        else:
            blob2.size += blob1.size
            blob1.size = 0

    def start(self):
        # Define player and enemies
        self.player = Blob("red", 1, 0, 0)
        self.enemies.append(Blob("blue", 1, 1, 2))
        self.enemies.append(Blob("green", 2, 4, 3))
        
        # Standard intro and initial positions
        print ("WASD to move. Eat smaller blobs to grow bigger. Don't get eaten by bigger blobs. Good luck!")
        print ("Player: " + str(self.player.x) + ", " + str(self.player.y))
        print ("Enemy 1: " + str(self.enemies[0].x) + ", " + str(self.enemies[0].y))
        print ("Enemy 2: " + str(self.enemies[1].x) + ", " + str(self.enemies[1].y))
        
        # Main gameloop
        gameOver = False
        while gameOver is False:
            self.printGameBoard()

            # Handle all possible moves. Evaluate after.
            print ("Enter a move: ")
            move = input()
            if move == "w":
                if(self.player.y == 0):
                    print ("Invalid move. Try again.")
                    continue
                self.player.move(self.player.x, self.player.y - 1)
            elif move == "a":
                if(self.player.x == 0):
                    print ("Invalid move. Try again.")
                    continue
                self.player.move(self.player.x - 1, self.player.y)
            elif move == "s":
                if(self.player.y == self.gameBoard.height - 1):
                    print ("Invalid move. Try again.")
                    continue
                self.player.move(self.player.x, self.player.y + 1)
            elif move == "d":
                if(self.player.x == self.gameBoard.width - 1):
                    print ("Invalid move. Try again.")
                    continue
                self.player.move(self.player.x + 1, self.player.y)
            elif move == "q":
                print ("Quitting game.")
                gameOver = True
            else:
                print ("Invalid move. Try again.")
            
            # Do everything resulting from a move
            print ("Player: " + str(self.player.x) + ", " + str(self.player.y))
            for enemy in self.enemies:
                print ("Enemy: " + str(enemy.x) + ", " + str(enemy.y))
                if self.player.x == enemy.x and self.player.y == enemy.y:
                    self.blobFight(self.player, enemy)
            # elif self.player.x == self.enemies[1].x and self.player.y == self.enemies[1].y:
            #     self.blobFight(self.player, self.enemies[1])
            
            # Remove defeated enemies from the board
            for idx, x in enumerate(self.enemies):
                if x.size == 0:
                    self.enemies.pop(idx)
                    break
                                
            # Lose condition
            if self.player.size == 0:
                gameOver = True
                self.printGameBoard()
                print("You lose.")
                break
            
            # Win condition
            enemySize = 0
            for enemy in self.enemies:
                enemySize += enemy.size
            if enemySize == 0:
                self.printGameBoard()
                print("You win!")
                break


    def end(self):
        pass

    def restart(self):
        pass


def main():
    print("Hello World!")
    gameManager = GameManager()
    gameManager.start()


if __name__ == "__main__":
    main()