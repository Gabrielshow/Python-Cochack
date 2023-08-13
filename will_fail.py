#simple python game
class Goblin(Gameobjects):
    def _init_(self, name):
        self.class_name = "goblin"
        self.health = 3
        self._desc = "A foul creature"
        
    super()._init_(name)
    
    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            
    