from data import dataset # Input data in datastr
from data import dataset_sorted 
import collections
import math

n = len(dataset)
print("Data Statistics: \n")
# Calculate Mean:
def mean(dataset, n):
  sum = 0
  for i in range (0, n):
    sum += dataset_sorted[i]
  return sum / n
print("Mean: " + str(mean(dataset, n)) + "\n")
mean = mean(dataset, n) 

#Calculate Median:
def median(dataset, n):
  if n%2 == 0:
    return (0.5 * (dataset_sorted[int(n/2 - 1)] + dataset_sorted[int(n/2)]))
  elif n%2 != 0:
    return dataset_sorted[int((n - 1)/2)]
print("Median: " + str(median(dataset, len(dataset))) + "\n")

#Calculate Mode:
def mode(dataset, n):
  data1 = collections.Counter(dataset)
  data_list = dict(data1)
  max_value = max(list(data1.values()))
  mode_val = [num for num, freq in data_list.items() if freq == max_value]
  if len(mode_val) == len(dataset):
     print("Mode: None\n")
  else:
     print("Mode: " + ''.join(map(str, mode_val)) + "\n")
mode(dataset, n)

#Calculate standard deviation
def stddev(dataset, n):
  sum1 = 0
  for i in range (0, n):
    sum1 += (dataset[i] - mean) ** 2
  return math.sqrt(sum1 / n)
print("Standard deviation: " + str(stddev(dataset, n)) + "\n")

#Calculate variance:
print("Variance: " + str(a ** 2) + "\n")

#Calculate max:
def max(dataset, n):
  return dataset_sorted[n-1]
print("Maximum value: " + str(max(dataset, n)) + "\n")

#Calculate min:
def min(dataset, n):
  return dataset_sorted[0]
print("Minimum value: " + str(min(dataset, n)) + "\n")

#Calculate range:
def range(dataset, n):
  return dataset_sorted[n - 1] - dataset_sorted[0]
print("Range: " + str(range(dataset, n)) + "\n")

#Number of terms:
print("Number of terms (n) : " + str(n) + "\n")
