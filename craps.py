import random

#this program simulates craps
print("\n"+ "*"*100)
print("You walk into a room filled with smokey air and dark figures. \
	\nA jovial hefty man with a red beard waves you to come play at the table.")
print('He slides you the dice and gestures for you to make your bet')
print("\n"+ "*"*100)

myMoney = 1000
onTheTable = 0

isPoint = False 
thePoint = 0
roll = 0


pay = 1

#counts stats for throws
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0
sevens = 0
eights = 0
nines = 0
tens = 0 
elevens = 0
twelves = 0

rollCount = 0

#TODO: Stat Tracking
def throwTracker():
	for x in range(throws):
		print

	print()

#TODO: BET LISTER
'''
	for i in bets:
		print i
'''
#Rolls Dice
def throwDice():
	for die in range(1):
		dieOne = random.randint(1,6)
		dieTwo = random.randint(1,6)
		throw = dieOne + dieTwo
		return throw, dieOne, dieTwo





	print("You have " + str(myMoney) + 'in the bank')
	print('You have' + str(onTheTable) + 'on the table')
	print('the point is ' + str(point))
	print("\n"+ "*"*15)
	print("ENTER = Roll")
	print("y = bet")
	#print("c = current bets")
	print("q = walk")
	print("*"*15)


#***************************************************************************************************
#All the types of bets 
betPassline = 0
betDontPassline = 0
betField = 0

def placeBet():
	while True:
		#Come out bet
		yn = input('Place a bet?')
		if yn.strip() =='y':
			game = input('\nBet:\nlight | dark | both?')

			if isPoint == False:
				odds = 0
			else:
				odds = True

			if game == 'light':
				bets[0] == passline()
			elif game == 'dark':
				bets[1] = dontPassline()
			elif game == 'both':
				bets[0] = passline()
				bets[1] = dontPassline()

			

			#place = input('\nf = field | h = horn | w = world \nfh = fireBetHigh | fb = fl = fireBetLow | f = fireBetAll ')
		else:
			False

		return bets

def passline():
	global myMoney
	betPassline = int(input('How much? '))
	myMoney = myMoney - betPassline
	return betPassline

def dontPassline():
	global myMoney
	betDontPassline = int(input('How much? '))
	myMoney = myMoney - betDontPassline
	return betDontPassline

def theTop(t_):
	global isPoint 
	global thePoint
	top = [4,5,6,8,9,10]

	if t_ in top:
		isPoint = True
		thePoint = t_
		return isPoint, thePoint 

def field():
	win = [2,3,4,9,10,11,12]
	#Triple payout
	if roll == 12:
		pay = 3
	if roll == 2:
		pay = 2

#def horn():
	

#def fireBetHigh():
	
#def fireBetLow():
	
#def fireBetAll():
	
#****************************************************************************************************

#Start game
def playCraps():
	global bets
	global myMoney
	global onTheTable
	try:
		while True:
			throw = throwDice()
			newBets = placeBet(isPoint)
			print('Throw: %s\nDie One: %s | Die Two: %s' % (throw[0], throw[1], throw[2]))
			print('\nBets are:\n Passline- %s Dont Passline- %s' % (newBets[0], newBets[1]))
	except KeyboardInterrupt:
		# Handle the Ctrl-C exception to keep its error message from displaying.	
		if onTheTable != 0:
			myMoney = myMoney + onTheTable - betPassline
			onTheTable = 0
			print('\nDone.')



#Initiates Game
playCraps()
