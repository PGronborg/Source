#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import sys
#import csv
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

imgFolder = "/Users/Greenborg/Desktop/Experiments/Test/"
file = "/Users/Greenborg/Desktop/Experiments/Test/"
fileEval = "/Users/Greenborg/Desktop/Source/Nuclei-CNTK/FasterRCNN/Output/"
name = "/Ref/ColorChange.txt"
#num = 5;

Floc = open(file+"testval_nuclei.txt","r")
Froi = open(file+"testval_nuclei_roi.txt","r")

lines = Floc.readlines()
roiLines = Froi.readlines()
PrecTop = np.zeros([100,100])
RecTop = np.zeros([100,100])
Prec = np.zeros(100)
Rec = np.zeros(100)
for i in range(0,100):
    print(i)
    lineLoc = lines[i]
    loc = lineLoc.split()
    
    lineRoi = roiLines[i]
    roi = lineRoi.split()
    roi[0:2] = []
    
    FroiEval = open(fileEval+name)
    roiLinesEval = FroiEval.readlines()
    lineRoiEval = roiLinesEval[i]
    roiEval = lineRoiEval.split()
    
    distArray = np.zeros([int(len(roi)/5),int(len(roiEval)/6)])
    roiSel = np.zeros(int(len(roi)))
    roiEvalSel = np.zeros(int(len(roiEval)))
    NumGT = int(len(roi)/5)
    NumPro = int(len(roiEval)/6)
    Pro = np.zeros(NumPro)
    GT = np.zeros(NumGT)
    
    score = np.zeros(NumPro)
    
    for k in range(NumGT):
        indI = int(k*5)
        for j in range(NumPro):
            indJ = int(j*6)
            a=[int(round(np.mean((float(roi[indI]),float(roi[indI+2]))))),int(round(np.mean((float(roi[indI+1]),float(roi[indI+3])))))]
            b=[int(round(np.mean((float(roiEval[indJ]),float(roiEval[indJ+2]))))),int(round(np.mean((float(roiEval[indJ+1]),float(roiEval[indJ+3])))))]
            dist = np.linalg.norm(np.array(a)-np.array(b))
            if dist < 30:
                distArray[k,j] = bb_intersection_over_union(list(map(float,roi[indI:indI+4])), list(map(float,roiEval[indJ:indJ+4])))
                
    for j in range(NumPro):
        indJ = int(j*6)
        score[j] = float(roiEval[indJ+5])
        
        if np.max(distArray[:,j])>0.5:
            ind = np.unravel_index(np.argmax(distArray[:,j], axis=None), distArray[:,j].shape)
            indGT = int(ind[0]*5)
            if int(roiEval[indJ+4])==int(roi[indGT+4]):
                if GT[ind[0]]==0:
                    GT[ind[0]] = 1
                    Pro[j] = 1
                    
    Prec[i] = np.sum(Pro)/NumPro
    Rec[i] = np.sum(Pro)/NumGT
    k = 0
    sorter = np.argsort(score)
    
    while k<100:
        try:
            PrecTop[i,k] = np.sum(Pro[sorter[0:(k+1)]])/(k+1)
            RecTop[i,k] = np.sum(Pro[sorter[0:(k+1)]])/NumGT
            k=k+1
        except:
            break
        
        
