#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import csv
import matplotlib.pyplot as plt
import numpy as np
import cv2

#imgFolder = "/Users/Greenborg/Desktop/Experiments/Train/Correct/"
imgFolder = "/Volumes/Visiopharm Student HDD/F18_Peter/Data/Ki67/test_256_20XX/"
#file = "/Users/Greenborg/Desktop/Experiments/"
file = "/Volumes/Visiopharm Student HDD/F18_Peter/Data/Ki67/test_256_20X/"
fileEval = "/Users/Greenborg/Desktop/Source/Nuclei-CNTK/FasterRCNN/Output/"
name = "Tester1.txt"
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
    #cv2.rectangle(img,(round(float(roi[ind])),round(float(roi[ind+1]))),(round(float(roi[ind+2])),round(float(roi[ind+3]))),(0,255,0),1)
    cv2.circle(img,(int(round(np.mean((float(roi[ind]),float(roi[ind+2]))))),int(round(np.mean((float(roi[ind+1]),float(roi[ind+3])))))),2,(0,255,0),-1)
    #if int(round(float(roi[ind+4]))) == 1:
     #   cv2.circle(img,(int(round(np.mean((float(roi[ind]),float(roi[ind+2]))))),int(round(np.mean((float(roi[ind+1]),float(roi[ind+3])))))),2,(255,0,0),-1)
    #else:
     #   cv2.circle(img,(int(round(np.mean((float(roi[ind]),float(roi[ind+2]))))),int(round(np.mean((float(roi[ind+1]),float(roi[ind+3])))))),2,(0,255,0),-1)

FroiEval = open(fileEval+name)
roiLinesEval = FroiEval.readlines()
lineRoiEval = roiLinesEval[num]
roiEval = lineRoiEval.split()

for i in range(int(len(roiEval)/6)):
    ind = int(i*6)
    #cv2.rectangle(img,(round(float(roi[ind])),round(float(roi[ind+1]))),(round(float(roi[ind+2])),round(float(roi[ind+3]))),(0,255,0),1)
    cv2.circle(img,(int(round(np.mean((float(roiEval[ind]),float(roiEval[ind+2]))))),int(round(np.mean((float(roiEval[ind+1]),float(roiEval[ind+3])))))),2,(0,0,255),-1)
    #if int(round(float(roi[ind+4]))) == 1:
     #   cv2.circle(img,(int(round(np.mean((float(roi[ind]),float(roi[ind+2]))))),int(round(np.mean((float(roi[ind+1]),float(roi[ind+3])))))),2,(255,0,0),-1)
    #else:
     #   cv2.circle(img,(int(round(np.mean((float(roi[ind]),float(roi[ind+2]))))),int(round(np.mean((float(roi[ind+1]),float(roi[ind+3])))))),2,(0,255,0),-1)


plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
#cv2.imshow(loc[1],img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


