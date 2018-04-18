#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start testrun"

time CUDA_VISIBLE_DEVICES=0 python3 run_faster_rcnn_VGG16.py Layers/Ref pool2 drop7 > Output/Layers/RefOut.txt 2> Output/Layers/RefErr.txt &

time CUDA_VISIBLE_DEVICES=1 python3 run_faster_rcnn_VGG16.py Layers/Start_Pool3 pool3 drop7 > Output/Layers/Start_Pool3Out.txt 2> Output/Layers/Start_Pool3Err.txt &

time CUDA_VISIBLE_DEVICES=2 python3 run_faster_rcnn_VGG16.py Layers/Start_Pool4 pool4 drop7 > Output/Layers/Start_Pool4Out.txt 2> Output/Layers/Start_Pool4Err.txt &

time CUDA_VISIBLE_DEVICES=3 python3 run_faster_rcnn_VGG16.py Layers/Last_Drop6 pool2 drop6 > Output/Layers/Last_Drop6Out.txt 2> Output/Layers/Last_Drop6Err.txt &
wait

mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done testrun"