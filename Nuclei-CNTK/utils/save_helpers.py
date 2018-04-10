from __future__ import print_function
from builtins import str
import sys, os, time
import numpy as np
from builtins import range
import copy, textwrap
from PIL import Image, ImageFont, ImageDraw
from PIL.ExifTags import TAGS
import cntk
from cntk import input_variable, Axis
from utils.nms_wrapper import apply_nms_to_single_image_results
from utils.rpn.bbox_transform import regress_rois
import cv2 # pip install opencv-python


def save_data(evaluator, num_eval, results_base_path, cfg):

	with open(cfg["DATA"].TEST_MAP_FILE) as f:
		content = f.readlines()

	img_base_path = os.path.dirname(os.path.abspath(cfg["DATA"].TEST_MAP_FILE))

	img_file_names = [os.path.join(img_base_path, x.split('\t')[1]) for x in content]

	img_shape = (cfg.NUM_CHANNELS, cfg.IMAGE_HEIGHT, cfg.IMAGE_WIDTH)

	saver_file = os.path.join(cfg.OUTPUT_PATH, "{}.txt"
	                                 .format(cfg.SAVE_NAME))
	with open(saver_file, 'w') as txtf:
		for i in range(0, num_eval):
			img_path = img_file_names[i]
			out_cls_pred, out_rpn_rois, out_bbox_regr, dims = evaluator.process_image_detailed(img_path)
			labels = out_cls_pred.argmax(axis=1)
			scores = out_cls_pred.max(axis=1)

			# apply regression and nms to bbox coordinates
			regressed_rois = regress_rois(out_rpn_rois, out_bbox_regr, labels, dims)
			nmsKeepIndices = apply_nms_to_single_image_results(regressed_rois, labels, scores,
			                                                   use_gpu_nms=cfg.USE_GPU_NMS,
			                                                   device_id=cfg.GPU_ID,
			                                                   nms_threshold=cfg.RESULTS_NMS_THRESHOLD,
			                                                   conf_threshold=cfg.RESULTS_NMS_CONF_THRESHOLD)

			filtered_bboxes = regressed_rois[nmsKeepIndices]
			filtered_labels = labels[nmsKeepIndices]
			filtered_scores = scores[nmsKeepIndices]

			txtString = ""
			for roiIndex in range(len(filtered_bboxes)):
				label = filtered_labels[roiIndex]
				if filtered_scores is not None:
					score = filtered_scores[roiIndex]
					if cfg.RESULTS_BGR_PLOT_THRESHOLD and score < cfg.RESULTS_BGR_PLOT_THRESHOLD:
						label = 0

				rect = [i for i in filtered_bboxes[roiIndex]]
				rect[0] = int(max(0, min(img_shape[2], rect[0])))
				rect[1] = int(max(0, min(img_shape[1], rect[1])))
				rect[2] = int(max(0, min(img_shape[2], rect[2])))
				rect[3] = int(max(0, min(img_shape[1], rect[3])))
				
				if label > 0:
					txtString = txtString + "{} {} {} {} {} {} ".format(str(rect[0]),str(rect[1]),str(rect[2]),str(rect[3]),str(label),str(score))

			txtf.write(txtString+"\n")
	return
