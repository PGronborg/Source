#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start"

CUDA_VISIBLE_DEVICES=6 python run_faster_rcnn_VGG16.py > TextOutput2.txt 2> err2.txt

mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done"
