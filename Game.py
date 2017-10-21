from player import player
class Game:
    def __init__(self,player1Name,player2Name):
        self.player1 = player(player1Name)
        self.player2 = player(player2Name)
        self.stream1Chat = []
        self.stream2Chat = []
        self.Winner = None

    def validSize(self):
        if len(self.stream1Chat) > 16 and len(self.stream2Chat) > 16:
            return True
        return False
    def turn(self):
        self.player1.turn(self.stream1Chat)
        self.player2.turn(self.stream2Chat)
        self.stream1Chat = []
        self.stream2Chat = []
        self.player1.AttackPlayer(self.player2)
        self.player2.AttackPlayer(self.player1)
        if self.player1.HP <= 0 and self.player2.HP <= 0:
            if self.player1.HP < self.player2.HP:
                self.Winner = self.player2
                return self.player2.Name + " wins"
            else:
                self.Winner = self.player1
                return self.player1.Name + " wins"
        if self.player1.HP <= 0:
            self.Winner = self.player2
            return self.player2.Name + " wins"
        if self.player2.HP <= 0:
            self.Winner = self.player1
            return self.player1.Name + " wins"
        return "Keep fighting " + self.player1.Name + ' '+ str(self.player1.HP) + " hp " + self.player2.Name + ' '+ str(self.player2.HP) + " hp "







