#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap = 0
    i = 0
    while i<n-1:
        if arr[i]!=i+1: #comparing element with index
            temp=arr[i] #store the element into a temporary list
            arr[i],arr[temp-1] = arr[temp-1],arr[i] #swaping with the element
            swap+=1 #swap count
        else:
            i+=1
    return swap 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
