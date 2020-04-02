from PlayerClass import PlayerClass
from settings import*

# initializing pygame
pygame.init()


# button class
class Button:

    def __init__(self, text, x, y, width, height, inactive_color, active_color, action=None):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.action = action

    def button(self, text, x, y, width, height, inactive_color, active_color, action=None):
        # current position of mouse cursor
        cur = pygame.mouse.get_pos()
        # when user clicks
        click = pygame.mouse.get_pressed()

        # when user hovers over button, it changes color
        if self.x + self.width > cur[0] > x and y + height > cur[1] > y:
            pygame.draw.rect(screen, active_color, (self.x, self.y, self.width, self.height))
            if click[0] == 1 and self.action != None:
                if action == "quit":
                    pygame.quit()
                    quit()

                # takes you to controls menu
                if action == "controls":
                    game.controls()
                # starts game and ends game intro
                if action == "play":
                    game.intro = False
                    game.newgame()
                # takes you to main menu
                if action == "main":
                    game.intro()

        else:
            pygame.draw.rect(screen, inactive_color, (self.x, self.y, self.width, self.height))

        text_to_button(text, black, self.x, self.y, width, height)


class GameClass:

    def __init__(self):
        pass

    # exit game
    def play(self, game_play=True):
        if not game_play:
            pygame.quit()
            quit()

    # game menu
    def intro(self, intro = True):

        while intro:
            # game exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.play(False)

            screen.fill(black)

            # displays text to screen
            message_to_screen("Welcome to the first build of my simple game", white, -100, "large")
            message_to_screen("For now you can only move and jump", white, -30, "small")

            # button objects
            button1.button("Play", 200, 500, 100, 50, blue, light_blue, action="play")
            button2.button("Controls", 550, 500, 100, 50, blue, light_blue, action="controls")
            button3.button("Quit", 900, 500, 100, 50, blue, light_blue, action="quit")

            pygame.display.update()
            clock.tick(fps)

    # controls menu
    def controls(self, gcont=True):

        while gcont:
            # game exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.play(False)

            screen.fill(black)
            message_to_screen("Controls", white, -100, "large")
            message_to_screen("Move left: 'A'  Move Right: 'D'  Jump: 'Space'", white, -30, "small")

            button1.button("Play", 200, 500, 100, 50, blue, light_blue, action="play")
            button2.button("Menu", 550, 500, 100, 50, blue, light_blue, action="main")
            button3.button("Quit", 900, 500, 100, 50, blue, light_blue, action="quit")

            pygame.display.update()
            clock.tick(fps)

    # start new game
    def newgame(self):

        self.intro = False

        # clicking x button event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.play(False)

        # variable that stores pressed keys
        keys = pygame.key.get_pressed()

        # move player left when 'a' is pressed
        if keys[pygame.K_a]:
            player.move(-player.velocity)
        # move player right when 'd' is pressed
        if keys[pygame.K_d]:
            player.move(player.velocity)

        # player jumping when space clicked
        if keys[pygame.K_SPACE]:
            player.jump(True)
        # player not jumping when space not clicked
        if not keys[pygame.K_SPACE]:
            player.jump(False)

        # checking window boundaries
        if player.x >= screen_width:
            player.x = screen_width
        if player.x <= player.width:
            player.x = player.width

        if player.y >= screen_height:
            player.y = screen_height
        if player.y <= 0:
            player.y = 0

        # background fill
        screen.fill(black)

        # drawing player to the screen
        pygame.draw.rect(screen, white, (player.x - player.height, player.y, player.width, player.height))

        # "printing" everything to the screen
        pygame.display.update()

        # running the game with fixed fps settings
        clock.tick(fps)


# defining text size function
def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "med":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


# printing text to button function
def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + (buttonwidth / 2)), (buttony + 10 + (buttonheight / 2)))
    screen.blit(textSurf, textRect)


# displaying text to the center of screen
def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (screen_width / 2), (screen_height / 2 + y_displace)
    screen.blit(textSurf, textRect)


# player object is created by giving it its starting position
player = PlayerClass(int(screen_width * 0.1), int(screen_height * 0.9))
game = GameClass()
# button object is created with: text, x and y position, x and y shift and colors
button1 = Button("Play", 200, 500, 100, 50, blue, light_blue, action="play")
button2 = Button("Controls", 550, 500, 100, 50, blue, light_blue, action="controls")
button3 = Button("Quit", 900, 500, 100, 50, blue, light_blue, action="quit")

game.intro()

while game.newgame():
    game.newgame()

pygame.quit()
quit()
