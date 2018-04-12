#!/bin/bash 
mail -s 'Starting'  peter.gronborg.7@gmail.com <<< "Start Exp SigRPN 2"

time CUDA_VISIBLE_DEVICES=0 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN2/SigDET0_5 2.0 0.5 > Output/SigmaCenter/Center0_5/SigRPN2/OutputSigDET0_5.txt 2> Output/SigmaCenter/Center0_5/SigRPN2/errSigDET0_5.txt &

wait

time CUDA_VISIBLE_DEVICES=0 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN2/SigDET1 2.0 1 > Output/SigmaCenter/Center0_5/SigRPN2/OutputSigDET1.txt 2> Output/SigmaCenter/Center0_5/SigRPN2/errSigDET1.txt &

wait

time CUDA_VISIBLE_DEVICES=0 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN2/SigDET1_5 2.0 1.5 > Output/SigmaCenter/Center0_5/SigRPN2/OutputSigDET1_5.txt 2> Output/SigmaCenter/Center0_5/SigRPN2/errSigDET1_5.txt &

wait

time CUDA_VISIBLE_DEVICES=0 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN2/SigDET2 2.0 2 > Output/SigmaCenter/Center0_5/SigRPN2/OutputSigDET2.txt 2> Output/SigmaCenter/Center0_5/SigRPN2/errSigDET2.txt &


wait

time CUDA_VISIBLE_DEVICES=0 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN2/SigDET5 2.0 5 > Output/SigmaCenter/Center0_5/SigRPN2/OutputSigDET5.txt 2> Output/SigmaCenter/Center0_5/SigRPN2/errSigDET5.txt &

wait

time CUDA_VISIBLE_DEVICES=0 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN2/SigDET10 2.0 10 > Output/SigmaCenter/Center0_5/SigRPN2/OutputSigDET10.txt 2> Output/SigmaCenter/Center0_5/SigRPN2/errSigDET10.txt &


wait

time CUDA_VISIBLE_DEVICES=0 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN2/SigDET50 2.0 50 > Output/SigmaCenter/Center0_5/SigRPN2/OutputSigDET50.txt 2> Output/SigmaCenter/Center0_5/SigRPN2/errSigDET50.txt &

wait

time CUDA_VISIBLE_DEVICES=0 python3 run_faster_rcnn_VGG16.py SigmaCenter/Center0_5/SigRPN2/SigDET100 2.0 100 > Output/SigmaCenter/Center0_5/SigRPN2/OutputSigDET100.txt 2> Output/SigmaCenter/Center0_5/SigRPN2/errSigDET100.txt &

#time CUDA_VISIBLE_DEVICES=2 python3 run_faster_rcnn_VGG16.py SigmaCenter/Tester2 0.00005 > Output/SigmaCenter/Tester2TextFile.txt 2> Output/SigmaCenter/errTester2.txt &

#time CUDA_VISIBLE_DEVICES=3 python3 run_faster_rcnn_VGG16.py SigmaCenter/Tester2 0.00005 > Output/SigmaCenter/Tester2TextFile.txt 2> Output/SigmaCenter/errTester2.txt &

#time CUDA_VISIBLE_DEVICES=4 python3 run_faster_rcnn_VGG16.py SigmaCenter/Tester2 0.00005 > Output/SigmaCenter/Tester2TextFile.txt 2> Output/SigmaCenter/errTester2.txt &

wait

mail -s 'Finished'  peter.gronborg.7@gmail.com <<< "Done Exp SigRPN 2"