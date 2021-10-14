import pygame, sys
from content.settings import *
from content.imager import Imager
from content.player import Player
from content.enemy import Enemy

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()

        self.background = Imager(0, 0, screen_width, screen_height, "content/assets/Background.png")
        self.goal = Imager(970, 230, 32, 32, "content/assets/Goal.png")
    
        self.level = 1.0
        self.stage_reset()
    
    def stage_reset(self):
        self.player = Player(10, 230, 24, 32, "content/assets/Player2.png", 10)

        self.speed = 5 + (self.level * 0.3)

        if self.level >= 4.0:
            self.enemies = [
            Enemy(80, 230, 24, 32, "content/assets/entity.png", 10),
            Enemy(120, 230, 24, 32, "content/assets/entity.png", 10),
            Enemy(160, 230, 24, 32, "content/assets/entity.png", 10),
            Enemy(180, 230, 24, 32, "content/assets/entity.png", 10)
        ]

        elif self.level >= 2.0:
            self.enemies = [
            Enemy(120, 230, 24, 32, "content/assets/entity.png", 10),
            Enemy(160, 230, 24, 32, "content/assets/entity.png", 10),
        ]

        else:
            self.enemies = [
            Enemy(190, 230, 24, 32, "content/assets/entity.png", 10),
            ]


    

    
    def drawings(self):
        self.screen.fill('Black')
        self.screen.blit(self.background.image, (self.background.x, self.background.y))
        self.screen.blit(self.goal.image, (self.goal.x, self.goal.y))
        self.screen.blit(self.player.image, (self.player.x, self.player.y))

        for enemy in self.enemies:
            self.screen.blit(enemy.image, (enemy.x, enemy.y))







        pygame.display.update()
    
    def mover(self, player_direction):
        self.player.move(player_direction, screen_width)
        for enemy in self.enemies:
            enemy.move(screen_height)
    
    def check_collision(self):
        for enemy in self.enemies:
            if self.detect_collision(self.player, enemy):
                self.level = 1.0
                return True
        if self.detect_collision(self.player, self.goal):
            self.level += 0.5
            return True
        return False

    
    def detect_collision(self, object_1, object_2):
        if object_1.y < (object_2.y + object_2.height) and (
                object_1.y + object_1.height) > object_2.y and object_1.x < (object_2.x + object_2.width) and (
                object_1.x + object_1.width) > object_2.x:
            return True
        return False
    

    def run(self):

        player_direction = 0
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        player_direction = 1
                    if event.key == pygame.K_LEFT:
                        player_direction -= 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        player_direction = 0
            
            self.mover(player_direction)
            
            self.drawings()

            if self.check_collision():
                self.stage_reset()

            self.clock.tick(24)

game = Game()
game.run()
