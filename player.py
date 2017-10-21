class player:
    def _init_(self):
        self.HP = 100
        self.interupt = 0
    def turn(chatInput,player):
        attack = 0
        for chat in chatInput:
            if chat == "attack" or chat == "Attack":
                attack = attack + 1
            if chat == "int" or chat == "interupt":
                self.interupt = self.interupt + 1
            if chat == "heal" or chat == "Heal":
                self.HP = self.HP + 2
        self.GetAttack(player)



