import time
import pandas as pd
from selenium import webdriver

from sklearn import tree
import matplotlib.pyplot as plt


def readExcel():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)


    df = pd.read_csv('test.csv')
    rollno = df["rollno"]
    name = df["name"]
    english = df["english"]
    physics = df["physics"]
    math = df["math"]
    print(df)
    return name, english, physics, rollno, math


name, english, physics, rollno, math = readExcel()
# print( name,rollno,chemistry, physics, math)
sub=(english, physics,math,rollno)
print('sub = ',sub)
# marks = [[x] for x in sub]
# print(rollno)
# for r in rollno:
#     print(r)