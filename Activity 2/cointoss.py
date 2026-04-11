#
# cointoss.py - simulate tossing a coin multiple times
#
import random
coin = ['head', 'tail']
heads = 0
tails = 0
trials = int(input('Enter the number of tosses:...'))
print('\nCOIN TOSS\n')
for i in range(trials):
	if random.choice(coin) == 'head':
		heads += 1
	else:
		tails += 1
print('\nThere were ', heads, ' heads & ', tails, ' tails.\n')

