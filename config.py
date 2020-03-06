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
	# Proxy (restreamer) channels config
	#------------------------------------------------------------
	#
	# user agent
	usr_agent = 'Restream/5.20408.171030 (mag250, mag250) SmartSDK/1.5.63-rt-25 Qt/4.7.3 API/0.30.0'
	# chunk size in bytes (1024 .. 8192)
	chunk_size = 2048
	# input buffer in milliseconds (0 .. 60000)
	input_buff = 1000
	# output buffer in milliseconds (0 .. 60000)
	output_buff = 2000
	# sources that will be buffered
	sources_buff = [
		'ott.onlineott.tv',
		'ott.ipstream.one',
		'ace/getstream',
		'zproxy/step',
		'strm.yandex.ru',
		'rt-cache1.peers.tv',
		'iptv1.satbiling.com',
		'api-tv.ipnet.ua',
		]
