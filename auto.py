import pyautogui
import time
import sys
import img_matching


current_img = 'enter_combat';

def findAndClick(filename):
	print("find and click for "+ filename)
	imgLocation = img_matching.getLocationOnScreen('res/'+filename+'.png')
	if not imgLocation:
		return False 
	x, y = imgLocation	# adjust position for mac
	x/=2
	y/=2
	# insure input is not missing
	pyautogui.click(x, y)
	pyautogui.click(x, y)
	pyautogui.click(x, y)
	time.sleep(1)
	return True

def mainLoop():
	global current_img
	global connecting_hash
	image_list = ['enter_combat','countinue','retry','confirm','end_list']
	print("Current image at " +  ''.join(connecting_hash[current_img]))
	for filename in connecting_hash[current_img]:
		if findAndClick(filename):
			current_img = filename
			print("Found")
			break
		time.sleep(1)	

def run():
	global current_img
	global connecting_hash
	connecting_hash = {
		'enter_combat': ['countinue','skip', 'enter_combat'],
		'countinue': ['end_screen', 'confirm','countinue'],
		'retry': ['teammate','retry'],
		'confirm': ['end_screen','confirm'],
		'end_screen': ['retry','end_screen'],
		'teammate':['pick','teammate'],
		'pick':['enter_combat','pick'],
		'skip':['skip','countinue']
	}
	if sys.argv[1] is None:
		current_img = enter_combat
	else:
		current_img = sys.argv[1]
	while True:
		try:
			mainLoop()
			time.sleep(2)
		except Exception as e:
			raise 
		else:
			pass

run()



