# -*- coding: utf-8 -*-
"""
Created on 19/05/2018

@author: Raphaël
"""
import copy

class Board:

	def __init__(self, row = 6, column = 7):
		self.board = [['.' for x in range(column)]for y in range(row)]
		self.__row = row
		self.__column = column
	
	def getRow(self):
		return copy.deepcopy(self.__row)
		
	def getColumn(self):
		return copy.deepcopy(self.__column)
