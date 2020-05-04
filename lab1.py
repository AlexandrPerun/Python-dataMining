import pandas as pd 				#Подключаем библиотеку pandas для импортирования csv-файлов
import matplotlib.pyplot as plt 	#Подключаем matplotlib для построения графиков

data = pd.read_csv('data2.csv', delimiter=';')		#Экспортируем файл с данными
plt.xlabel ('Рейтинг')								#Добавляем подпись "Рейтинг" для оси Х
plt.ylabel ('Возрастной рейтинг, Жанр')				#Добавляем подписи "Возрастной рейтинг" и "Жанр" для оси У
plt.title('Зависимость рейтинга от жанра и возрастного рейтинга игры') 	#Добавляем подпись для графика

plt.plot(data['Rating'], data['Content Rating'], color='yellow', LineWidth='2')					#Для графика зависимости Рейтинга от Возрастного рейтинга указываем данные, задаем желтый цвет и толщину 2
plt.plot(data['Rating'], data['Genres'], color='red', LineWidth='2')							#Для графика зависимости Рейтинга от Жанра указываем данные, задаем красный цвет графика и толщину 2
plt.scatter(data['Rating'], data['Content Rating'], color='yellow', LineWidth='4', marker='x')	#Для того, чтобы толщина маркеров на графиках отличалась, строим новый точечный график с толщиной 4
plt.scatter(data['Rating'], data['Genres'], color='red', LineWidth='4', marker='x')				#и маркером "Х"

plt.show()		#Строим график

