#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import cv2

imgFile = "/Users/Greenborg/Desktop/Source/CNTK-Peter/Examples/Image/DataSets/Grocery/testImages/WIN_20160803_11_28_42_Pro.jpg"

img = cv2.imread(imgFile,1)

img2 = img
col = (0,255,255)
cv2.rectangle(img2,(650,200),(1080,750),(0,255,255),6)

cv2.imwrite('GrocCut1.png',img2)
img = cv2.imread(imgFile,1)
img3 = img[100:850,650:1080]
cv2.circle(img,(756,411),10,col,-1)
cv2.putText(img,'756.0 , 411.0',(756-80, 411-20),cv2.FONT_HERSHEY_SIMPLEX,0.7,col,2)

cv2.circle(img,(972,563),10,col,-1)
cv2.putText(img,'972.0 , 563.0',(972-80, 563+24),cv2.FONT_HERSHEY_SIMPLEX,0.7,col,2)

cv2.putText(img,'Label=1, Avocado',(int(np.mean((756.0,972.0)))-105,int(np.mean((411.0,563.0)))+45),cv2.FONT_HERSHEY_SIMPLEX,0.7,col,2)
cv2.rectangle(img,(756,411),(972,563),col,1)


img3 = img[100:850,650:1080]

cv2.imwrite('GrocCut2.png',img3)
#plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
#plt.show()
