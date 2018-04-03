#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start HighLow"

time CUDA_VISIBLE_DEVICES=1 python run_faster_rcnn_VGG16.py HighLow [0.001]*200 0.000005  > HighLow.txt 2> errHighLow.txt

mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done HighLow"