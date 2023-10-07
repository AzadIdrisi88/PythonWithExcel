import time
import pandas as pd
from selenium import webdriver


def readExcel():

    df = pd.read_csv('test.csv')
    name = df["name"]
    rollno = df["rollno"]
    math = df["math"]
    # money = df["money"]
    # print(asins)
    # print(countries)
    return name,rollno,math
name,rollno,math = readExcel()
print(name,rollno,math)

