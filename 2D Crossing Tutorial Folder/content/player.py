from content.imager import Imager

class Player(Imager):
    def __init__(self, x, y, width, height, image_path, speed):
        super().__init__(x, y, width, height, image_path)

        # speed
        self.speed = speed
    
    def move(self, direction, max_width):

        if (self.x >= max_width - self.width and direction > 0) or (self.x == 0 and direction < 0):
            return

        self.x += (direction * self.speed)