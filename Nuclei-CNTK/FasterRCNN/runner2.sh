#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start Fail"

time CUDA_VISIBLE_DEVICES=7 python3 run_faster_rcnn_VGG16.py Fail 0.0005 > Fail.txt 2> errFail.txt &
wait
mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done Fail"