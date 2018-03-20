import cv2
import numpy as np
import os

def minmax(xy,scalenum):

    # Check if the corner hits below zero
    if (xy - scalenum) < 0:
        xymin = 0
    else:
        xymin = (xy - scalenum)

    # Check if the corner hits above max size of image(255)
    if (xy + scalenum) > 255:
        xymax = 255
    else:
        xymax = (xy + scalenum)

    return xymin, xymax


def saveNuclei(mask, scalenum, posneg, classer, texter):

    # Make the mask image in the correct format for HoughCircles, uint8
    mask = mask.astype(np.uint8)

    # detect circles in the image
    #circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 10, param1=1, param2=2, minRadius=0, maxRadius=5)

    im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Predefine counter
    numim = 0

    # # Define where to save files
    # loc = "E:/F18_Peter/Data/Ki67/Sampled Test/" + str(folderNum) + "/FeatureSamples/FeatureImage" + str(
    #     imgNum) + "/" + posneg
    #
    # # Check if the folder already exist else create it
    # if not os.path.exists(loc):
    #     os.makedirs(loc)

    # ensure at least some circles were found
    if contours is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        #circles = np.round(circles[0, :]).astype("int")

        # loop over the (x, y) coordinates
        #for (x, y, r) in circles:
        for i in range(0,contours.__len__()):
            valM = contours[i].mean(0)
            valM = valM[0].round()

            # Get coordinates of boundary box
            ymin, ymax = minmax(valM[1],scalenum)
            xmin, xmax = minmax(valM[0],scalenum)

            # Generate name for image to be saved
            #locTemp = loc + "/Image" + str(numim) + ".jpg"

            # Save part of the image
            #cv2.imwrite(locTemp, cv_img[ymin:ymax, xmin:xmax])

            # Add coordinates of boundary box to region of interest text and increase counter
            texter = texter+" "+str(xmin)+" "+str(ymin)+" "+str(xmax)+" "+str(ymax)+" "+str(classer)
            #numim = numim + 1

    return texter


TTtype = 'test'
TTname = 'test'
# Open files for write to training file and region of interest file
#trainFile = open('E:/F18_Peter/Data/Ki67/'+TTtype+'_256_20X/'+TTname+'val_nuclei.txt',"w")
#roiFile = open('E:/F18_Peter/Data/Ki67/'+TTtype+'_256_20X/'+TTname+'val_nuclei_roi.txt',"w")
trainFile = open('E:/F18_Peter/Data/Ki67/Sampled Test/'+TTname+'val_nuclei.txt',"w")
roiFile = open('E:/F18_Peter/Data/Ki67/Sampled Test/'+TTname+'val_nuclei_roi.txt',"w")

# Predefine number
countIm = 0

# Run through all folders and all images in all folders
for folderNum in range(12, 15):
    print(folderNum)
    for imgNum in range(32):

        # Make path for image and mask
        #img_path = 'E:/F18_Peter/Data/Ki67/'+TTtype+'_256_20X/'+str(folderNum)+"/Features/FeatureImage"+str(imgNum)+".tif"
        #label_path = 'E:/F18_Peter/Data/Ki67/'+TTtype+'_256_20X/'+str(folderNum)+"/Labels/LabelImage"+str(imgNum)+".tif"
        label_path = 'E:/F18_Peter/Data/Ki67/Sampled Test/' + str(folderNum) + "/Labels/LabelImage" + str(imgNum) + ".tif"

        #mask_path = 'E:/F18_Peter/Data/Ki67/'+TTtype+'_256_20X/' + str(folderNum) + "/Mask/MaskImage" + str(imgNum) + ".tif"

        # Define where to save files
        loc = 'E:/F18_Peter/Data/Ki67/'+TTtype+'_256_20XX/' + str(folderNum) + '/Features'

        # Check if the folder already exist else create it
        #if not os.path.exists(loc):
         #   os.makedirs(loc)

        # Save path to training file
        textsave = str(countIm)+"\t"+str(folderNum)+"/Features/FeatureImage"+str(imgNum)+".png\t0\n"
        trainFile.write(textsave)

        # Read image and mask file
        #cv_img = cv2.imread(img_path)
        cv_label = cv2.imread(label_path, 2)  # 0 = grayscale
        #cv_mask = cv2.imread(mask_path, 0)  # 0 = grayscale

        #i, j = np.where(cv_mask == 0)
        #cv_img[i, j, 0] = 255
        #cv_img[i, j, 1] = 255
        #cv_img[i, j, 2] = 255

        #loc = loc + "/FeatureImage"+str(imgNum)+".png"
        #cv2.imwrite(loc, cv_img)
        # Preallocate matrices for positive and negative masks
        label_positive = np.zeros(cv_label.shape)
        label_negative = np.zeros(cv_label.shape)

        i, j = np.where(cv_label == 2)
        label_negative[i, j] = 200

        i, j = np.where(cv_label == 1)
        label_positive[i, j] = 200
        # Start text for region of interest file
        text_roi = str(countIm)+" |roiAndLabel"
        countIm = countIm + 1

        # Get region of interest for positive and negative nuclei
        text_roi = saveNuclei(label_negative, 25, 'Negative',1,text_roi)
        text_roi = saveNuclei(label_positive, 25, 'Positive',2,text_roi)

        # Write region of interest text to file
        roiFile.write(text_roi+"\n")

# Close training and region of interest file
trainFile.close()
roiFile.close()
