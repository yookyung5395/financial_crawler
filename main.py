import pywinmacro as pw
import time

location1 = (363,60)  #주소창
location2 = (215,109)  #검색창
location3 = (300, 300)  #Historical Data
location4 = (400, 400)  #Download

stocks = ["FB", "MSFT", "RIOT", "TSLA"]


def price(ticker):
    pw.click(location2)
    time.sleep(3)
    pw.type_in(ticker)
    time.sleep(3)
    pw.key_press_once("enter")
    time.sleep(3)
    pw.click(location3)
    time.sleep(3)
    pw.click(location4)
    time.sleep(3)


def get_price_data(stocks):
    for stock in stocks:
        price(stocks)
        time.sleep(3)


def go_to_yfinance():
    pw.click(location1)
    time.sleep(1)
    pw.type_in("https://finance.yahoo.com")
    time.sleep(1)
    pw.key_press_once("enter")
    time.sleep(1)


go_to_yfinance()

get_price_data(stocks)

