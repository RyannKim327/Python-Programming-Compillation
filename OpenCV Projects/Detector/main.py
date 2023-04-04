from matplotlib import pyplot as plt
import cv2

img = cv2.imread("a.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rbg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

xml_data = cv2.CascadeClassifier("XML-Data.xml") # I don't know where do I need to get this
detect = xml_data.detectMultiScale(img_gray, minSize = (30, 30))
amt_det = len(detect)

if amt_det !=0:
	for(a, b, width, height) in detect:
		cv2.rectangle(img_rbg, (a, b),
		(a + height, b + width),
		(0, 275, 0), 9)

plt.subplot(1, 1, 1)
plt.imshow(img_rbg)
plt.show()