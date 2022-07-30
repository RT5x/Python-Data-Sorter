from data import dataset # Input data in datastr
from data import dataset_sorted 
import math
n = len(dataset)
# Calculate Mean:

def mean(dataset, n):
  sum = 0
  for i in range (0, n):
    sum += dataset_sorted[i]
  return sum / n
  

print("Mean: " + str(mean(dataset, n)))
mean = mean(dataset, n) 
#Calculate Median:
def median(dataset, n):
  if n%2 == 0:
    return (0.5 * (dataset_sorted[int(n/2 - 1)] + dataset_sorted[int(n/2)]))
  else:
    return dataset_sorted[(n - 1)/2]
print("Median: " + str(median(dataset, len(dataset))))

#Calculate Mode:
def mode(dataset, n):
  i = 0
  count = 0
  lst = []
  while i < n - 1:
    for j in range (0, n-1):
      if dataset[i] == dataset[j]:
        lst.append(dataset[i])
        i +=1
        count += 1
      else: 
        i+= 1
    
print("Mode: " + str(mode(dataset, n)))

#Calculate standard deviation
def stddev(dataset, n):
  sum1 = 0
  for i in range (0, n):
    sum1 += (dataset[i] - mean) ** 2
  return math.sqrt(sum1 / n)
  
print("Standard deviation: " + str(stddev(dataset, n)))

#Calculate max:
def max(dataset, n):
  return dataset_sorted[n-1]
print("Maximum value: " + str(max(dataset, n)))

#Calculate min:
def min(dataset, n):
  return dataset_sorted[0]
print("Minimum value: " + str(min(dataset, n)))

#Calculate range:
def range(dataset, n):
  return dataset_sorted[n - 1] - dataset_sorted[0]
print("Range: " + str(range(dataset, n)))

#Number of terms:
print("Number of terms: " + str(n))
