#!/bin/python3

import math
import os
import random
import re
import sys

 
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b


def bonAppetit(bill, k, b):
    # Write your code here 
    bill.pop(k)                     # remove the k element from list
    total = 0
    for ele in range(0, len(bill)):  # make sum of rest of the elements
        total = total + bill[ele]
    B_actual = total//2
    if B_actual == b:
        print("Bon Appetit")
    elif B_actual < b:
        result = b - B_actual
        print(result)

        

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
