class PlayerClass:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 10
        self.width = 40
        self.height = 40
        self.isJump = False
        self.jumpCount = 10

    # handling player movement
    def move(self, velocity):
        self.x += velocity

    # player jump method
    def jump(self, isJump):
        if not self.isJump:
            self.isJump = isJump
        else:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10
