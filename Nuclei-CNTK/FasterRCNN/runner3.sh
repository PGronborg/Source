#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start Tester1"

time CUDA_VISIBLE_DEVICES=0 python run_faster_rcnn_VGG16.py Tester1 0.00005  > Tester1.txt 2> errTester1.txt

mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done Tester1"