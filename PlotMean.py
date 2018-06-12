#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from openpyxl import load_workbook

fileEval = "/Users/Greenborg/Desktop/Source/Nuclei-CNTK/FasterRCNN/Output/RefNew/Results/"
#file = "Ref/Ref_3_All.xlsx"
val = 'NMS'
AllPrec = []
AllRec = []
AllPosPrec = []
AllPosRec = []
AllNegPrec = []
AllNegRec = []
for i in range(5,101,5):
    wb = load_workbook(fileEval+'All/RefNoNMS_'+val+'_'+str(i)+'.xlsx')
    if wb['Facts']['D3'].value>0:
        AllPrec.append(wb['Facts']['D4'].value/wb['Facts']['D3'].value)
    else:
        AllPrec.append(0)
    if wb['Facts']['D2'].value>0:
        AllRec.append(1-wb['Facts']['D4'].value/wb['Facts']['D2'].value)
    else:
        AllRec.append(0)
    if wb['Facts']['B3'].value>0:  
        AllPosPrec.append(wb['Facts']['B4'].value/wb['Facts']['B3'].value)
    else:
        AllPosPrec.append(0)
    if wb['Facts']['B2'].value>0:
        AllPosRec.append(1-wb['Facts']['B4'].value/wb['Facts']['B2'].value)
    else:
        AllPosRec.append(0)
    if wb['Facts']['C3'].value>0:
        AllNegPrec.append(wb['Facts']['C4'].value/wb['Facts']['C3'].value)
    else:
        AllNegPrec.append(0)
    if wb['Facts']['C2'].value>0:
        AllNegRec.append(1-wb['Facts']['C4'].value/wb['Facts']['C2'].value)
    else:
        AllNegRec.append(0)
    wb.close()

plt.plot(AllRec,AllPrec,'.-')
plt.plot(AllPosRec,AllPosPrec,'.-')
plt.plot(AllNegRec,AllNegPrec,'.-')
plt.plot([AllRec[6],AllPosRec[6],AllNegRec[6]],[AllPrec[6],AllPosPrec[6],AllNegPrec[6]],'o')
#plt.plot([AllRec[6],AllPosRec[6],AllNegRec[6]],[AllPrec[6],AllPosPrec[6],AllNegPrec[6]],'o')
#plt.plot([AllRec[14],AllPosRec[14],AllNegRec[14]],[AllPrec[14],AllPosPrec[14],AllNegPrec[14]],'o')
plt.title('Non-Maximum Suppression - IoU')
#plt.title('Metric - IoU')
#plt.title('Threshold - score')
plt.xlabel('1 - Recall')
plt.ylabel('Precision')
plt.xlim(0,1)
plt.ylim(0,1)

plt.legend(['All','Positive','Negative','IoU > 0.35'])
#plt.legend(['All','Positive','Negative','IoU > 0.35'])
#plt.legend(['All','Positive','Negative','Score > 0.74'])

#plt.show()
plt.savefig(fileEval+'All/RefNoNMS_'+val+'.png')