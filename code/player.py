
#https://pythonspot.com/jump-and-run-in-pygame/
class Player:
    def __init__(self):
            
        self.team = team
        self.player_name = player_name
    
class Guard(Player):
        def __init__(self):
            self.max_speed = random.randint(75, 95)
            self.steal = random.rantint(20, 35)
            self.block = random.randint(10, 40)
            self.shooting_close = random.randint(80, 95)
            self.shooing_midrange = random.randint(40, 60)
            self.shooting3pts = random.randint(30, 45)
            self.stamina = random.randint(70,95)

class Wing(Player):
        def __init__(self):
            self.speed = random.randint(80, 90)
            self.steal = random.rantint(20, 30)
            self.block = random.randint(20, 50)
            self.shooting_close = random.randint(85, 95)
            self.shooing_midrange = random.randint(40, 60)
            self.shooting3pts = random.randint(35, 45)
            self.stamina = random.randint(70,95)

class Big(Player):
        def __init__(self):
            self.speed = random.randint(65, 80)
            self.steal = random.rantint(5, 15)
            self.block = random.randint(5, 10)
            self.shooting_close = random.randint(90, 95)
            self.shooing_midrange = random.randint(30, 50)
            self.shooting3pts = random.randint(30, 40)
            self.stamina = random.randint(65,80)