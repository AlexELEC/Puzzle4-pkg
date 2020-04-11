# -*- coding: utf-8 -*-
''' Puzzle configuration script. Edit this file. '''

class PuzzleConf():
	#------------------------------------------------------------
	# Checking your internet connection
	#------------------------------------------------------------
	#
	# url or ip-address
	check_url = 'http://www.google.com/'
	# connection timeout in seconds
	check_timeout = 1
	#------------------------------------------------------------
	# Pproxy (restreamer) config
	#------------------------------------------------------------
	#
	# user agent
	usr_agent = 'Restream/5.20408.171030 (mag250, mag250) SmartSDK/1.5.63-rt-25 Qt/4.7.3 API/0.30.0'
	# chunk size in bytes (1024 .. 8192)
	chunk_size = 2048
	# enable/disable buffering - True/False
	buffering = True
	# simple prebuffering in megabytes (0 .. 20) only when buffering is disabled
	simple_prebuff = 1
	# input buffer in milliseconds (0 .. 60000)
	input_buff = 1000
	# output buffer in milliseconds (0 .. 60000)
	output_buff = 2000
	# sources that will not be buffered (comma separated)
	# example: sources_not_buff = ['cdn.adultiptv.net',]
	sources_not_buff = []
