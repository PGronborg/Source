#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start HighHigh"

time CUDA_VISIBLE_DEVICES=2 python run_faster_rcnn_VGG16.py 0.0005  > HighHigh.txt 2> errHighHigh.txt

mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done HighHigh"