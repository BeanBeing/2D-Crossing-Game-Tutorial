from content.imager import Imager

class Enemy(Imager):
    def __init__(self, x, y, width, height, image_path, speed):
        super().__init__(x, y, width, height, image_path)

        self.speed = speed
    
    def move(self, max_height):
        if self.y <= 0:

            self.speed = abs(self.speed)
        
        elif self.y >= max_height - self.height:
            self.speed = -self.speed
        
        self.y += self.speed