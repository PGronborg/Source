#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start Low"

time CUDA_VISIBLE_DEVICES=0 python run_faster_rcnn_VGG16.py Low 0.0000005 > Low.txt 2> errLow.txt

mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done Low"
