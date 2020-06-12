import io
import pandas as pd
import matplotlib.pyplot as plt
from django.shortcuts import render
from nsetools import Nse
from datetime import date
from StockPrediction.stock_prediction import get_stock_data

nse = Nse()


def greet(request):
    return render(request, 'StockPrediction/greet.html',)


def index(request):
    global data

    # url50 = 'https://archives.nseindia.com/content/indices/ind_nifty50list.csv'
    # url100 = 'https://archives.nseindia.com/content/indices/ind_nifty100list.csv'
    #
    # sfifty = requests.get(url50).content
    # shundred = requests.get(url100).content

    nifty50 = pd.read_csv('fifty.csv')
    # nifty100 = pd.read_csv(io.StringIO(shundred.decode('utf-8')))

    nifty50 = nifty50['Symbol']
    # nifty100 = nifty100['Symbol']

    symbols = []
    raw = []
    price = []
    raw2 = []

    data = [nse.get_quote(stock) for stock in nifty50]
    for i in range(len(data)):
        symbols.append([data[i].get('symbol')])
    for x in symbols:
        raw.append(','.join(x))

    for j in range(len(data)):
        price.append([data[j].get('open')])
    for y in price:
        raw2.append(','.join(map(str,y)))
    data = zip(raw, raw2)

    context = {'stocks': data}

    return render(request, 'StockPrediction/index.html', context)


def prediction(request):
    if request.method == 'POST':
        stock_id = request.POST['stocks_id']
        stock = stock_id.upper()
        msg = get_stock_data(stock)
        today = date.today()
        context = {
            'Predicted_data': msg,
            'name': stock,
            'date': today,
        }
        return render(request, 'StockPrediction/Predict.html', context)
    else:
        return render(request, 'StockPrediction/index.html')
