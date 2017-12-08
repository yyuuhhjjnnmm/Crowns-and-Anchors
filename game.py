from random import *

def main():
	#Counter for the number of rounds
	round_count = 1

	#Buffer for the output file
	f = open('output.txt','w')

	#Starting.
	print("Welcome to the Game.")

	#Getting number of players
	plys = input("How many players?")
	player_count = int(plys)

	#Initializing the players at 10 dollars
	player_list = []
	for i in range(0, player_count):
		player_list.append(Player(i,10,[]))

	#Looping the game while the game is not over
	while(not game_over(player_list)):

		#Betting stage
	      print("\nBetting stage.")
	      for i in range(0, player_count):
		      print("\nPlayer ",(i + 1)," is betting.")
		      #Skip round option
		      skip = input("Skip round? (y/n)")

			#Auto skip for not enough money
		      if(player_list[i].money <= 0):
			      print("Player does not have enough money. Auto skip the betting stage.")
			      skip= "y"

			#Actual betting
		      while(skip == "n"):

			      #Getting symbol
			      print("\nPossible symbols to bet on:")
			      print("hearts,spades,diamonds,clubs,crowns,anchors")
			      sy = input("Which symbol do you want to bet on?")

			      if not (sy == "hearts" or sy == "spades" or sy == "diamonds" or sy == "clubs" or sy == "crowns" or sy =="anchors"):
				      #Error cathing
				      print("Not a valid symbol. Betting skipped")
			      else:
				#Getting amount
				      print("Possible amount to bet:")
				      print("1,2,5,10")
				      amount = input("How much do you want to bet?")
				#Checking for money
			      if (int(amount) > player_list[i].money):
				      print("Not enough money. Betting skipped")
			      else:
				      #Making bet
				      player_list[i].bets.append(Bet(sy,amount))
				      player_list[i].money -= amount
				      print("Bet made.")
				#Checking for more bets
			      skip = input("Finish betting? (y/n)")

	      print("\nBetting Completed.")
	      print("Spinning the wheel...\n")

		#Generate the slot
	      slot = Slot(translate_sym(randrange(1,7)),translate_sym(randrange(1,7)),translate_sym(randrange(1,7)))
	      print("\nThe winning slot is: ", slot.sy1, " | ", slot.sy2, " | ", slot.sy3)#Printing out the winning slot

		#Printing and calculating payouts
	      print("\nHere are the payouts:")
	      for i in range(0,player_count):
	      		print("Player",(i+1), " won a payout of: $", player_list[i].check(slot))

		#Writing results to output file
	      print("\nWriting results....")
	      print("Round ", round_count, file=f)
	      for i in range(0,player_count):
	      		print("Player",(i+1), " $", player_list[i].money, file = f)
	      print("\n",file=f)

		#Printing out the updated money
	      print("\nUpdated money for players:")
	      for i in range(0,player_count):
	      		print("Player",(i+1), " $", player_list[i].money)
	      		
			#Resetting the bets for each player
	      		del player_list[i].bets[:]

	      	#Updating the rounds	
	      round_count +=1

	#end of game
	print("All players are out of money.\nThanks for playing.")



class Player(object):
	def __init__(self,n,m,b):
		self.number = n
		self.money = m
		self.bets = b

		
	   #Function to check the payouts of the winning slots
	def check(self,winningSlot):
		payout = 0

		#Checking each bet against winning slot
		for i in range(len(self.bets)):
			if (winningSlot.syCount(self.bets[i].symbol) == 3 and self.bets[i].symbol == "anchors"):
				print("Winners On Anchors -- Ahoy!!!!")
		
			payout += winningSlot.syCount(self.bets[i].symbol) * int(self.bets[i].amount) #winnings
			if (winningSlot.syCount(self.bets[i].symbol) > 0):
				payout += int((self.bets[i]).amount)#Paying back initial bet if won

		self.money += int(payout)#Update the money of player
		return payout #Output payout

class Bet(object):
	def __init__(self,symbol,amount):
		self.symbol = symbol
		self.amount = amount

	
class Slot(object):
	def __init__(self,sy1,sy2,sy3):
		self.sy1 = sy1
		self.sy2 = sy2
		self.sy3 = sy3

		#Function for checking if player won the bet
	def syCount(self,symbol):
		count = 0

		if (self.sy1 == symbol):
			count += 1

		if (self.sy2 == symbol):
			count += 1

		if (self.sy3 == symbol):
			count += 1

		return count

	#Translation function for randomly generating slots
def translate_sym(num):
	if (num == 1):
		return "hearts"
	elif (num == 2):
		return "spades"
	elif (num == 3):
		return "diamonds"
	elif (num == 4):
		return "clubs"
	elif (num == 5):
		return "crowns"
	elif (num == 6):
		return "anchors"

	#Function to check for game over
def game_over(player_list):
	for i in range(0,len(player_list)):
		if (player_list[i].money > 0) :
			return False
	#if everyone is broke then we finished
	return True

if __name__ == "__main__":
	main()
		
