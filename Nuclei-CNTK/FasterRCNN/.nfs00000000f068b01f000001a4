#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start Tester2"

time CUDA_VISIBLE_DEVICES=0 python run_faster_rcnn_VGG16.py Tester2 0.00005 > Tester2.txt 2> errTester2.txt

mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done Tester2"
