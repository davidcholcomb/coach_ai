import player
import random

class Big(Player):
        def __init__(self):
            self.speed = random.randint(65, 80)
            self.steal = random.rantint(5, 15)
            self.block = random.randint(5, 10)
            self.shooting_close = random.randint(90, 95)
            self.shooing_midrange = random.randint(30, 50)
            self.shooting3pts = random.randint(30, 40)
            self.stamina = random.randint(65,80)