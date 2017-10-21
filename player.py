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
        self.HP = 1000
        self.counter = 0
        self.Attack = 0
        self.Name = name
    def turn(chatInput):
HP = self.HP + 2


    def AttackPlayer(self,player):
        self.Attack = self.Attack - (player.Interupt * 2)
        if self.Attack > 0:
            player.HP = player.HP - self.Attack

        self.Attack = 0
        player.counter = 0
    def chair(self):
	self.Attack = self.Attack + 3;
	self.hp = self.hp * 1.2;
	self.counter = self.counter * 1.2;
    def interupt(player):
	if player.chat == "attack"
	    player.hp = player.hp - (0.3 * player.attack)
	    player.attack = 0;
	else
	    self.interupt = 0

