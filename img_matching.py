import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import pyautogui


# print(str(getLocation(cv.imread('res/test.png',0),'cv.imread('res/pick.png',0))))
def getLocation(image,template, threshold = 0.85, meth = 'cv.TM_CCOEFF_NORMED'):
	method = eval(meth)
	# Apply template Matching
	res = cv.matchTemplate(image,template,method)
	min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
	if max_val > threshold :
		return max_loc
	else:
		return False
# print(str(getLocationOnScreen('res/countinue.png')))
def getLocationOnScreen(template_path, threshold = 0.85, meth = 'cv.TM_CCOEFF_NORMED'):
	image = pyautogui.screenshot()
	gray = cv.cvtColor(np.array(image), cv.COLOR_BGR2GRAY)
	template = cv.imread(template_path, 0)

	return getLocation(gray,template, threshold, meth)



#print(str(getLocationOnScreen('res/end_screen.png')))

# img = pyautogui.screenshot()
# img = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
# img.astype(np.float32)
# pyautogui.screenshot("straight_to_disk.png")
# img = cv.imread("straight_to_disk.png")

# img2 = gray.copy()
# template = cv.imread('res/end_screen.png',0)
# w, h = template.shape[::-1]

# methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
#             'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
# for meth in methods:
#     img = img2.copy()
#     method = eval(meth)
#     # Apply template Matching
#     res = cv.matchTemplate(img,template,method)
#     min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
#     print(str(min_val)+"," +str(max_val)+","+str(min_loc)+","+str(max_loc))
#     # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
#     if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
#         top_left = min_loc
#     else:
#         top_left = max_loc
#     bottom_right = (top_left[0] + w, top_left[1] + h)
#     cv.rectangle(img,top_left, bottom_right, 255, 2)
#     plt.subplot(121),plt.imshow(res,cmap = 'gray')
#     plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
#     plt.subplot(122),plt.imshow(img,cmap = 'gray')
#     plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
#     plt.suptitle(meth)
#     plt.show()