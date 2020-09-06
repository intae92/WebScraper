import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

COUNTRY = 0
CURRENCY = 1
CURRENCY_CODE = 2
CURRENCY_NUMBER = 3
COUNTRY_INDEX = 4

inputCountry = []
country_arr = []
MAX_COUNTRY_LENGTH = 0

os.system("clear")
url = "https://www.iban.com/currency-codes"


def ask_number_your_country():
    target_index = input("#: ")
    try:
        idx = int(target_index)
        if idx > MAX_COUNTRY_LENGTH:
            print("Choose a number from the list")
            ask_number_your_country()
        else:
            inputCountry.append(country_arr[idx][CURRENCY_CODE].get_text())
            # f"{country_arr[idx][CURRENCY].get_text()}\n{country_arr[idx][CURRENCY_CODE].get_text()}")
            print(f"{country_arr[idx][CURRENCY].get_text()}\n")
            return
    except:
        print("That wasn't a number")
        ask_number_your_country()


def ask_number_choose_country():
    target_index = input("#: ")
    try:
        idx = int(target_index)
        if idx > MAX_COUNTRY_LENGTH:
            print("Choose a number from the list")
            ask_number_choose_country()
        else:
            inputCountry.append(country_arr[idx][CURRENCY_CODE].get_text())
            # f"{country_arr[idx][CURRENCY].get_text()}\n{country_arr[idx][CURRENCY_CODE].get_text()}")
            print(f"{country_arr[idx][CURRENCY].get_text()}\n")
            return
    except:
        print("That wasn't a number")
        ask_number_choose_country()


def currency_convertor():
    COUNTRY_NOW = inputCountry[0]
    COUNTRY_TARGET = inputCountry[1]
    money = input(
        f"How many {COUNTRY_NOW} do you want to convert to {COUNTRY_TARGET}\n")
    if money.isdigit():
        currencyUrl = f"https://transferwise.com/gb/currency-converter/{COUNTRY_NOW.lower()}-to-{COUNTRY_TARGET.lower()}-rate?amount={money}"
        result = requests.get(currencyUrl)
        soup = BeautifulSoup(result.text, "html.parser")
        exchange_rate = float(
            soup.find("span", {"class": "text-success"}).string)
        convert_money = exchange_rate * int(money)
        now_money = format_currency(int(money), COUNTRY_NOW, locale="ko_KR")
        target_money = format_currency(
            convert_money, COUNTRY_TARGET, locale="ko_KR")
        print(f"{COUNTRY_NOW}{now_money} is {target_money}")
    else:
        print("That wasn't a number\n")
        currency_convertor()


def printList():
    for target in country_arr:
        target_country_text = target[0].get_text()
        country_convert = target_country_text[0] + \
            target_country_text[1:].lower()
        print(f"# {target[COUNTRY_INDEX]} {country_convert}")

    print("\nWhere are you from? Choose a country by number\n")
    ask_number_your_country()
    print("\nNow choose another country\n")
    ask_number_choose_country()
    currency_convertor()


def main():
    print("Welcome to CurrencyConvert PRO 20000\n")
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    tbodyText = soup.find('tbody')
    for tr in tbodyText:
        if tr != '\n':
            td = tr.find_all('td')
            if len(td) == 4:
                td.append(len(country_arr))
                country_arr.append(td)

    global MAX_COUNTRY_LENGTH
    MAX_COUNTRY_LENGTH = len(country_arr)
    printList()


main()
