#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the MinSliceWeight function below.
def MinSliceWeight(Matrix):
    N = len(Matrix[0])
    j = Matrix[0].index(min(Matrix[0]))
    ans = [min(Matrix[0])]
    for i in range(N-1):
        cal = []
        cal_num = []
        if j != 0:
            cal.append(j-1,Matrix[i+1][j-1])
            cal_num.append(j-1)
        if j != N-1:
            cal.append(Matrix[i+1][j+1])
            cal_num.append(j+1)
        cal.append(Matrix[i+1][j])
        cal_num.append(j)
                   
        for value, num in zip(cal, cal_num):
            if min(cal) == value:
                ans.append(value)
                j = num
    return sum(ans)
        
    
if __name__ == '__main__':
    
    Matrix_rows = int(input().strip())
    Matrix_columns = int(input().strip())

    Matrix = []
    cal = 0
    ans = []

    for _ in range(Matrix_rows):
        Matrix.append(list(map(int, input().rstrip().split())))

    res = MinSliceWeight(Matrix)

    print(res)
