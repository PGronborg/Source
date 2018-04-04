#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start High"

time CUDA_VISIBLE_DEVICES=1 python run_faster_rcnn_VGG16.py High 0.05 > High.txt 2> errHigh.txt

mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done High"