class player:


    def __init__(self,Name):
        self.HP = 12
        self.Interupt = 0
        self.Attack = 0
        self.Name = Name
    def turn(self,chatInput):
        self.Attack = 0
        self.counter = 0
        for chat in chatInput:
            chat = chat.lower()
            if chat == "attack" or chat == "atk":
                self.Attack = self.Attack + 1
            if chat == "heal":
                self.HP = self.HP + 2
            if chat == "int" or chat == "interupt":
                self.Interupt = self.Interupt + 1



    def AttackPlayer(self,player):
        self.Attack = self.Attack - (player.Interupt * 2)
        if self.Attack > 0:
            player.HP = player.HP - self.Attack
            print(player.HP)
        self.Attack = 0
        self.Interupt = 0
