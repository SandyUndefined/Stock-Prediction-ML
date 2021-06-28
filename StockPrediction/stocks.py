import os
import pathlib
import joblib
import pandas as pd
from sklearn import linear_model
from nsetools import Nse

nse = Nse()


def get_nse_data(name):
    data = nse.get_quote(name)
    current = [data['open'], data['dayHigh'], data['dayLow']]
    return current


def model_check(name):
    path = pathlib.Path(os.getcwd()+ "\\data\\saved_data\\"+name+'.pkl')
    if path.exists():
        return True
    else:
        return False


def get_stock_data(name):
    try:
        if model_check(name) == False:
            data_path = os.getcwd()+"\\StockPrediction\\data\\HISTORICAL_DATA\\"
            df = pd.read_csv(data_path + name + '_data.csv')
            df.fillna(df.mean(), inplace=True)
            X = df.iloc[:, [1, 2, 3]]
            Y = df.iloc[:, [4]]

            reg = linear_model.LinearRegression()
            reg.fit(X,Y)
            y_today = reg.predict([get_nse_data(name)])

            model_path = os.getcwd() + "\\StockPrediction\\data\\saved_data\\"
            file = model_path + name + ".pkl"
            joblib.dump(reg, file)
            return y_today[0][0]
        else:
            model_path = os.getcwd()+"\\StockPrediction\\data\\saved_data\\"
            file = model_path + name+".pkl"
            model = joblib.load(file)
            y_today = model.predict([get_nse_data(name)])
            return y_today
    except:
        return ("Error")