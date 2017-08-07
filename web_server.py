from bbio import *
from bbio.libraries.BBIOServer import BBIOServer, Page

server = BBIOServer(8000)

def setup():
	page1 = Page("Server Test")
	page1.add_text("Testing BBIO Server library")

	page2 = Page("LED control")
	page2.add_text("Control and on-board LED")

	page2.add_button(lambda: toggle(USR3), "Toggle USR3 LED", newline = True)
	page2.add_monitor(lambda: pinstate(USR3), "Current state:")

	server.start(page1), page2


def loop():
	print "\nServer had stopped, exiting"
	stop()


run(setup, loop)		