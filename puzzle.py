#!/usr/bin/python
# coding: utf-8

import sys, os
import time
import threading

import server
import core
import proxy

PTV_LOGFILE='/var/log/puzzle.log'
root_dir = os.path.dirname(sys.argv[0])

class Logger(object):
	def __init__(self, pathToLog):
		self.pathToLog = pathToLog
		self.console = sys.stdout

	def write(self, message):
		f = open(self.pathToLog, "a")
		f.write(message)
		f.close()
		self.console.write(message)
		self.console.flush()

if os.path.exists(PTV_LOGFILE): os.remove(PTV_LOGFILE)
sys.stdout=Logger(PTV_LOGFILE)

ip = core.ip
port = core.port
proxy_port = port + 1

print('\n------------ Starting Puzzle-TV v%s ------------') % server.version()
print ('***')
print('WEBUI:          http://'+ip+':'+str(port))
print('PLAYLIST:       http://'+ip+':'+str(port)+'/playlist')
print('TVH PLAYLIST:   http://'+ip+':'+str(port)+'/tvhlist')
print('PROXY PLAYLIST: http://'+ip+':'+str(port)+'/proxylist')
print ('***')

serv = server.MyThreadingHTTPServer(("0.0.0.0",port), server.HttpProcessor)
threading.Thread(target=serv.serve_forever).start()

serv_proxy = proxy.ThreadingSimpleServer(("0.0.0.0",proxy_port), proxy.ProxyRequestHandler)
threading.Thread(target=serv_proxy.serve_forever).start()

print('------------- Starting Puzzle-TV: OK --------------')
print('\nDate: %s\n') % time.strftime('%Y-%m-%d %H:%M:%S')

upd_channels_cnt = 0
clean_log_cnt = 0

try:
	while server.trigger:
		if upd_channels_cnt == 0:
			core.refresh_cnl()

		upd_channels_cnt += 1
		if upd_channels_cnt > 10:
			upd_channels_cnt = 0
			clean_log_cnt += 1
		if clean_log_cnt > 300:
			clean_log_cnt = 0
			if os.path.exists(PTV_LOGFILE):
				print('----- Clean log file -----')
				os.remove(PTV_LOGFILE)
		time.sleep(6)
except KeyboardInterrupt:
	print '\n...Program Stopped Manually!\n'

try:
	serv_proxy.server_close()
	serv_proxy.shutdown()
except: pass
try:
	serv.server_close()
	serv.shutdown()
except: pass

print('------------ Stopped Puzzle-TV: OK ------------\n')
