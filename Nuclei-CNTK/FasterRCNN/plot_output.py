#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import csv
import matplotlib.pyplot as plt
import numpy as np

# Pre allocate containers
count = [0]*200
train_err = [0]*200
val_err = [0]*200
train_loss = [0]*200
train_loss2 = [0]*200
val_loss = [0]*200
counter = 0

# Read .csv file and extracting data
with open(sys.argv[1], 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        count[counter] = int(row['Count'])
        train_loss[counter] = float(row['Train Loss'])
        train_loss2[counter] = float(row['Train Loss2'])
        train_err[counter] = float(row['Train error'])
        val_loss[counter] = float(row['Val Loss'])
        val_err[counter] = float(row['Val error'])
        counter += 1

# Removing empty spaces
count = count[0:counter]
train_err = train_err[0:counter]
val_err = val_err[0:counter]
train_loss = train_loss[0:counter]
train_loss2 = train_loss2[0:counter]
val_loss = val_loss[0:counter]
axes = plt.gca()
# Plotting the results
plt.plot(count, train_err, 'c-'),plt.text(np.percentile(count,70.0), 0.75,'-- Training error',{'color': 'c','fontsize': 11}), axes.set_ylim([0,100])
plt.plot(count, val_err, 'm-'),plt.text(np.percentile(count,70.0), 0.70,'-- Validation error',{'color': 'm','fontsize': 11})

plt.plot(count, train_loss, 'r-'),plt.text(np.percentile(count,70.0), 0.90,'-- Training Loss',{'color': 'r','fontsize': 11}), axes.set_ylim([0,1])
plt.plot(count, val_loss, 'b-'),plt.text(np.percentile(count,70.0), 0.85,'-- Validation Loss',{'color': 'b','fontsize': 11})
plt.plot(count, train_loss2, 'g-'),plt.text(np.percentile(count,70.0), 0.80,'-- Training Loss2',{'color': 'g','fontsize': 11})
# Adding title and correct ticks
plt.title('Training vs. validation')
plt.xticks(count[0:-1:2])
plt.xlabel('Epoch')
#plt.ylabel('%')

# Setting legend
plt.text(np.percentile(count,70.0), 90,'-- Training error',{'color': 'r','fontsize': 11})
plt.text(np.percentile(count,70.0), 85,'-- Validation error',{'color': 'b','fontsize': 11})

# Displaying the plot
plt.show()