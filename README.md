# Getting quotes in real time
Получение котировок российских ценных бумаг в реальном времени и последующий технический анализ.
# Начало работы
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=pip+install+tinkoff-investments)](https://git.io/typing-svg)

Данную библиотеку (Tinkoff API V2) мы используем для получения котировок в реальном времени.
Сайт, с которого берём котировки прошлых лет - Finam.

Репозиторий содержит в себе файл requirements.txt

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=pip+install+-r+requirements.txt)](https://git.io/typing-svg)

Данной командой мы загружаем все необходимые библиотеки для работы с кодом.

Также для использования .env-файла необходимо удалить .example из названия. В этом файле Вам необходимо ввести необходимые значения переменных, а именно:
1) TOKEN - Введите свой токен от Tinkoff API
2) NEW_FIGI - Введите FIGI-код акции, котировки которой будете получать
3) STOCK - Введите название акции. Данная переменная влияет только на отображение названия акции на графике.


Скачиваем котировки за столько лет, сколько нам надо, вставляем файл в код и запускаем. Код добавит отсутствующие котировки за указанный вами интервал (имейте ввиду, интервал ограничен самим API Tinkoff).


Для удобства вместе с кодом загрузил файл, которым пользовался сам. (Название - "MOEX.SBER_SMAL_220501_230523 (2).csv")

# Пример работоспособности

В качестве примера возьмем котировки Сбербанка. Технический анализ был выполнен 25.05.2023

# Результат SMA-индикатора:
![Image alt](https://github.com/neznayu-hub/getting-quotes-in-realtime/blob/main/pictures/SMA.jpg)

# Результат RSI-индикатора:
![Image alt](https://github.com/neznayu-hub/getting-quotes-in-realtime/blob/main/pictures/RSI.jpg)

# Результат EMA-индикатора:
![Image alt](https://github.com/neznayu-hub/getting-quotes-in-realtime/blob/main/pictures/EMA.jpg)

# Связаться

В случае, если возникнут вопросы - можете написать мне в Discord: 

![Image alt](https://github.com/neznayu-hub/getting-quotes-in-realtime/blob/main/pictures/Discordik.jpg)
