class player:
    def __init__(self,name):
        self.HP = 1
        self.Interupt = 0
        self.Attack = 0
        self.Name = name
    def turn(self,chatInput):
        self.Interupt = 0
        self.Attack = 0
        for chat in chatInput:
            if chat == "attack" or chat == "Attack":
                self.Attack = self.Attack + 1
            if chat == "int" or chat == "interupt":
                self.Interupt = self.Interupt + 1
            if chat == "heal" or chat == "Heal":
                self.HP = self.HP + 2

    def AttackPlayer(self,player):
        self.Attack = self.Attack - (player.Interupt * 2)
        if self.Attack > 0:
            player.HP = player.HP - self.Attack
        self.Attack = 0
        player.Interupt = 0




