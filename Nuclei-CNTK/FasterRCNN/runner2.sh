#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start High"

time CUDA_VISIBLE_DEVICES=1 python run_faster_rcnn_VGG16.py Fail 0.0005 > Fail.txt 2> errFail.txt &
time CUDA_VISIBLE_DEVICES=2 python run_faster_rcnn_VGG16.py Fail2 0.0005 > Fail2.txt 2> errFail2.txt &
wait
mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done High"