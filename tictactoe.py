#tic tac toe
import pprint
import random


def is_winner(board):
	#top row
	if bc['tl'] == 'X' and bc['tm'] == 'X' and bc['tr'] == 'X':
		return(True,'X')
	elif bc['tl'] == 'O' and bc['tm'] == 'O' and bc['tr'] == 'O':
		return(True,'O')
	# middle row
	elif bc['ml'] == 'X' and bc['mm'] == 'X' and bc['mr'] == 'X':
		return(True,'X')
	elif bc['ml'] == 'O' and bc['mm'] == 'O' and bc['mr'] == 'O':
		return(True,'O')
	# bottom row
	elif bc['ll'] == 'X' and bc['lm'] == 'X' and bc['lr'] == 'X':
		return(True,'X')
	elif bc['ll'] == 'O' and bc['lm'] == 'O' and bc['lr'] == 'O':
		return(True,'O')
	# left column
	elif bc['tl'] == 'X' and bc['ml'] == 'X' and bc['ll'] == 'X':
		return(True,'X')
	elif bc['tl'] == 'O' and bc['ml'] == 'O' and bc['ll'] == 'O':
		return(True,'O')
	# middle column
	elif bc['tm'] == 'X' and bc['mm'] == 'X' and bc['lm'] == 'X':
		return(True,'X')
	elif bc['tm'] == 'O' and bc['mm'] == 'O' and bc['lm'] == 'O':
		return(True,'O')
	# right column
	elif bc['tr'] == 'X' and bc['mr'] == 'X' and bc['lr'] == 'X':
		return(True,'X')
	elif bc['tr'] == 'O' and bc['mr'] == 'O' and bc['lr'] == 'O':
		return(True,'O')
	# diagonal backslash
	elif bc['tl'] == 'X' and bc['mm'] == 'X' and bc['lr'] == 'X':
		return(True,'X')
	elif bc['tl'] == 'O' and bc['mm'] == 'O' and bc['lr'] == 'O':
		return(True,'O')
	# diagonal slash
	elif bc['tr'] == 'X' and bc['mm'] == 'X' and bc['ll'] == 'X':
		return(True,'X')
	elif bc['tr'] == 'O' and bc['mm'] == 'O' and bc['ll'] == 'O':
		return(True,'O')
	else:
		return(False,'')


def print_board():
	print('TIC TAC TOE')
	print(' ')
	print( bc['tl'], '|',  bc['tm'], '|',  bc['tr'])
	print('--+---+--')
	print(bc['ml'], '|',  bc['mm'], '|',  bc['mr'])
	print('--+---+--')
	print(bc['ll'], '|',  bc['lm'], '|',  bc['lr'])
	print(' ')

# tic tac toe initialization
bc = {'tl':' ', 'tm':' ', 'tr':' ', 'ml':' ', 'mm':' ', 'mr':' ', 'll':' ', 'lm':' ', 'lr':' '}
game_map = {'tl':'top left ', 'tm':'top middle ', 'tr':'top right ', 'ml':'middle left', 'mm':'middle middle', 'mr':'middle right ', 'll':'lower left ', 'lm':' lower middle', 'lr':'lower right '}

# game start
print('type the following letters for your turn')
for key, value in game_map.items():
	print(key, '=' , value)
# loop thru 9 turns
places = ['X','O']
p1 = places[random.randint(0,1)]
places.remove(p1)
p2 = places[0]
print('player1:',p1,'player2:',p2)
print(p1,'\'s turn')
turn = p1
num_move=0
print_board()
while num_move < 9:
	move = input('your move?')
	bc[move] = turn
	if turn == p1:
		turn = p2
	else:
		turn = p1

	num_move+=1
	print_board()
	# algorithm on who wins?
	winner, player = is_winner(bc)
	if winner:
		print('==================')
		print(' ', player,' wins!')
		print('==================')
		break

# algorithm on who wins?
winner, player = is_winner(bc)
if winner:
	print('==================')
	print(' ', player,' wins!')
	print('==================')
else:
	print('Fair and Square! Equal Share!')
