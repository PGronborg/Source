#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start"

CUDA_VISIBLE_DEVICES=7 python run_faster_rcnn_VGG16.py > TextOutput1.txt 2> err1.txt

mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done"