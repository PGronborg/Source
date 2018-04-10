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
counter = 0

# Read .csv file and extracting data
with open(sys.argv[1], 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        count[counter] = int(row['Count'])
        train_err[counter] = float(row['Train Loss'])*100
        val_err[counter] = float(row['Val Loss'])*100
        counter += 1

# Removing empty spaces
count = count[0:counter]
train_err = train_err[0:counter]
val_err = val_err[0:counter]

# Plotting the results
plt.plot(count, train_err, 'r-', count, val_err, 'b-')
# Adding title and correct ticks
plt.title('Training vs. validation')
plt.xticks(count[0:-1:2])
axes = plt.gca()
axes.set_ylim([0,100])
plt.xlabel('Epoch')
plt.ylabel('%')

# Setting legend
plt.text(np.percentile(count,70.0), 90,'-- Training error',{'color': 'r','fontsize': 11})
plt.text(np.percentile(count,70.0), 85,'-- Validation error',{'color': 'b','fontsize': 11})

# Displaying the plot
plt.show()