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
	# generic user agent
	usr_agent = 'Restream/5.20408.171030 (mag250, mag250) SmartSDK/1.5.63-rt-25 Qt/4.7.3 API/0.30.0'
	# TS streams buffer size in megabytes (0 .. 20)
	buffer_ts = 5
	# HLS streams buffer size in megabytes (0 .. 20)
	buffer_hls = 10
	# size of the thread pool used to download HLS segments (1 .. 10)
	hls_threads = 4
	# how many segments from the end to start live HLS streams on (1 .. 10)
	hls_edge = 3
	# wait until the HLS buffer is full
	wait_buffer = False
