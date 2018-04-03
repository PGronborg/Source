#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start"

time CUDA_VISIBLE_DEVICES=0 python run_faster_rcnn_VGG16.py TestRun1 > TextOutput11.txt 2> err11.txt

mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done"
