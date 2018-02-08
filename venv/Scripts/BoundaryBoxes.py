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
    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 15, param1=1, param2=10, minRadius=0, maxRadius=20)

    # Predefine counter
    numim = 0

    # Define where to save files
    loc = "E:/F18_Peter/Data/Ki67/Sampled Test/" + str(folderNum) + "/FeatureSamples/FeatureImage" + str(
        imgNum) + "/" + posneg

    # Check if the folder already exist else create it
    if not os.path.exists(loc):
        os.makedirs(loc)

    # ensure at least some circles were found
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # loop over the (x, y) coordinates
        for (x, y, r) in circles:

            # Get coordinates of boundary box
            ymin, ymax = minmax(y,scalenum)
            xmin, xmax = minmax(x,scalenum)

            # Generate name for image to be saved
            locTemp = loc + "/Image" + str(numim) + ".jpg"

            # Save part of the image
            cv2.imwrite(locTemp, cv_img[ymin:ymax, xmin:xmax])

            # Add coordinates of boundary box to region of interest text and increase counter
            texter = texter+" "+str(ymin)+" "+str(ymax)+" "+str(xmin)+" "+str(xmax)+" "+str(classer)
            numim = numim + 1

    return texter


# Open files for write to training file and region of interest file
trainFile = open("E:/F18_Peter/Data/Ki67/Sampled Test/trainval_nuclei.txt","w")
roiFile = open("E:/F18_Peter/Data/Ki67/Sampled Test/trainval_nuclei_roi.txt","w")

# Predefine number
countIm = 0

# Run through all folders and all images in all folders
for folderNum in range(0, 15):
    for imgNum in range(0, 32):

        # Make path for image and mask
        img_path = "E:/F18_Peter/Data/Ki67/Sampled Test/"+str(folderNum)+"/Features/FeatureImage"+str(imgNum)+".tif"
        mask_path = "E:/F18_Peter/Data/Ki67/Sampled Test/"+str(folderNum)+"/Labels/LabelImage"+str(imgNum)+".tif"

        # Save path to training file
        textsave = str(countIm)+"\t"+img_path+"\t0\n"
        trainFile.write(textsave)
        countIm = countIm + 1

        # Read image and mask file
        cv_img = cv2.imread(img_path)
        cv_mask = cv2.imread(mask_path, 2)  # 0 = grayscale

        # Preallocate matrices for positive and negative masks
        mask_positive = np.zeros(cv_mask.shape)
        mask_negative = np.zeros(cv_mask.shape)

        # Separate positive and negative masks
        for i in range(0, 255):
            for j in range(0, 255):
                if cv_mask[i, j] == 1:
                    mask_positive[i, j] = 200
                elif cv_mask[i, j] == 2:
                    mask_negative[i, j] = 200

        # Start text for region of interest file
        text_roi = str(countIm)+" |roiAndLabel"

        # Get region of interest for positive and negative nuclei
        text_roi = saveNuclei(mask_negative, 25, 'Negative',1,text_roi)
        text_roi = saveNuclei(mask_positive, 25, 'Positive',2,text_roi)

        # Write region of interest text to file
        roiFile.write(text_roi+"\n")

# Close training and region of interest file
trainFile.close()
roiFile.close()
