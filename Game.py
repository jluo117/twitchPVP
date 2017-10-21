from player import player
class Game:
    def __init__(self):
        player1 = player()
        player2 = player()
        winner = None

    def turn(self,streamer1,streamer2):
        player1.turn(streamer1,player2)
        player2.turn(streamer2,player2)
        if player1.HP <= 0:
            Winner = player2
            return player2.name + "is the winner"
        if player2.HP <= 0:
            Winner = player1
            return player1.name + "is the winner"
        return "Keep on fighting for the true champ"








