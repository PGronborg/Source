#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start testrun"

#time CUDA_VISIBLE_DEVICES=0 python3 run_faster_rcnn_VGG16.py Layers/Ref pool2 drop7 > Output/Layers/RefOut.txt 2> Output/Layers/RefErr.txt &

#time CUDA_VISIBLE_DEVICES=1 python3 run_faster_rcnn_VGG16.py Layers/Start_Pool3 pool3 drop7 > Output/Layers/Start_Pool3Out.txt 2> Output/Layers/Start_Pool3Err.txt &

#time CUDA_VISIBLE_DEVICES=2 python3 run_faster_rcnn_VGG16.py Layers/Start_Pool4 pool4 drop7 > Output/Layers/Start_Pool4Out.txt 2> Output/Layers/Start_Pool4Err.txt &

#time CUDA_VISIBLE_DEVICES=1 python3 run_faster_rcnn_VGG16.py Layers/Last_Drop6 pool2 drop6 > Output/Layers/Last_Drop6Out.txt 2> Output/Layers/Last_Drop6Err.txt &
#time CUDA_VISIBLE_DEVICES=2 python3 run_faster_rcnn_VGG16.py Layers/Last_fc6 pool2 fc6 > Output/Layers/Last_Fc6ut.txt 2> Output/Layers/Last_Fc6Err.txt &
#time CUDA_VISIBLE_DEVICES=3 python3 run_faster_rcnn_VGG16.py Layers/Last_relu6 pool2 relu6 > Output/Layers/Last_Relu6Out.txt 2> Output/Layers/Last_Relu6Err.txt &

time CUDA_VISIBLE_DEVICES=0 python3 run_faster_rcnn_VGG16.py Ref/Ref_L2_0005 > Output/Ref/Ref_L2_0005Out.txt 2> Output/Ref/Ref_L2_0005Err.txt &

wait

mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done testrun"