from matplotlib import pyplot as plt
import cv2

img = cv2.imread("a.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rbg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.subplot(1, 1, 1)
plt.imshow(img_rbg)
plt.show()