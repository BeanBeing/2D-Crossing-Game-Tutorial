import pygame


class Imager:
    def __init__(self, x, y, width, height, image_path):

        # grabs the image
        image = pygame.image.load(image_path)

        # scales the image it grabbed
        self.image = pygame.transform.scale(image, (width, height))

        self.x = x
        self.y = y
        self.width = width
        self.height = height