# -*- coding: utf-8 -*-
"""
Created on 19/05/2018

@author: Raphaël
"""
class Game:
	""" Play a game of Connect Four. """


	def __init__( self, ai ):

		self.count_ai_moves = 0
		self.last_move_human = 0

		self._init_field()

	def _init_field( self ):

		self.board = ny.array( [[0] * 6] * 7 )
		self.current_height = [0] * 7
		
        def check_board_full( self ):
		if ny.shape( ny.where( self.board == STONE_BLANK ) )[1] == 0:
			return True
		return False

	def _count_stones( self, column, row, stone, blank, ai, human ):
		""" Compares the value of the found stone with the existing stone types.
		Sets a stop flag if it is not possible anymore for either the human or the AI
		to connect enough stones.
		Returns a tuple in the form: ( position of a blank field, #ai, #human, flag_to_stop ).
		"""

		flag_stop = False

		if stone == 0:
			# No danger/chance if there is more than one blank field in range
			if blank != -1: flag_stop = True
			# Save blank field. This is a candidate to place the stone.
			else: blank = { "col": column, "row": row }
		elif stone == -1:
			# If there has been at least one human stone already,
			# it is not possible for AI stones to have a connection of three and a blank field available.
			if human > 0: flag_stop = True
			else: ai += 1
		elif stone == 1:
			# Same here, vice versa.
			if ai > 0: flag_stop = True
			else: human += 1

		return ( blank, ai, human, flag_stop )

	def _count_stones_up( self, x, y ):
		""" From position (x,y) count the types of the next stones upwards. """

		blank, ai, human = -1, 0, 0

		if y + CONNECT <= FIELD_HEIGHT:
			for i in range( CONNECT ):
				col, row = x, y + i
				stone = self.board[col][row]
				blank, ai, human, flag_stop = self._count_stones( col, row, stone, blank, ai, human )
				if flag_stop: break

		return ( blank, ai, human )

	def _count_stones_right( self, x, y ):
		""" From position (x,y) count the types of the next stones to the right. """

		blank, ai, human = -1, 0, 0

		if x + CONNECT <= FIELD_WIDTH:
			for i in range( CONNECT ):
				col, row = x + i, y
				stone = self.board[col][row]
				blank, ai, human, flag_stop = self._count_stones( col, row, stone, blank, ai, human )
				if flag_stop: break

		return ( blank, ai, human )

	def _count_stones_rightup( self, x, y ):
		""" From position (x,y) count the types of the next stones diagonal right up. """

		blank, ai, human = -1, 0, 0

		if x + CONNECT <= FIELD_WIDTH and y + CONNECT <= FIELD_HEIGHT:
			for i in range( CONNECT ):
				col, row = x + i, y + i
				stone = self.board[col][row]
				blank, ai, human, flag_stop = self._count_stones( col, row, stone, blank, ai, human )
				if flag_stop: break

		return ( blank, ai, human )

        def _count_stones_rightdown( self, x, y ):
		""" From position (x,y) count the types of the next stones diagonal right down. """

		blank, ai, human = -1, 0, 0

		if x + CONNECT <= FIELD_WIDTH and y - CONNECT + 1 >= 0:
			for i in range( CONNECT ):
				col, row = x + i, y - i
				stone = self.board[col][row]
				blank, ai, human, flag_stop = self._count_stones( col, row, stone, blank, ai, human )
				if flag_stop: break

		return ( blank, ai, human )

        def _check_proposed_col( self, pos ):
		""" We want to check if we can place a stone here (don't levitate !)
                Returns true (ok)/false (ko)
		"""

		if pos == -1:
			return False

		if pos["col"] >= 0 and pos["col"] < 7:
			# Check if it is possible to place the stone at the needed height
			if pos["row"] == 0 or self.board[pos["col"]][pos["row"] - 1] != 0:
				return True

		return False

	def _find_forced_move( self ):
		""" Check if the next move is a forced one and where to place the stone.
		A forced move occurs if the human player or the AI could win the game with the next move.
		Returns the position where to place the stone or -1 if not necessary.
		"""

		force_x = -1

		for x in range( FIELD_WIDTH ):
			for y in range( FIELD_HEIGHT ):

				# Check: UP
				blank, ai, human = self._count_stones_up( x, y )
				# Evaluate: UP
				if blank != -1:
					# If there is a chance to win: Do it!
					if ai == 3: return blank["col"]
					# Remember dangerous situation for now.
					# Maybe there will be a chance to win somewhere else!
					elif human == 3:
						if VERBOSE: print "[human] could win UP with %d." % blank["col"]
						force_x = blank["col"]

				# Check: RIGHT
				blank, ai, human = self._count_stones_right( x, y )
				# Evaluate: RIGHT
				if self._check_proposed_col( blank ):
					if ai == 3: return blank["col"]
					elif human == 3:
						if VERBOSE: print "[human] could win RIGHT with %d." % blank["col"]
						force_x = blank["col"]

				# Check: DIAGONAL RIGHT UP
				blank, ai, human = self._count_stones_rightup( x, y )
				# Evaluate: DIAGONAL RIGHT UP
				if self._check_proposed_col( blank ):
					if ai == 3: return blank["col"]
					elif human == 3:
						if VERBOSE: print "[human] could win DIAGONAL RIGHT UP with %d." % blank["col"]
						force_x = blank["col"]

				# Check: DIAGONAL RIGHT DOWN
				blank, ai, human = self._count_stones_rightdown( x, y )
				# Evaluate: DIAGONAL RIGHT DOWN
				if self._check_proposed_col( blank ):
					if ai == 3: return blank["col"]
					elif human == 3:
						if VERBOSE: print "[human] could win DIAGONAL RIGHT DOWN with %d." % blank["col"]
						force_x = blank["col"]

		return force_x
