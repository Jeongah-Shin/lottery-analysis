# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from flask import Flask,render_template

rawData = pd.read_csv('lottery.csv', usecols=['round','date','first','second','third','fourth','fifth','sixth','bonus'])

app = Flask(__name__)

@app.route('/')
def count_frequency():
    arr1 = pd.read_csv('lottery.csv', usecols=['first']).T.values.tolist()[0]
    arr2 = pd.read_csv('lottery.csv', usecols=['second']).T.values.tolist()[0]
    arr3 = pd.read_csv('lottery.csv', usecols=['third']).T.values.tolist()[0]
    arr4 = pd.read_csv('lottery.csv', usecols=['fourth']).T.values.tolist()[0]
    arr5 = pd.read_csv('lottery.csv', usecols=['fifth']).T.values.tolist()[0]
    arr6 = pd.read_csv('lottery.csv', usecols=['sixth']).T.values.tolist()[0]
    arr_bonus = pd.read_csv('lottery.csv', usecols=['bonus']).T.values.tolist()[0]
    arr_all = arr1 + arr2 + arr3 + arr4 + arr5 + arr6 + arr_bonus

    r = range(1, 46)
    f = 1
    frequency = {}
    for f in r:
        frequency[f-1] = 0

    for temp in arr_all:
        frequency[temp-1] += 1

    result = []
    for i in frequency:
        print(str(i+1) + "의 갯수:" + str(frequency[i]))
        result.append(str(i+1) + "의 갯수:" + str(frequency[i]))

    re = ''
    for r in result :
        re = re + (r + '<br/>')
    print(re)

    return render_template('index.html', results=result)


if __name__ == '__main__':
    app.debug = True
    app.run()
