#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start Exp SigRPN 1.5"

time CUDA_VISIBLE_DEVICES=0 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN1_5/SigDET0_5 1.5 0.5 > Output/SigmaCenter/Center0_5/SigRPN1_5/OutputSigDET0_5.txt 2> Output/SigmaCenter/Center0_5/SigRPN1_5/errSigDET0_5.txt &

time CUDA_VISIBLE_DEVICES=5 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN1_5/SigDET1 1.5 1 > Output/SigmaCenter/Center0_5/SigRPN1_5/OutputSigDET1.txt 2> Output/SigmaCenter/Center0_5/SigRPN1_5/errSigDET1.txt &

wait

time CUDA_VISIBLE_DEVICES=0 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN1_5/SigDET1_5 1.5 1.5 > Output/SigmaCenter/Center0_5/SigRPN1_5/OutputSigDET1_5.txt 2> Output/SigmaCenter/Center0_5/SigRPN1_5/errSigDET1_5.txt &

time CUDA_VISIBLE_DEVICES=5 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN1_5/SigDET2 1.5 2 > Output/SigmaCenter/Center0_5/SigRPN1_5/OutputSigDET2.txt 2> Output/SigmaCenter/Center0_5/SigRPN1_5/errSigDET2.txt &


wait

time CUDA_VISIBLE_DEVICES=0 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN1_5/SigDET5 1.5 5 > Output/SigmaCenter/Center0_5/SigRPN1_5/OutputSigDET5.txt 2> Output/SigmaCenter/Center0_5/SigRPN1_5/errSigDET5.txt &

time CUDA_VISIBLE_DEVICES=5 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN1_5/SigDET10 1.5 10 > Output/SigmaCenter/Center0_5/SigRPN1_5/OutputSigDET10.txt 2> Output/SigmaCenter/Center0_5/SigRPN1_5/errSigDET10.txt &


wait

time CUDA_VISIBLE_DEVICES=0 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN1_5/SigDET50 1.5 50 > Output/SigmaCenter/Center0_5/SigRPN1_5/OutputSigDET50.txt 2> Output/SigmaCenter/Center0_5/SigRPN1_5/errSigDET50.txt &

time CUDA_VISIBLE_DEVICES=5 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN1_5/SigDET100 1.5 100 > Output/SigmaCenter/Center0_5/SigRPN1_5/OutputSigDET100.txt 2> Output/SigmaCenter/Center0_5/SigRPN1_5/errSigDET100.txt &

#time CUDA_VISIBLE_DEVICES=2 python3 run_faster_rcnn_VGG16.py SigmaCenter/Tester2 0.00005 > Output/SigmaCenter/Tester2TextFile.txt 2> Output/SigmaCenter/errTester2.txt &

#time CUDA_VISIBLE_DEVICES=3 python3 run_faster_rcnn_VGG16.py SigmaCenter/Tester2 0.00005 > Output/SigmaCenter/Tester2TextFile.txt 2> Output/SigmaCenter/errTester2.txt &

#time CUDA_VISIBLE_DEVICES=4 python3 run_faster_rcnn_VGG16.py SigmaCenter/Tester2 0.00005 > Output/SigmaCenter/Tester2TextFile.txt 2> Output/SigmaCenter/errTester2.txt &

wait

mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done Exp SigRPN 1.5"