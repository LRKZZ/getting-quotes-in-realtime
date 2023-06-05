import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from datetime import date
from tinkoff.invest import Client, RequestError, CandleInterval, HistoricCandle
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os


load_dotenv()

token = os.getenv('token')

newfigi = os.getenv('new_figi')

stock = os.getenv('stock')

plt.style.use('fivethirtyeight') #строка грубо говоря для красоты графика RSI
count_added_rows = 0 # объявляем счетчик добавленных строк

df = pd.read_csv('MOEX.SBER_SMAL_220501_230523 (2).csv', delimiter=',') # загружаем котировки ценной бумаги. Сайт с данными: https://www.finam.ru/profile/moex-akcii/gazprom/export/



def Stock_SMA(stock):  #функция SMA-индикатора
    global df
    current_date = str(date.today().day) + '/' + str(date.today().month) + '/' + str(date.today().year)
    SMA30 = pd.DataFrame()
    SMA30['Close Price'] = df['<CLOSE>'].rolling(window=30).mean()
    SMA90 = pd.DataFrame()
    SMA90['Close Price'] = df['<CLOSE>'].rolling(window=90).mean()
    data = pd.DataFrame()
    data['Stock'] = df['<CLOSE>']
    data['SMA30'] = SMA30['Close Price']
    data['SMA90'] = SMA90['Close Price']
    #Визуализируем
    plt.figure(figsize=(12.6, 4.6))
    plt.plot(data['Stock'], label=stock, alpha=0.35)
    plt.plot(SMA30['Close Price'], label='SMA30', alpha=0.35)
    plt.plot(SMA90['Close Price'], label='SMA90', alpha=0.35)
    plt.title(stock + ' history (SMA)')
    plt.xlabel('01/01/2022 - ' + current_date)
    plt.ylabel('Close price')
    plt.legend(loc='upper left')
    plt.show()


def Stock_EMA(stock): #функция EMA-индикатора
    global df
    current_date = str(date.today().day) + '/' + str(date.today().month) + '/' + str(date.today().year)
    EMA50 = pd.DataFrame()
    EMA50['Close Price'] = df['<CLOSE>'].ewm(span=50).mean()
    EMA200 = pd.DataFrame()
    EMA200['Close Price'] = df['<CLOSE>'].ewm(span=200).mean()
    EMA21 = pd.DataFrame()
    EMA21['Close Price'] = df['<CLOSE>'].ewm(span=21).mean()
    data = pd.DataFrame()
    data['Stock'] = df['<CLOSE>']
    data['EMA21'] = EMA21['Close Price']
    data['EMA50'] = EMA50['Close Price']
    data['EMA200'] = EMA200['Close Price']

    # Визуализируем
    plt.figure(figsize=(12.6, 4.6))
    plt.plot(data['Stock'], label=stock, alpha=0.35)
    plt.plot(EMA21['Close Price'], label='EMA21', alpha=0.35)
    plt.plot(EMA50['Close Price'], label='EMA50', alpha=0.35)
    plt.plot(EMA200['Close Price'], label='EMA200', alpha=0.35)
    plt.title(stock + ' history (EMA)')
    plt.xlabel('01/01/2022 - ' + current_date)
    plt.ylabel('Close price')
    plt.legend(loc='upper left')
    plt.show()

def Wilder(data, periods): #индикатор Уайлдера (так нигде и не был использован, просто сохранил на будущее)
    start = np.where(~np.isnan(data))[0][0]
    Wilder = np.array([np.nan] * len(data))
    Wilder[start + periods - 1] = data[start:(start + periods)].mean()
    for i in range(start + periods, len(data)):
        Wilder[i] = (Wilder[i - 1] * (periods - 1) + data[i]) / periods
    return (Wilder)




def Stock_RSI(stock): #Функция RSI-индикатора

    delta = df['<CLOSE>'].diff(1)
    delta.dropna(inplace=True)

    positive = delta.copy()
    negative = delta.copy()

    positive[positive < 0] = 0
    negative[negative > 0] = 0

    days = 14 # указываем интервал для подсчета среднего значения и убытка

    average_gain = positive.rolling(window=days).mean() # Средняя длина растущих свечек
    average_loss = abs(negative.rolling(window=days).mean()) # Средняя длина падающих свечек

    relative_strength = average_gain / average_loss # частное от среднего значения роста цены и среднего значения снижения цены за период переменной days (по желанию можно поменять, но самый актуальный вариант - 14)
    RSI = 100.0 - (100.0 / (1.0 + relative_strength)) #основная формула RSI

    combined = pd.DataFrame()
    combined['<CLOSE>'] = df['<CLOSE>']
    combined['RSI'] = RSI
    #Визуализируем
    plt.figure(figsize=(12, 8))
    ax1 = plt.subplot(211)
    ax1.plot(combined.index, combined['<CLOSE>'], color='lightgray')
    ax1.set_title("Adjusted Close Price", color='white')

    ax1.grid(True, color='#555555')
    ax1.set_axisbelow(True)
    ax1.set_facecolor('black')
    ax1.figure.set_facecolor('#121212')
    ax1.tick_params(axis='x', colors = 'white')
    ax1.tick_params(axis='y', colors = 'white')

    ax2 = plt.subplot(212, sharex=ax1)
    ax2.plot(combined.index, combined['RSI'], color='lightgray')
    #Закоментированные строки - RSI-индикаторы с другими показателями (показатель указан в начале скобок)
    #ax2.axhline(0, linestyle='--', alpha = 0.5, color = '#ff0000')
    #ax2.axhline(10, linestyle='--', alpha=0.5, color='#ffaa00')
    #ax2.axhline(20, linestyle='--', alpha=0.5, color='#00ff00')
    ax2.axhline(30, linestyle='--', alpha=0.5, color='#cccccc')
    ax2.axhline(70, linestyle='--', alpha=0.5, color='#cccccc')
    #ax2.axhline(80, linestyle='--', alpha=0.5, color='#00ff00')
    #ax2.axhline(90, linestyle='--', alpha=0.5, color='#ffaa00')
    #ax2.axhline(100, linestyle='--', alpha=0.5, color='#ff0000')

    ax2.set_title("RSI Value")
    ax2.grid(False)
    ax2.set_axisbelow(True)
    ax2.set_facecolor('black')
    ax2.tick_params(axis='x', colors='white')
    ax2.tick_params(axis='y', colors='white')
    plt.show()

while True:
    response = input("Введите 1, если хотите обновить котировки или 2, если хотите получить графики. Если хотите выйти из программы - введите любой другой символ")
    if response == "1":
        with open('MOEX.SBER_SMAL_220501_230523 (2).csv', "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            existing_dates_times = set()
            for row in csv_reader:
                if len(row) >= 4:  # проверяем, что есть столбцы DATE и TIME
                    existing_dates_times.add((row[3], row[2]))  # меняем порядок элементов в кортеже

        try:
            with Client(token) as client: #обращаемся к API-Tinkoff, получая котировки
                check = client.market_data.get_candles(
                    figi = newfigi,
                    from_ = datetime.utcnow() - timedelta(days=7), #Указываем интервал котировок (неделя от времени запуска кода)
                    to=datetime.utcnow(),
                    interval=CandleInterval.CANDLE_INTERVAL_HOUR #Указываем, что хотим получать ежечасные котировки (например, чтобы указать минутные, пишем CANDLE_INTERVAL_1_MIN
                )
                with open('MOEX.SBER_SMAL_220501_230523 (2).csv', "a") as csv_file: # открываем файл для работы с ним
                    csv_writer = csv.writer(csv_file, delimiter=",")

                    for candle in check.candles:
                        # в этих трёх строках преобразовываем дату и время так, чтобы они совпадали с форматом ввода в csv-файле
                        datetime_str = candle.time.replace(microsecond=0).isoformat() + 'Z'
                        date_str = datetime_str.split('T')[0]
                        time_str = datetime_str.split('T')[1].replace('Z', '')
                        date_value = datetime.strptime(date_str, "%Y-%m-%d").strftime('%d/%m/%y')

                        # Форматируем время в нужный формат
                        time_value = datetime.strptime(time_str, '%H:%M:%S%z').strftime("%H:%M:%S")

                        # Объединяем дату и время в кортеж
                        date_time = (time_value, date_value) # меняем порядок элементов в кортеже

                        # проверяем, есть ли уже такая строка в файле
                        if (time_value, date_value) not in existing_dates_times: # проверяем наличие элементов в кортеже
                            # если нет - записываем новую строку в файл и добавляем ее дату и время в набор existing_dates_times
                            open_value = candle.open.units + (candle.open.nano / 1000000000) # "/ 1000000000" используется, чтобы нормально выводились полученные копейки
                            high_value = candle.high.units + (candle.high.nano / 1000000000)
                            low_value = candle.low.units + (candle.low.nano / 1000000000)
                            close_value = candle.close.units + (candle.close.nano / 1000000000)
                            volume_value = candle.volume
                            new_row = ["MOEX.SBER:SMAL", "60", date_value, time_value, open_value, high_value, low_value,
                                    close_value, volume_value] #формируем новую строку, чтобы добавить её в файл

                            csv_writer.writerow(new_row)
                            existing_dates_times.add((time_value, date_value)) # добавляем элементы в кортеж
                            count_added_rows += 1 # пополняем счетчик строк
                    print(f"Было добавлено {count_added_rows} строк")

        except RequestError as e:
            print("Ошибка при обращении к API:", e)
    elif response == "2":
        Stock_SMA(stock)
        Stock_EMA(stock)
        Stock_RSI(stock)
    else:
        break




