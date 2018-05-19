# -*- coding: utf-8 -*-
"""
Created on 19/05/2018

@author: Raphaël
"""
import copy

class Player:
	
	def __init__(self, player_num, symbol):
		self.__playerNum = player_num
		self.__symbol = symbol
	
	def getPlayerNum(self):
		return copy.deepcopy(self.__playerNum)
	
	def getSymbol(self):
		return copy.deepcopy(self.__symbol)
