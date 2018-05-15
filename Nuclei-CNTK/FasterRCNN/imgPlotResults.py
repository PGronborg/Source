#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##Plot all results for image 5
# python3 imgPlotResults.py 5

##Plot all results with IOU under 0.3 but higher than 0.0
# python3 imgPlotResults.py 5 0.3

##Plot all results with IOU over 0.7
# python3 imgPlotResults.py 5 0.7

##Plot outliers
# python3 imgPlotResults.py 5 out
import sys
import csv
import matplotlib.pyplot as plt
import numpy as np
import cv2

def bb_intersection_over_union(boxA, boxB):
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    
    # compute the area of intersection rectangle
    interArea = (xB - xA + 1) * (yB - yA + 1)
    
    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
    
    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = max(0,interArea / float(boxAArea + boxBArea - interArea))
    if iou>1.0:    
        iou = 0.0
    
    # return the intersection over union value
    return iou

#imgFolder = "/Users/Greenborg/Desktop/Experiments/Train/Correct/"
imgFolder = "/Users/Greenborg/Desktop/Experiments/Test/"
#file = "/Users/Greenborg/Desktop/Experiments/"
file = "/Users/Greenborg/Desktop/Experiments/Test/"
fileEval = "/Users/Greenborg/Desktop/Source/Nuclei-CNTK/FasterRCNN/Output/"
name = "/Ref/Ref_3.txt"
num = int(sys.argv[1])
pltNum = 2

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

FroiEval = open(fileEval+name)
roiLinesEval = FroiEval.readlines()
lineRoiEval = roiLinesEval[num]
roiEval = lineRoiEval.split()

if len(sys.argv)==3:
    try:
        numIn = float(sys.argv[2])
    except:
        numIn = 2
        
    distArray = np.zeros([int(len(roi)/5),int(len(roiEval)/6)])
    roiSel = np.zeros(int(len(roi)))
    roiEvalSel = np.zeros(int(len(roiEval)))

    for i in range(int(len(roi)/5)):
        indI = int(i*5)
        for j in range(int(len(roiEval)/6)):
            indJ = int(j*6)
            a=[int(round(np.mean((float(roi[indI]),float(roi[indI+2]))))),int(round(np.mean((float(roi[indI+1]),float(roi[indI+3])))))]
            b=[int(round(np.mean((float(roiEval[indJ]),float(roiEval[indJ+2]))))),int(round(np.mean((float(roiEval[indJ+1]),float(roiEval[indJ+3])))))]
            dist = np.linalg.norm(np.array(a)-np.array(b))
            if dist < 30:
                distArray[i,j] = bb_intersection_over_union(list(map(float,roi[indI:indI+4])), list(map(float,roiEval[indJ:indJ+4])))
    if numIn == 2:
        for i in range(int(len(roiEval)/6)):
            k = np.where(max(distArray[:,i])==distArray[:,i])
            k = k[0]
            if max(distArray[:,i]) == 0.0:
                roiEvalSel[i*6:i*6+6] = roiEval[i*6:i*6+6]
            elif max(distArray[:,i]) != max(distArray[k[0],:]):
                if distArray[k,i]<0.3:
                    roiEvalSel[i*6:i*6+6] = roiEval[i*6:i*6+6]
        for j in range(int(len(roi)/5)):
            if max(distArray[j,:])<0.3:
                roiSel[j*5:j*5+5] = roi[j*5:j*5+5]
    elif numIn <0.5:
        for i in range(int(len(roiEval)/6)):
            if max(distArray[:,i]) < numIn:
                if max(distArray[:,i])>0.0:
                    k = np.where(max(distArray[:,i])==distArray[:,i])
                    k = k[0]
                    roiEvalSel[i*6:i*6+6] = roiEval[i*6:i*6+6]
                    if len(k)>1:
                        for j in range(len(k)):
                            roiSel[int(k[j])*5:int(k[j])*5+5] = roi[int(k[j])*5:int(k[j])*5+5]
                    else:
                        roiSel[int(k[0])*5:int(k[0])*5+5] = roi[int(k[0])*5:int(k[0])*5+5]  
    elif numIn>0.5:
        for i in range(int(len(roiEval)/6)):
            if max(distArray[:,i]) > numIn:
                k = np.where(max(distArray[:,i])==distArray[:,i])
                k = k[0]
                roiEvalSel[i*6:i*6+6] = roiEval[i*6:i*6+6]
                if len(k)>1:
                    for j in range(len(k)):
                        roiSel[int(k[j])*5:int(k[j])*5+5] = roi[int(k[j])*5:int(k[j])*5+5]
                else:
                    roiSel[int(k[0])*5:int(k[0])*5+5] = roi[int(k[0])*5:int(k[0])*5+5]       
    roi = roiSel
    roiEval = roiEvalSel
elif len(sys.argv)>3:
    roiEvalSel = np.zeros(int(len(roiEval)))
    numIn = float(sys.argv[3])

    if len(sys.argv)==4:
        for j in range(int(len(roiEval)/6)):
            indJ = int(j*6)
            if float(roiEval[indJ+5])>numIn:
                roiEvalSel[j*6:j*6+6] = roiEval[j*6:j*6+6]
    elif len(sys.argv)==5:
        cl = int(sys.argv[4])
        roiSel = np.zeros(int(len(roi)))
        for j in range(int(len(roiEval)/6)):
            indJ = int(j*6)
            if float(roiEval[indJ+5])>numIn:
                if int(roiEval[indJ+4])==cl:
                    roiEvalSel[j*6:j*6+6] = roiEval[j*6:j*6+6]

        for i in range(int(len(roi)/5)):
            indI = int(i*5)
            if int(roi[indI+4])==cl:
                roiSel[i*5:i*5+5] = roi[i*5:i*5+5]

        roi = roiSel

    roiEval = roiEvalSel


for i in range(int(len(roi)/5)):
    ind = int(i*5)
    if pltNum==1:
        cv2.rectangle(img,(round(float(roi[ind])),round(float(roi[ind+1]))),(round(float(roi[ind+2])),round(float(roi[ind+3]))),(0,255,0),1)
    else:
        cv2.circle(img,(int(round(np.mean((float(roi[ind]),float(roi[ind+2]))))),int(round(np.mean((float(roi[ind+1]),float(roi[ind+3])))))),3,(0,255,0),-1)
    #if int(round(float(roi[ind+4]))) == 1:
     #   cv2.circle(img,(int(round(np.mean((float(roi[ind]),float(roi[ind+2]))))),int(round(np.mean((float(roi[ind+1]),float(roi[ind+3])))))),2,(255,0,0),-1)
    #else:
     #   cv2.circle(img,(int(round(np.mean((float(roi[ind]),float(roi[ind+2]))))),int(round(np.mean((float(roi[ind+1]),float(roi[ind+3])))))),2,(0,255,0),-1)


for i in range(int(len(roiEval)/6)):
    ind = int(i*6)
    if pltNum==1:
        cv2.rectangle(img,(round(float(roiEval[ind])),round(float(roiEval[ind+1]))),(round(float(roiEval[ind+2])),round(float(roiEval[ind+3]))),(255,0,0),1)
    else:
        cv2.circle(img,(int(round(np.mean((float(roiEval[ind]),float(roiEval[ind+2]))))),int(round(np.mean((float(roiEval[ind+1]),float(roiEval[ind+3])))))),2,(255,0,0),-1)
    #if int(round(float(roi[ind+4]))) == 1:
     #   cv2.circle(img,(int(round(np.mean((float(roi[ind]),float(roi[ind+2]))))),int(round(np.mean((float(roi[ind+1]),float(roi[ind+3])))))),2,(255,0,0),-1)
    #else:
     #   cv2.circle(img,(int(round(np.mean((float(roi[ind]),float(roi[ind+2]))))),int(round(np.mean((float(roi[ind+1]),float(roi[ind+3])))))),2,(0,255,0),-1)


plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
#cv2.imshow(loc[1],img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


