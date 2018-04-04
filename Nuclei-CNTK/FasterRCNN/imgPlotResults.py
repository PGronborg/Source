#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import csv
import matplotlib.pyplot as plt
import numpy as np
import cv2

imgFolder = "/Volumes/Visiopharm Student HDD/F18_Peter/Data/Ki67/test_256_20XX/"
file = "/Volumes/Visiopharm Student HDD/F18_Peter/Data/Ki67/test_256_20X/"
num = int(sys.argv[1])

#imgVal = num % 100
#folderVal = (num - imgVal) / 100
#imgVal = imgVal - 1

Floc = open(file+"testval_nuclei.txt","r")
Froi = open(file+"testval_nuclei_roi.txt","r")

lines = Floc.readlines()
lineLoc = lines[num]
loc = lineLoc.split()

img = cv2.imread(imgFolder+loc[1],1)

roiLines = Froi.readlines()
lineRoi = roiLines[num]
roi = lineRoi.split()
roi[0:2] = []


for i in range(int(len(roi)/5)):
    ind = int(i*5)
    cv2.rectangle(img,(round(float(roi[ind])),round(float(roi[ind+1]))),(round(float(roi[ind+2])),round(float(roi[ind+3]))),(0,255,0),1)
    

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
#cv2.imshow(loc[1],img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


