import pandas as pd
from django.shortcuts import render
from nsetools import Nse
from datetime import date
from StockPrediction.stock_prediction import get_stock_data

nse = Nse()


def greet(request):
    return render(request, 'StockPrediction/greet.html',)


def index(request):
    if request.method == 'GET':
        global data
        symbols = []
        raw = []
        price = []
        raw2 = []
        open = []
        raw3 = []
        companay_name = []
        raw4 = []

        nifty50 = pd.read_csv('fifty.csv')
        nifty50 = nifty50['Symbol']

        data = [nse.get_quote(stock) for stock in nifty50]

        # Companay name
        for i in range(len(data)):
            companay_name.append([data[i].get('companyName')])

        for x in companay_name:
            raw4.append(','.join(x))

        # Symbol
        for i in range(len(data)):
            symbols.append([data[i].get('symbol')])

        for x in symbols:
            raw.append(','.join(x))

        # Open
        for i in range(len(data)):
            open.append([data[i].get('open')])

        for x in open:
            raw3.append(','.join(map(str, x)))

        # Last Price
        for j in range(len(data)):
            price.append([data[j].get('lastPrice')])

        for y in price:
            raw2.append(','.join(map(str, y)))

        data = zip(raw4, raw, raw3, raw2)

        context = {'stocks': data}

        return render(request, 'StockPrediction/index.html', context)
    else:
        return render(request, 'StockPrediction/greet.html')


def prediction(request):
    if request.method == 'POST' and 'stocks_id' in request.POST:
        stock_id = request.POST['stocks_id']
        stock = stock_id.upper()
        msg = get_stock_data(stock)
        today = date.today()
        print(msg)

        context = {
            'Predicted_data': msg,
            'name': stock,
            'date': today,
        }
        return render(request, 'StockPrediction/Predict.html', context)
    elif request.method == 'POST' and '_predict' in request.POST:
        return render(request, 'StockPrediction/Predict.html')
    else:
        return render(request, 'StockPrediction/index.html')
