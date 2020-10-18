from math import factorial, sqrt
import requests
import xml.etree.ElementTree as ET
import datetime


def formatNumber(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num


def addition(x, y):
    try:
        return float(x) + float(y)
    except ValueError:
        return 'Error'


def subtraction(x, y):
    try:
        return float(x) - float(y)
    except ValueError:
        return 'Error'


def multiplication(x, y):
    try:
        return float(x) * float(y)
    except ValueError:
        return 'Error'


def division(x, y):
    try:
        return float(x) / float(y)
    except ZeroDivisionError:
        return 'ZeroDivisionError'
    except ValueError:
        return 'Error'


def power(x, y):
    try:
        return float(x) ** float(y)
    except ValueError:
        return 'Error'


def root(x):
    try:
        return sqrt(float(x))
    except ValueError:
        return 'Error'


def fctrial(x):
    try:
        if float(x) >= 0:
            return factorial(float(x))
        else:
            return f'-{factorial(float(x) * -1)}'
    except ValueError:
        return 'Error'


def rate_from_cbrf():
    y, m, d = [i for i in str(datetime.date.today()).split('-')]

    url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={d}/{m}/{y}'
    r = requests.request('GET', url=url)

    root = ET.fromstring(r.text)

    rates = {}
    for i in root:
        rates[i[0].text] = [int(i[2].text), i[1].text, round(float(i[4].text.replace(',', '.')), 2)]
    return rates
