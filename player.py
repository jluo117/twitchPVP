class player:

    def __init__(self,name):
        self.HP = 1
        self.Interupt = 0
        self.Attack = 0
        self.Name = name
    def turn(self,chatInput):
        self.Interupt = 0
        self.Attack = 0

    def _init_(self,Name):
        self.HP = 1
        self.counter = 0
        self.Attack = 0
        self.Name = name
    def turn(self,chatInput):
        for chat in chatInput:
            if chat == "attack" or chat == "Attack":
                self.Attack = self.Attack + 1
            if chat == "heal" or chat == "Heal":
                self.HP = self.HP + 2
            if chat == "int" or chat == "interupt":
                self.Interupt = self.Interupt + 1
	    if chat == "cheers" or chat == "Cheers"
		self.cheers



    def AttackPlayer(self,player):
        self.Attack = self.Attack - (player.Interupt * 2)
        if self.Attack > 0:
            player.HP = player.HP - self.Attack
        self.Attack = 0
        self.Interupt = 0

   def cheers(self):
	self.Attack = self.Attack * 2
	self.HP = self.HP + 5
	self.Interrupt = self.Interrupt + 5
	
