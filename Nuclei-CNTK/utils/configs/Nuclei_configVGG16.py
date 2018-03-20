# Copyright (c) Microsoft. All rights reserved.

# Licensed under the MIT license. See LICENSE.md file in the project root
# for full license information.
# ==============================================================================

# `pip install easydict` if you don't have it
from easydict import EasyDict as edict

__C = edict()
__C.DATA = edict()
cfg = __C

# data set config
__C.DATA.DATASET = "NucleiVGG16"
#__C.DATA.MAP_FILE_PATH = "/scratch/s124262"
#__C.DATA.CLASS_MAP_FILE = "class_map.txt"
#__C.DATA.TRAIN_MAP_FILE = "train_256_20XX/trainval_nuclei.txt"
#__C.DATA.TRAIN_ROI_FILE = "train_256_20XX/trainval_nuclei_roi.txt"
#__C.DATA.VAL_MAP_FILE = "test_256_20XX/valval_nuclei.txt"
#__C.DATA.VAL_ROI_FILE = "test_256_20XX/valval_nuclei_roi.txt"
#__C.DATA.TEST_MAP_FILE = "test_256_20XX/testval_nuclei.txt"
#__C.DATA.TEST_ROI_FILE = "test_256_20XX/testval_nuclei_roi.txt"
#__C.DATA.NUM_TRAIN_IMAGES = 347400
#__C.DATA.NUM_TEST_IMAGES = 50300
#__C.DATA.NUM_VAL_IMAGES = 50300
#__C.DATA.EPOCH_SIZE = 347400
# __C.DATA.VAL_SIZE = 50300
__C.DATA.MAP_FILE_PATH = "../Sampled Test"
__C.DATA.CLASS_MAP_FILE = "class_map.txt"
__C.DATA.TRAIN_MAP_FILE = "trainval_nuclei.txt"
__C.DATA.TRAIN_ROI_FILE = "trainval_nuclei_roi.txt"
__C.DATA.VAL_MAP_FILE = "valval_nuclei.txt"
__C.DATA.VAL_ROI_FILE = "valval_nuclei_roi.txt"
__C.DATA.TEST_MAP_FILE = "testval_nuclei.txt"
__C.DATA.TEST_ROI_FILE = "testval_nuclei_roi.txt"
__C.DATA.NUM_TRAIN_IMAGES = 320
__C.DATA.NUM_TEST_IMAGES = 96
__C.DATA.NUM_VAL_IMAGES = 64
__C.DATA.EPOCH_SIZE = 320
__C.DATA.VAL_SIZE = 64
__C.DATA.PROPOSAL_LAYER_SCALES = [2, 3, 4]

# overwriting proposal parameters for Fast R-CNN
# minimum relative width/height of an ROI
__C.roi_min_side_rel = 0.01
# maximum relative width/height of an ROI
__C.roi_max_side_rel = 0.04
# minimum relative area of an ROI
__C.roi_min_area_rel = 2 * __C.roi_min_side_rel * __C.roi_min_side_rel
# maximum relative area of an ROI
__C.roi_max_area_rel = 0.33 * __C.roi_max_side_rel * __C.roi_max_side_rel
# maximum aspect ratio of an ROI vertically and horizontally
__C.roi_max_aspect_ratio = 1.0

# For this data set use the following lr factor for Fast R-CNN:
# __C.CNTK.LR_FACTOR = 10.0