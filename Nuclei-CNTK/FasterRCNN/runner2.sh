#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start"

CUDA_VISIBLE_DEVICES=0 python run_faster_rcnn_VGG16.py > TextOutput2.txt

mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done"