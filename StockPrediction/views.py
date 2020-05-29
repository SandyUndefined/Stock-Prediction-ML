import io

import requests
from django.shortcuts import render
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import pandas as pd
from django.template.loader import render_to_string
from math import pi
import datetime


def index(request):
    api_key = '1KVQW60J7LHPS12D'
    url50 = 'https://archives.nseindia.com/content/indices/ind_nifty50list.csv'
    url100 = 'https://archives.nseindia.com/content/indices/ind_nifty100list.csv'
    url200 = 'https://archives.nseindia.com/content/indices/ind_nifty200list.csv'
    sfifty = requests.get(url50).content
    shundred = requests.get(url100).content
    stwohundred = requests.get(url200).content
    nifty50 = pd.read_csv(io.StringIO(sfifty.decode('utf-8')))
    nifty100 = pd.read_csv(io.StringIO(shundred.decode('utf-8')))
    nifty200 = pd.read_csv(io.StringIO(stwohundred.decode('utf-8')))
    nifty50 = nifty50['Symbol']
    nifty100 = nifty100['Symbol']
    nifty200 = nifty200['Symbol']
    context = {
        'fifty': nifty50,
        'hundred': nifty100,
        'twohundred': nifty200
               }
    return render(request, 'StockPrediction/index.html', context)
