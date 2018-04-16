#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start Exp SigRPN 10"

time CUDA_VISIBLE_DEVICES=2 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN10/SigDET0_5 10.0 0.5 > Output/SigmaCenter/Center0_5/SigRPN10/OutputSigDET0_5.txt 2> Output/SigmaCenter/Center0_5/SigRPN10/errSigDET0_5.txt &

wait

time CUDA_VISIBLE_DEVICES=2 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN10/SigDET1 10.0 1 > Output/SigmaCenter/Center0_5/SigRPN10/OutputSigDET1.txt 2> Output/SigmaCenter/Center0_5/SigRPN10/errSigDET1.txt &

wait

time CUDA_VISIBLE_DEVICES=2 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN10/SigDET1_5 10.0 1.5 > Output/SigmaCenter/Center0_5/SigRPN10/OutputSigDET1_5.txt 2> Output/SigmaCenter/Center0_5/SigRPN10/errSigDET1_5.txt &

wait

time CUDA_VISIBLE_DEVICES=2 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN10/SigDET2 10.0 2 > Output/SigmaCenter/Center0_5/SigRPN10/OutputSigDET2.txt 2> Output/SigmaCenter/Center0_5/SigRPN10/errSigDET2.txt &


wait

time CUDA_VISIBLE_DEVICES=2 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN10/SigDET5 10.0 5 > Output/SigmaCenter/Center0_5/SigRPN10/OutputSigDET5.txt 2> Output/SigmaCenter/Center0_5/SigRPN10/errSigDET5.txt &

wait

time CUDA_VISIBLE_DEVICES=2 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN10/SigDET10 10.0 10 > Output/SigmaCenter/Center0_5/SigRPN10/OutputSigDET10.txt 2> Output/SigmaCenter/Center0_5/SigRPN10/errSigDET10.txt &


wait

time CUDA_VISIBLE_DEVICES=2 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN10/SigDET50 10.0 50 > Output/SigmaCenter/Center0_5/SigRPN10/OutputSigDET50.txt 2> Output/SigmaCenter/Center0_5/SigRPN10/errSigDET50.txt &

wait

time CUDA_VISIBLE_DEVICES=2 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN10/SigDET100 10.0 100 > Output/SigmaCenter/Center0_5/SigRPN10/OutputSigDET100.txt 2> Output/SigmaCenter/Center0_5/SigRPN10/errSigDET100.txt &

#time CUDA_VISIBLE_DEVICES=2 python3 run_faster_rcnn_VGG16.py SigmaCenter/Tester2 0.00005 > Output/SigmaCenter/Tester2TextFile.txt 2> Output/SigmaCenter/errTester2.txt &

#time CUDA_VISIBLE_DEVICES=3 python3 run_faster_rcnn_VGG16.py SigmaCenter/Tester2 0.00005 > Output/SigmaCenter/Tester2TextFile.txt 2> Output/SigmaCenter/errTester2.txt &

#time CUDA_VISIBLE_DEVICES=4 python3 run_faster_rcnn_VGG16.py SigmaCenter/Tester2 0.00005 > Output/SigmaCenter/Tester2TextFile.txt 2> Output/SigmaCenter/errTester2.txt &

wait

mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done Exp SigRPN 10"