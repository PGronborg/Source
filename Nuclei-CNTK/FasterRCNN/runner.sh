#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start"

time CUDA_VISIBLE_DEVICES=1 python run_faster_rcnn_VGG16.py TestRun2 > TextOutput12.txt 2> err12.txt

mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done"
