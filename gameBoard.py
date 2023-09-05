class GameBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print(self, player, enemies):
        for i in range(self.height):
            for j in range(self.width):
                loopBreak = False
                print ("|", end="")
                # TODO - Having enemies print first results in X3P0 due to nesting. Fix.
                if player.x == j and player.y == i:
                    print("P" + str(player.size), end="")
                    continue
                for enemy in enemies:
                    if enemy.x == j and enemy.y == i:
                        print("X" + str(enemy.size), end="")
                        loopBreak = True
                        continue
                if loopBreak is False:
                    print("--", end="")
                
            print("")

    def isValidMove(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        return True