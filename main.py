import pandas as pd
from pandas import Series, DataFrame
from flask import Flask

app = Flask(__name__)

@app.route('/')
def show_tables():
    rawData = pd.read_csv('lottery.txt', sep='\t')
    rawData.set_index(['round'],inplace = True)

    return rawData.to_html(classes='lottery_result')

if __name__ == '__main__':
    app.debug = True
    app.run()
