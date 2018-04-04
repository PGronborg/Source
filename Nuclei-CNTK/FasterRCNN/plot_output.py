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
        train_err[counter] = float(row['Train error'])*100
        val_err[counter] = float(row['Val error'])*100
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

# Setting legend
plt.text(count[-6], np.max(val_err),'-- Training error',{'color': 'r','fontsize': 11})
plt.text(count[-6], np.max(val_err)-0.7,'-- Validation error',{'color': 'b','fontsize': 11})

# Displaying the plot
plt.show()