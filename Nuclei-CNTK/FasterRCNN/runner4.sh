#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start LowHigh"

time CUDA_VISIBLE_DEVICES=3 python run_faster_rcnn_VGG16.py LowHigh [0.00001]*200 0.0005  > LowHigh.txt 2> errLowHigh.txt

mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done LowHigh"