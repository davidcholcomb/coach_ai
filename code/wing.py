import player
import random

class Wing(Player):
        def __init__(self):
            self.speed = random.randint(80, 90)
            self.steal = random.rantint(20, 30)
            self.block = random.randint(20, 50)
            self.shooting_close = random.randint(85, 95)
            self.shooing_midrange = random.randint(40, 60)
            self.shooting3pts = random.randint(35, 45)
            self.stamina = random.randint(70,95)