import time
used = {}
freq = 5
class player:
    def _init_(self,Name):
        self.HP = 1000
        self.counter = 0
        self.Attack = 0
        self.Name = name
	self.command = None
	
    def turn(chatInput):
        for chat in chatInput:
            if chat == "attack" or chat == "Attack":
                self.Attack = self.Attack + 1
		self.command = "attack"
            if chat == "counter" or chat == "Counter":
                self.counter = self.counter + 1
		self.command = "counte"r
            if chat == "heal" or chat == "Heal":
                self.HP = self.HP + 2
		self.command = "heal"
	
    def call_command(command):
	if(self.command == "heal" or self.command == "counter"):
	print("Calling command '%s'." % self.command)
	
	 
    def Attack(player):
        self.Attack = self.Attack - (player.counter * 2)
        player.hp = player.HP - self.Attack
        self.Attack = 0
        player.counter = 0
    def chair(self):
	self.Attack = self.Attack + 3;
	self.hp = self.hp * 1.2;
	self.counter = self.counter * 1.2;
    def counter(player):
	if player.chat == "attack"
	    player.hp = player.hp - (0.3 * player.attack)
	    player.attack = 0;
	else
	    self.counter = 0
   def cooldown(self):
	if(chat == "heal" or chat == "Heal"):
 	  print("You have used the command Heal in the last %u seconds." % (chat, freq))
	else:
	  print("You have used the command Counter in the last %u seconds" % (chat, freq))
   def process_command(command)
	if(
	   command not in used or
	   time.time() - used[command] > freq
	
):
	used[command] = time.time()
 	call_command(command)

	else:
		cooldown(command)

