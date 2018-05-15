#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from openpyxl import load_workbook

fileEval = "/Users/Greenborg/Desktop/Source/Nuclei-CNTK/FasterRCNN/Output/"
file = "Ref/Ref_3_All.xlsx"
wb = load_workbook(fileEval+file)