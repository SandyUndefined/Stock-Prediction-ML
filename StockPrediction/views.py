import pandas as pd
from django.shortcuts import render
from nsetools import Nse
from datetime import date
from .stocks import get_stock_data

nse = Nse()


def greet(request):
    return render(request, 'greet.html',)


def index(request):
    return render(request, 'index.html')

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
        return render(request, 'Predict.html', context)
    elif request.method == 'POST' and '_predict' in request.POST:
        return render(request, 'Predict.html')
    else:
        return render(request, 'index.html')