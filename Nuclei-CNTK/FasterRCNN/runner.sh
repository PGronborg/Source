#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start Tester2"

time CUDA_VISIBLE_DEVICES=0 python3 run_faster_rcnn_VGG16.py SigmaCenter/Tester2 0.00005 > Output/SigmaCenter/Tester2TextFile.txt 2> Output/SigmaCenter/errTester2.txt

mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done Tester2"
