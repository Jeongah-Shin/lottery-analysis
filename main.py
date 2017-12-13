import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from flask import Flask,render_template

rawData = pd.read_csv('lottery.txt', sep='\t')
rawData.set_index(['round'], inplace=True)

app = Flask(__name__)

@app.route('/')
def show_tables():
    return render_template('index.html')

@app.route('/count')
def count_frequency():
    arr = ['']
    for ex in rawData:
        print (ex)
        arr.append(ex)
    return arr




if __name__ == '__main__':
    app.debug = True
    app.run()
