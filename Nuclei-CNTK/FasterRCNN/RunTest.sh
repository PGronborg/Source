#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start testrun"

#time CUDA_VISIBLE_DEVICES=0 python3 run_faster_rcnn_VGG16.py Layers/Ref pool2 drop7 > Output/Layers/RefOut.txt 2> Output/Layers/RefErr.txt &

#time CUDA_VISIBLE_DEVICES=1 python3 run_faster_rcnn_VGG16.py Layers/Start_Pool3 pool3 drop7 > Output/Layers/Start_Pool3Out.txt 2> Output/Layers/Start_Pool3Err.txt &

#time CUDA_VISIBLE_DEVICES=2 python3 run_faster_rcnn_VGG16.py Layers/Start_Pool4 pool4 drop7 > Output/Layers/Start_Pool4Out.txt 2> Output/Layers/Start_Pool4Err.txt &

#time CUDA_VISIBLE_DEVICES=1 python3 run_faster_rcnn_VGG16.py Layers/Last_Drop6 pool2 drop6 > Output/Layers/Last_Drop6Out.txt 2> Output/Layers/Last_Drop6Err.txt &
#time CUDA_VISIBLE_DEVICES=2 python3 run_faster_rcnn_VGG16.py Layers/Last_fc6 pool2 fc6 > Output/Layers/Last_Fc6ut.txt 2> Output/Layers/Last_Fc6Err.txt &
#time CUDA_VISIBLE_DEVICES=3 python3 run_faster_rcnn_VGG16.py Layers/Last_relu6 pool2 relu6 > Output/Layers/Last_Relu6Out.txt 2> Output/Layers/Last_Relu6Err.txt &
#time CUDA_VISIBLE_DEVICES=0 python3 run_faster_rcnn_VGG16.py Ref/Ref_1 > Output/Ref/Ref_1Out.txt 2> Output/Ref/Ref_1Err.txt &
#time CUDA_VISIBLE_DEVICES=2 python3 run_faster_rcnn_VGG16.py Ref/Ref_2 > Output/Ref/Ref_2Out.txt 2> Output/Ref/Ref_2Err.txt &
time CUDA_VISIBLE_DEVICES=6 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center_1/0_01 0.01 > Output/SigmaCenter/Center_1/Out/0_01.txt 2> Output/SigmaCenter/Center_1/Err/0_01.txt &
wait
time CUDA_VISIBLE_DEVICES=6 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center_1/0_1 0.1 > Output/SigmaCenter/Center_1/Out/0_1.txt 2> Output/SigmaCenter/Center_1/Err/0_1.txt &
wait
time CUDA_VISIBLE_DEVICES=6 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center_1/1 1 > Output/SigmaCenter/Center_1/Out/1.txt 2> Output/SigmaCenter/Center_1/Err/1.txt &
wait
time CUDA_VISIBLE_DEVICES=6 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center_1/10 10 > Output/SigmaCenter/Center_1/Out/10.txt 2> Output/SigmaCenter/Center_1/Err/10.txt &
wait
time CUDA_VISIBLE_DEVICES=6 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center_1/100 100 > Output/SigmaCenter/Center_1/Out/100.txt 2> Output/SigmaCenter/Center_1/Err/100.txt &


wait

mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done testrun"