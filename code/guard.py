import player
import random

class Guard(Player):
        def __init__(self):
            self.max_speed = random.randint(75, 95)
            self.steal = random.rantint(20, 35)
            self.block = random.randint(10, 40)
            self.shooting_close = random.randint(80, 95)
            self.shooing_midrange = random.randint(40, 60)
            self.shooting3pts = random.randint(30, 45)
            self.stamina = random.randint(70,95)