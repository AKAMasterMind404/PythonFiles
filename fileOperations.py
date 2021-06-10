import os
import csv
import datetime

off='FL_insurance_sample.csv'
tr='excelfile2.csv'

def keyGenerator(file):
    #file should be readable
    t = ''
    for i in file.readline():
        if i == ',':
            t += ' '
        else:
            t += i
    return t.split()
with open(tr,'r') as f:
    keys=keyGenerator(f)
    f=csv.reader(f)
    for i in f:
        print(i)