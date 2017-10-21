class player:


    def __init__(self,Name):
        self.HP = 15
        self.Interupt = 0
        self.Attack = 0
        self.cheers = 0
        self.Name = Name
    def turn(self,chatInput):
        self.Attack = 0
        self.counter = 0
        self.cheers = 0
        for chat in chatInput:
            chat = chat.lower()
            if chat == "attack" or chat == "atk":
                self.Attack = self.Attack + 1
            if chat == "heal":
                self.HP = self.HP + 2
            if chat == "int" or chat == "interupt":
                self.Interupt = self.Interupt + 1
            if chat == "cheers" or chat == "Cheers":
                self.cheer()
                self.cheers = self.cheers + 1




    def AttackPlayer(self,player):
        if player.cheers > 2:
            player.cheers = 0
            return
        self.Attack = self.Attack - (player.Interupt * 2)
        if self.Attack > 0:
            player.HP = player.HP - self.Attack
            print(player.HP)
        self.Attack = 0
        self.Interupt = 0

    def cheer(self):
       self.Attack = self.Attack * 2
       self.HP = self.HP + 5
       self.Interupt = self.Interupt + 5

