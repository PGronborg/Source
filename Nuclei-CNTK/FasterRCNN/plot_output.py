#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 13:29:54 2018

@author: Greenborg
"""

import sys
import csv
import matplotlib.pyplot as plt

count = [0]*50
train_err = [0]*50
val_err = [0]*50
counter = 0
with open(sys.argv[1], 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        count[counter] = int(row['Count'])
        train_err[counter] = float(row['Train error'])*100
        val_err[counter] = float(row['Val error'])*100
        counter += 1

count = count[0:counter]
train_err = train_err[0:counter]
val_err = val_err[0:counter]

plt.plot(count, train_err, 'r-', count, val_err, 'b-')
plt.title('Training vs. validation')
plt.show()