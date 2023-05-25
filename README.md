# Getting quotes in real time
Получение котировок российских ценных бумаг в реальном времени и последующий технический анализ.
# Начало работы
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=pip+install+tinkoff-investments)](https://git.io/typing-svg)

Данную библиотеку (Tinkoff API V2) мы используем для получения котировок в реальном времени.
Сайт, с которого берём котировки прошлых лет: <a href="[https://daniilshat.ru/](https://www.finam.ru/profile/moex-akcii/sberbank_sber-smal/export/?market=1&em=2854944&token=&code=SBER&apply=0&df=1&mf=4&yf=2022&from=01.05.2022&dt=23&mt=4&yt=2023&to=23.05.2023&p=7&f=SBER_220501_230523&e=.csv&cn=SBER&dtf=4&tmf=3&MSOR=1&mstime=on&mstimever=1&sep=1&sep2=1&datf=1&at=1)" target="_blank">клик</a> 
Скачиваем котировки за столько лет, сколько нам надо, вставляем файл в код и запускаем. Код добавит отсутствующие котировки за указанный вами интервал (имейте ввиду, интервал ограничен самим API Tinkoff).
