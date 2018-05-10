#to run this script, please install pynput from pip
from pynput.mouse import Button, Controller
import time 

i= 1000 #Set i to how many click you wanted
mouse = Controller()





while True:
	if(mouse.position[0] != 1365):
	    mouse.click(Button.left,i)
	    time.sleep(0.8)
	else:
	    break

	
