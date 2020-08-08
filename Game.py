import sys
import pygame
from Settings import Settings


class Game:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("COVID: The Escape")
        self.font = pygame.font.Font('Raleway-Black.ttf', 50)
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.bot1_x = 5
        self.bot1_y = 755
        self.bot2_x = 1150
        self.bot2_y = 5
        self.character_x = 600
        self.character_y = 400

    def run_game(self):
        while True:
            self.screen.fill(self.settings.background_color)
            pygame.draw.rect(self.screen, (119, 119, 156), (self.character_x, self.character_y, 30, 30))
            pygame.draw.rect(self.screen, (230, 88, 83), (self.bot1_x, self.bot1_y, 30, 30))
            pygame.draw.rect(self.screen, (230, 88, 83), (self.bot2_x, self.bot2_y, 30, 30))
            self.key_press()
            self.character_movement()
            self.bot1_movement()
            self.bot2_movement()
            if self.character_x - 5 < self.bot1_x < self.character_x + 5 and self.character_y - 5 < self.bot1_y < self.character_y + 5:
                self.moving_left = False
                self.moving_right = False
                self.moving_up = False
                self.moving_down = False
                self.bot1_x = 5
                self.bot1_y = 755
                self.bot2_x = 1150
                self.bot2_y = 5
                self.character_x = 600
                self.character_y = 400
                self.end()
                break

            if self.character_x - 5 < self.bot2_x < self.character_x + 5 and self.character_y - 5 < self.bot2_y < self.character_y + 5:
                self.moving_left = False
                self.moving_right = False
                self.moving_up = False
                self.moving_down = False
                self.bot1_x = 5
                self.bot1_y = 755
                self.bot2_x = 1150
                self.bot2_y = 5
                self.character_x = 600
                self.character_y = 400
                self.end()
                break
            
            pygame.display.update()

    def character_movement(self):
        if self.moving_right and (self.character_x + 30) < 1200:
            self.character_x += 1.5
        if self.moving_left and self.character_x >= 0:
            self.character_x -= 1.5
        if self.moving_up and self.character_y >= 0:
            self.character_y -= 1.5
        if self.moving_down and (self.character_y + 30) < 800:
            self.character_y += 1.5

    def bot1_movement(self):
        if self.character_x > self.bot1_x:
            self.bot1_x += .3
        elif self.character_x < self.bot1_x:
            self.bot1_x -= .3
        if self.character_y > self.bot1_y:
            self.bot1_y += .3
        elif self.character_y < self.bot1_y:
            self.bot1_y -= .3

    def bot2_movement(self):
        if self.character_x > self.bot2_x:
            self.bot2_x += .5
        elif self.character_x < self.bot2_x:
            self.bot2_x -= .5
        if self.character_y > self.bot2_y:
            self.bot2_y += .5
        elif self.character_y < self.bot2_y:
            self.bot2_y -= .5

    def key_press(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.moving_left = True
                elif event.key == pygame.K_DOWN:
                    self.moving_down = True
                elif event.key == pygame.K_UP:
                    self.moving_up = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.moving_left = False
                elif event.key == pygame.K_DOWN:
                    self.moving_down = False
                elif event.key == pygame.K_UP:
                    self.moving_up = False

    def menu(self):
        text = self.font.render('COVID: The Escape', True, (0, 0, 0), (255, 255, 255))
        text1 = self.font.render('STAY 6 feet away from the germs!!!', True, (0, 0, 0), (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (self.settings.screen_width // 2, self.settings.screen_height // 2)
        while True:
            self.screen.fill((255, 255, 255))
            self.screen.blit(text, text_rect)
            click = pygame.mouse.get_pressed()
            mouse_position = pygame.mouse.get_pos()
            if 550 < mouse_position[0] < 650 and 470 < mouse_position[1] < 520:
                pygame.draw.rect(self.screen, (0, 0, 0),
                                 (self.settings.screen_width // 2 - 50, self.settings.screen_height // 2 + 70, 100, 50))
                if click[0] == 1:
                    self.run_game()
                    break
            else:
                pygame.draw.rect(self.screen, (100, 130, 100),
                                 (self.settings.screen_width // 2 - 50, self.settings.screen_height // 2 + 70, 100, 50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()

    def end(self):
        text = self.font.render("OOPS!", True, (0, 0, 0), (255, 255, 255))
        text_1 = self.font.render("You didn't keep a safe distance from the germs.", True, (0, 0, 0), (255, 255, 255))
        text_2 = self.font.render("Remember 6 FEET, Try Again:", True, (0, 0, 0), (255, 255, 255))
        text_rect = text.get_rect()
        text_1_rect = text_1.get_rect()
        text_2_rect = text_2.get_rect()
        text_2_rect.center = (600, 400)
        text_1_rect.center = (600, 350)
        text_rect.center = (600, 300)
        while True:
            self.screen.fill((255, 255, 255))
            self.screen.blit(text, text_rect)
            self.screen.blit(text_1, text_1_rect)
            self.screen.blit(text_2, text_2_rect)
            click = pygame.mouse.get_pressed()
            mouse_position = pygame.mouse.get_pos()
            if 550 < mouse_position[0] < 650 and 470 < mouse_position[1] < 520:
                pygame.draw.rect(self.screen, (0, 0, 0),
                                 (self.settings.screen_width // 2 - 50, self.settings.screen_height // 2 + 70, 100, 50))
                if click[0] == 1:
                    self.run_game()
                    break
            else:
                pygame.draw.rect(self.screen, (100, 130, 100),
                                 (self.settings.screen_width // 2 - 50, self.settings.screen_height // 2 + 70, 100, 50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()



if __name__ == '__main__':
    g = Game()
    g.menu()




