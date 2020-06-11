import io
import pandas as pd
import requests
from django.shortcuts import render
from nsetools import Nse
from datetime import date
from StockPrediction.stock_prediction import get_stock_data

nse = Nse()


def index(request):
    global data
    api_key = '1KVQW60J7LHPS12D'
    base_url = 'https://www.alphavantage.co/query?'
    function = 'TIME_SERIES_DAILY_ADJUSTED'

    url50 = 'https://archives.nseindia.com/content/indices/ind_nifty50list.csv'
    url100 = 'https://archives.nseindia.com/content/indices/ind_nifty100list.csv'
    url200 = 'https://archives.nseindia.com/content/indices/ind_nifty200list.csv'
    url500 = 'https://archives.nseindia.com/content/indices/ind_nifty500list.csv'

    sfifty = requests.get(url50).content
    shundred = requests.get(url100).content
    stwohundred = requests.get(url200).content
    sfivehundred = requests.get(url500).content

    nifty50 = pd.read_csv(io.StringIO(sfifty.decode('utf-8')))
    nifty100 = pd.read_csv(io.StringIO(shundred.decode('utf-8')))
    nifty200 = pd.read_csv(io.StringIO(stwohundred.decode('utf-8')))
    nifty500 = pd.read_csv(io.StringIO(sfivehundred.decode('utf-8')))

    nifty50 = nifty50['Symbol']
    nifty100 = nifty100['Symbol']
    nifty200 = nifty200['Symbol']
    nifty500 = nifty500['Symbol']

    stocks = nse.get_stock_codes()
    symbols = []
    raw = []
    price = []
    raw2 = []

    data = [nse.get_quote(stock) for stock in nifty100]
    for i in range(len(data)):
        symbols.append([data[i].get('symbol')])
    for x in symbols:
        raw.append(','.join(x))

    for j in range(len(data)):
        price.append([data[j].get('open')])
    for y in price:
        raw2.append(','.join(map(str,y)))
    data = zip(raw,raw2)

    # symbols.append(data['symbol'])
    # open = data['open']


    context = {
        'fifty': nifty50,
        'hundred': nifty100,
        'twohundred': nifty200,
        'fivehundred': nifty500,
        'stocks': data,

               }

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
