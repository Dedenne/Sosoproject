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
