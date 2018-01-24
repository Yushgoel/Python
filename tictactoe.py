board = []
p1inputrow = -1
p1inputcolom = -1
p2inputrow = -1
p2inputcolom = -1
count = 0 
breakornot = False

for x in range(3):
    board.append(["_"] * 3)

def print_board(boardv):
    for row in boardv:
        print " ".join(row)

def check():
	count = 0
	p1rcount = 0
	p1c1count = 0
	p1c2count = 0
	p1c3count = 0
	p2rcount = 0
	p2c1count = 0
	p2c2count = 0
	p2c3count = 0
	breakornot = False
	for i in board:

		for col in i:
#			print "******col %s" % col

			if count % 3 == 0:
				p1rcount = 0
				p2rcount = 0
				if col == "O":
					p1rcount += 1
					p1c1count += 1
#					print "p1 col 1increment"
				elif col == "X":
					p2rcount += 1
					p2c1count += 1
#					print "p2 col2 increment"
			elif count % 3 == 1:
				if col == "O":
					p1rcount += 1
					p1c2count += 1
#					print "p1 col 2 increment"
				elif col == "X":
					p2rcount += 1
					p2c2count += 1
#					"print p2 col 2 1increment"
			else:
				if col == "O":
					p1rcount += 1
					p1c3count += 1
#					print "p1 col 3 increment"
				elif col == "X":
					p2rcount += 1
					p2c3count += 1
#					print "p2 col 3 increment"
#			print "p1rcount %s, p" %p1rcount 
#			print "p2rcount %s, p" %p2rcount

			if p1rcount == 3 or p1c3count == 3 or p1c2count == 3 or p1c1count == 3:
				print "player 1 wins."
				return True;
				breakornot = True
				break
			elif p2rcount == 3 or p2c3count == 3 or p2c2count == 3 or p2c1count == 3:
				print "player 2 wins."
				return True;
				breakornot = True
				break
			count += 1
	return False;

def diagnol(xoro, p1p2):
	if board[0][0] == xoro and board[1][1] == xoro and board[2][2] == xoro:
		print p1p2
		return True;
	elif board[0][2] == xoro and board[1][1] == xoro and board[2][0] == xoro:
		print p1p2
		return True;

#***************************************************************************************

def position_check(xoro):
	
	if xoro == "O":
		p1inputrow = int(raw_input("p1 please enter row number ")) - 1
		p1inputcolom = int(raw_input("p1 please enter coloum number ")) - 1
		if p1inputrow > 2 or p1inputcolom > 2:
			print "pick a spot inside the board"
			p1inputrow = int(raw_input("p1 please enter row number ")) - 1
			p1inputcolom = int(raw_input("p1 please enter coloum number ")) - 1
			if board[p1inputrow][p1inputcolom] == "_":
				board[p1inputrow][p1inputcolom] = "O"
			else:
				print "turn skipped"
		elif board[p1inputrow][p1inputcolom] == "_":
			board[p1inputrow][p1inputcolom] = "O"
		else:
			print "pick an empty spot."
			p1inputrow = int(raw_input("p1 please enter row number ")) - 1
			p1inputcolom = int(raw_input("p1 please enter coloum number ")) - 1
			if board[p1inputrow][p1inputcolom] == "_":
				board[p1inputrow][p1inputcolom] = "O"
			else:
				print "turn skipped"
	else:
		p2inputrow = int(raw_input("p2 please enter row number ")) - 1
		p2inputcolom = int(raw_input("p2 please enter coloum number ")) - 1
		if p2inputrow > 2 or p2inputcolom > 2:
			print "pick a spot inside the board"
			p2inputrow = int(raw_input("p2 please enter row number ")) - 1
			p2inputcolom = int(raw_input("p2 please enter coloum number ")) - 1
			if board[p2inputrow][p2inputcolom] == "_":
				board[p2inputrow][p2inputcolom] = "X"
		elif board[p2inputrow][p2inputcolom] == "_":
			board[p2inputrow][p2inputcolom] = "X"
		else:
			print "pick an empty spot."
			p2inputrow = int(raw_input("p2 please enter row number ")) - 1
			p2inputcolom = int(raw_input("p2 please enter coloum number ")) - 1
			if board[p2inputrow][p2inputcolom] == "_":
				board[p2inputrow][p2inputcolom] = "X"
			else:
				print "turn skipped"

#**********************************************************************************

print_board(board)

for i in range(4):
	
	position_check("O")
	print_board(board)
	breakornot = check()

	if breakornot == False:
		breakornot = diagnol("O", "Player 1 wins!")
	if breakornot == True:
		break
	
	position_check("X")
	
	print_board(board)
	breakornot = check()
	if breakornot == False:
		breakornot = diagnol("X", "Player 2 wins!")
	if breakornot == True:
		break 
	

if breakornot == True:
	print "Game over"
else:
	position_check("O")
	print "***********"
	print_board(board)
	check()