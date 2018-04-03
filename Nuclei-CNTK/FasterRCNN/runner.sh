#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start LowLow"

time CUDA_VISIBLE_DEVICES=0 python run_faster_rcnn_VGG16.py LowLow [0.00001]*200 0.000005  > LowLow.txt 2> errLowLow.txt

mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done LowLow"
