from bbio import *
from bbio.libraries.BBIOServer import BBIOServer, Page

server = BBIOServer(8000)

def setup():
	page1 = Page("Server Test")
	page1.add_text("Testing the BBIOServer library")
	
	page2 = Page("LED Control")
	page2.add_text("Controlling an onboard LED")
	
	# page2.add_button(lambda: toggle(USR3),  "Toggle USR3 LED", newline = True)
	# page2.add_monitor(lambda: pinState(USR3), "current state:")
	
	# server.start(page1, page2)

def loop():
	print("/nServer has stopped, exiting")
	stop()
	
	run(setup, loop)