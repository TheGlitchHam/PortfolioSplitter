import yfinance as yf
import json

"""
    Small program to calulate current portfolio split /
    and give advice on where to invest next

    Will also save data and transactions

"""


{
    "current_values" : [{
        "symbol":"EUNL.DE", "count": 7, "quantifier": 0.5
    },{
        "symbol" : "EXSA.DE", "count": 3, "quantifier": 0.3
    },{
        "symbol": "IS3N.DE", "count": 1, "quantifier": 0.2
    }
],
    "history":{

    }
}

import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))


class PortfolioSplitter():

    def __init__(self) -> None:
        self.json_data = self.load_json()
        self.current_data = self.get_current_data(self.json_data)

    def __str__(self):
        return self.current_data.__str__()

    def get_current_data(self, data):

        all_positions = []
        total = 0

        for position in data["current_values"]:
            symbol = position["symbol"]
            ticker_info = yf.Ticker(symbol).info
            ticker_name = ticker_info['longName']
            ticker_price= ticker_info['regularMarketPrice']
            position_value = position["count"] * ticker_price
            quantifier = position["quantifier"]
            all_positions.append({"symbol": symbol, "name": ticker_name, "price": ticker_price, "position_value": position_value,"percent":0, "quantifier": quantifier})
            total += position_value

        for position in all_positions:
            position["percent"] = self.calc_percent(total, position["position_value"])

        return all_positions

    def calc_percent(self, total, position_value):
        percent = position_value / total *100
        return round(percent, 2)
        

    def load_json(self):
        with open("data.json") as dataJson:
            data = json.load(dataJson)
            dataJson.close()
            return data

    def print_next_invest(self):
        for position in self.current_data:
            if position["percent"]/100 < position["quantifier"]:
                print(f"Invest into {position['name']} next. Should be {position['quantifier']*100} %, is { position['percent']} %")

    def invest(self, symbol, amount):
        for entry in self.json_data["current_values"]:
            if entry["symbol"] == symbol:
                entry["count"] += amount
                self.save_json(self.json_data)

    def save_json(self, json_data):
        with open('data.json', 'w') as f:
            json.dump(json_data, f)


    def print_symbol_names(self):
        for position in self.current_data:
            print(f"Name: {position['name']} , Symbol: {position['symbol']}")