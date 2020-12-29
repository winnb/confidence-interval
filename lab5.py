# Brandon Winn
# EE 381
# Lab 5: Confidence Intervals
# 18 Dec 2020

import math as m
import matplotlib.pyplot as plt
import numpy as np
import random
import statistics

N = 1000000 # Given N value as 1,000,000
MEAN = 100 # Given mean value
SIGMA = 12 # Given standard deviation
SAMPLE_SIZE_MAX = 200

def task1(): # Plots random confidence intervals and sample means
    population = list(np.random.normal(MEAN, SIGMA, N)) # Create the population by generating normal dist
    sample_means = [] # Create list to hold sample mean values
    confidence_intervals_min_95 = [] # Create list to hold min confidence interval for 95%
    confidence_intervals_max_95 = [] # Create list to hold max confidence interval for 95%
    confidence_intervals_min_99 = [] # Create list to hold min confidence interval for 99%
    confidence_intervals_max_99 = [] # Create list to hold max confidence interval for 99%
    for sample_size in range(1,SAMPLE_SIZE_MAX+1): # Loop from 1 to 200
        sample = random.sample(population, sample_size) # Pick sample from population
        sample_means.append( statistics.mean(sample) ) # Calculate sample mean
        confidence_intervals_min_95.append( getConfidenceInterval(1.96, sample_size, "min") ) # Calculate confidence interval for 95%
        confidence_intervals_max_95.append( getConfidenceInterval(1.96, sample_size, "max") ) # Calculate confidence interval for 95%
        confidence_intervals_min_99.append( getConfidenceInterval(2.58, sample_size, "min") ) # Calculate confidence interval for 99%
        confidence_intervals_max_99.append( getConfidenceInterval(2.58, sample_size, "max") ) # Calculate confidence interval for 99%
    plotIntervals(sample_means, confidence_intervals_min_95, confidence_intervals_max_95, confidence_intervals_min_99, confidence_intervals_max_99) # Plot results

def getConfidenceInterval(z, sample_size, min_or_max): # Calculate bounds of confidence interval for sample
    if min_or_max=="min":
        return MEAN-z*SIGMA/m.sqrt(sample_size) # Calculate lower bound
    else:
      return MEAN+z*SIGMA/m.sqrt(sample_size) # Calculate upper bound

def plotIntervals(means, interval_min_95, interval_max_95, interval_min_99, interval_max_99): # Plot sample means and confidence intervals
    xList = [] # Create list to hold x values
    for i in range(200):
        xList.append(i)
    figureA = plt.subplot(1,2,1) # Create for 95% confidence interval
    figureA.set_title("Means & 95% Confid. Intervals") # Add title to chart
    plt.setp(figureA, xticks=[0,40,80,120,160,200], xlabel="Sample Size", yLabel="X_Bar") # Set x ticks
    figureA.plot(xList, means, 'bx', label='Mean Values') # Plot mean values for 95%
    figureA.plot(xList, interval_min_95, 'r') # Plot min range for 95%
    figureA.plot(xList, interval_max_95, 'r') # Plot max range for 95%

    figureB = plt.subplot(1,2,2) # Create for 99% confidence interval
    figureB.set_title("Means & 99% Confid. Intervals") # Add title to chart
    plt.setp(figureB, xTicks=[0,40,80,120,160,200], xLabel="Sample Size", yLabel="X_Bar") # Set x ticks
    figureB.plot(xList, means, 'gx') # Plot mean values for 99%
    figureB.plot(xList, interval_min_99, 'r') # Plot min range for 99%
    figureB.plot(xList, interval_max_99, 'r') # Plot max range for 99%

    plt.subplots_adjust(wspace=0.3) # Add space between subplots
    plt.show() # Show graphs
    plt.legend(loc='best') # Show labels

def task2():
    population = list(np.random.normal(MEAN, SIGMA, N)) # Create the population by generating normal dist
    pop_mean = statistics.mean(population) # Calculate population mean
    sample_sizes = [5,40,120] # Given sample sizes
    z_values = [1.96, 2.58, 2.78, 4.6] # Given z values
    counts = [0,0,0,0,0,0,0,0,0,0,0,0]  # List containing occurences of population mean being within 12 sample mean confidence intervals
    runs = 10000 # Given number of trials
    for k in range(runs):
      for i in range(len(sample_sizes)): # Loop through each sample size
          for j in range(len(z_values)): # Loop through each z value
              sample = random.sample(population, sample_sizes[i]) # Pick sample from population
              sample_mean = statistics.mean(sample) # Calculate sample mean
              sample_sigma = statistics.stdev(sample) # Calculate sample std dev
              mean_lower = sample_mean-z_values[j]*sample_sigma/m.sqrt(sample_sizes[i]) # Calculate lower sample confidence
              mean_upper = sample_mean+z_values[j]*sample_sigma/m.sqrt(sample_sizes[i]) # Calculate upper sample confidence
              if pop_mean>mean_lower and pop_mean<mean_upper: # If population mean is within sample confidence interval then add to count
                  addToCount(sample_sizes[i], z_values[j], counts) # Add to count
    xNum = 0 # Value used to iterate over counts
    for i in range(len(sample_sizes)): # Loop through each sample size
        for j in range(len(z_values)): # Loop through each z value
            print("N="+str(sample_sizes[i])+" Z="+str(z_values[j])+" "+str(counts[xNum]/runs))
            xNum += 1

def addToCount(N, Z, counts): # Add 1 to table of counts
    if N==5 and Z==1.96:
        counts[0] += 1
    elif N==5 and Z==2.58:
        counts[1] += 1
    elif N==5 and Z==2.78:
        counts[2] += 1
    elif N==5 and Z==4.6:
        counts[3] += 1
    elif N==40 and Z==1.96:
        counts[4] += 1
    elif N==40 and Z==2.58:
        counts[5] += 1
    elif N==40 and Z==2.78:
        counts[6] += 1
    elif N==40 and Z==4.6:
        counts[7] += 1
    elif N==120 and Z==1.96:
        counts[8] += 1
    elif N==120 and Z==2.58:
        counts[9] += 1
    elif N==120 and Z==2.78:
        counts[10] += 1
    elif N==120 and Z==4.6:
        counts[11] += 1
    return counts

print("Starting...")
task1()
#task2()