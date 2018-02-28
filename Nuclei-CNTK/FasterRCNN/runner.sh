#!/bin/bash 

CUDA_VISIBLE_DEVICES=7 python run_faster_rcnn_VGG16.py > TextOutput1.txt
clear
CUDA_VISIBLE_DEVICES=7 python run_faster_rcnn_VGG16.py >> TextOutput1.txt
clear
CUDA_VISIBLE_DEVICES=7 python run_faster_rcnn_VGG16.py >> TextOutput1.txt

mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done"