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
