class player:
    def _init_(self,Name):
        self.HP = 1000
        self.Interupt = 0
        self.Attack = 0
        self.Name = name
    def turn(chatInput,target):
        for chat in chatInput:
            if chat == "attack" or chat == "Attack":
                self.Attack = self.Attack + 1
            if chat == "int" or chat == "interupt":
                self.Interupt = self.Interupt + 1
            if chat == "heal" or chat == "Heal":
                self.HP = self.HP + 2

    def Attack(player):
        self.Attack = self.Attack - (player.Interupt * 2)
        player.hp = player.HP - self.Attack
        self.Attack = 0
        player.Interupt = 0





