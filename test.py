#testing function
import random


isPoint = False
odds = False
thePoint = 0
myMoney = 1000
onTheTable = 0


bets = [0, 0]



def diceTest():
	for die in range(1):
		dieOne = random.randint(1,6)
		dieTwo = random.randint(1,6)
		throw = dieOne + dieTwo
		
		return throw, dieOne, dieTwo




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




def placeBetTest():
	global bets
	while True:
		#Come out bet
		game = input('\nBet:\nlight | dark | both?')

		if isPoint == False:
			odds = 0
		else:
			odds = True

		if game == 'light':
			bets[0] = passline()
			print('newPassline is ' + str(bets[0]))
		elif game == 'dark':
			bets[1] = dontPassline()
		elif game == 'both':
			bets[0] = passline()
			bets[1] = dontPassline()

		#place = input('\nf = field | h = horn | w = world \nfh = fireBetHigh | fb = fl = fireBetLow | f = fireBetAll ')
		else:
			False
		print('Passline bet is ' + str(bets[0]) + ' DontPassline bet is ' + str(bets[1]))
		return bets

	betType = input('') 

def playTest():
	global bets
	global myMoney
	global onTheTable
	global thePoint
	newBets = bets
	while True:
		if isPoint == True:
			print('the point is ' + str(thePoint))
		while True:
			

			print("\n"+ "*"*15)
			print("ENTER = Roll")
			print("y = place a bet")
			print("q = walk")
			print("s = stats")
			print("t = take bet")
			print("*"*15)
			input_ = input('').strip()

			#TODO: Walk Away q 
			if input_ == 'q':
				break

			elif input_ == 'y':
				newBets = placeBetTest()

			#Stats s
			elif input_ == 's':
				print("\nYou have " + str(myMoney) + 'in the bank')
				print('You have' + str(onTheTable) + 'on the table')

			#TODO: Take bets t
			elif input_ == 't':
				break

			else:
				break

		if isPoint == True:
			print('the point is ' + str(thePoint))

		throw = diceTest()

		print('Throw: %s\nDie One: %s | Die Two: %s' % (throw[0], throw[1], throw[2]))
		print('\nBets are:\nPassline- %s DontPassline- %s' % (newBets[0], newBets[1]))


		





playTest()