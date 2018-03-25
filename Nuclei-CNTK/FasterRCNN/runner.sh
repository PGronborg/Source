#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start"

CUDA_VISIBLE_DEVICES=5,6 python run_faster_rcnn_VGG16.py 10 > TextOutput10.txt 2> err10.txt

mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done"
