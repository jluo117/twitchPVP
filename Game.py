from player import player
class Game:
    def __init__(self,player1Name.player2Name):
        player1 = player(player1Name)
        player2 = player(player2Name)
        Winner = None

    def turn(self,streamer1Chat,streamer2Chat):
        player1.turn(streamer1Chat,player1)
        player2.turn(streamer2Chat,player2)
        player1.Attack(player2)
        player2.Attack(player1)
        if player1.HP <= 0 and player2.HP <= 0:
            if player1.HP < player2.HP:
                Winner = player2
                return player2.Name + "wins"
            else:
                Winner = player1
                return player1.Name + "wins"
        if player1.HP <= 0:
            Winner = player2
            return player2.Name + "wins"
        if player2.HP <= 0:
            Winner = player1
            return player1.Name + "wins"
        return "Keep fighting"







