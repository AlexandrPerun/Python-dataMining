import matplotlib.pyplot as plt     #Подключаем библиотеку matplotlib
from math import sqrt               #Подключаем библиотеку math
import csv                          #Импортируем csv-айл с данными
 
def csv_dict_reader(file_obj):      #Фунция для импорта данных из файла
    x = []                          #объявляем массив x
    y = []                          #объявляем массив y
    z = []                          #объявляем массив z
       
    reader = csv.DictReader(file_obj, delimiter=',')    #Метод для открытия csv-айла
    for line in reader:                                 #
        x.append(line["Sepal.Length"])                  #Добавление в массив x данных о длине чашелистика
        y.append(line["Petal.Length"])                  #Добавление в массив y данных о длине лепестка
        z.append(line["Species"])                       #Добавление в массив z данных о виде цветка
    return x, y, z
 
with open("iris.csv") as f_obj:                         #Экспортируем файл (файл взятс сайта: http://archive.ics.uci.edu/ml/datasets/Iris)
    sepal, petal, species = csv_dict_reader(f_obj)      #Присваивание переменным sepal, petal, species соответствующех данных из файла
for i in range(len(sepal)):
    sepal[i]=float(sepal[i])
    petal[i]=float(petal[i])

color = []                          #Объявляем массив color
for i in species:                   #Перебирая массив species 
    if i == "setosa":               
        color.append('yellow')      #Присваеваем жёлтый цвет виду setosa
    elif i == "versicolor":         
        color.append('green')       #Присваеваем жёлтый цвет виду versicolor
    elif i == "virginica":          
        color.append('blue')        #Присваеваем жёлтый цвет виду virginica
    
x = float(input('Input sepal length in cm: '))                #Запрашиваем у пользователя длину чашелистика "нового растения"
y = float(input('Input petal length in cm: '))                #Запрашиваем у пользователя длину лепестка "нового растения"
k = int(input('Input number of neighbours: '))           #Запрашиваем у пользователя колличество ближайших соседей

d = []                              #Объявляем массив d

for i in range(len(sepal)):                                                                 
    d.append([((float(sepal[i]) - x)**2 + (float(petal[i]) - y)**2)**0.5, color[i]])        # Добавляем в массив d эвклидовы расстояния от "нового растения"
                                                                                            # до растений из csv-файла с данными и цвета
                                                                                            # x и y координаты это длины чашелитика и лепестка соответственно
d.sort()                    # Сортируем массив d 

d = d[:k]                   # Отбираем к расстояний (к-количество соседей)

votes = [[0,'yellow'],[0,'green'],[0,'blue']]           #Объявляем двумерный массив votes
for i in d:                                             #Проводим взвешенное голосование расстояний в массиве d. Проводим посчёт голосов.
    if i[1] == 'yellow' and i[0]!=0:                    
        votes[0][0] += 1/i[0]                           
    elif i[1] == 'green' and i[0]!=0:                   
        votes[1][0] += 1/i[0]                           
    elif i[1] == 'blue' and i[0]!=0:                    
        votes[2][0] += 1/i[0]                           
votes.sort()                                            #Сортируем массив votes
votes.reverse()                                         #Реверсируем отсортированный массив votes

sepal.append(float(x))                                    #Добавляем нашу длину чашелистика в массив sepal
petal.append(float(y))                                    #Добавляем нашу длину лепестка в массив petal
color.append('red')                                     #Добавляем цвет red в массив color

title = 'yellow - setosa, green - versicolor, blue - virginica' #Делаем подпись Цвет-Вид в окне с диаграммой классов
plt.scatter(sepal, petal, c = color)                    #Строим диаграмму зависимости длины чашелистика от длины лепестка.

if votes[0][1] == 'yellow':                             #Определяем вид растения исходя из колличества голосов за цвет. Выводим пользователю название вида в консоль и на график.
    plt.scatter(x, y, c = 'red', label='new object is "Iris-setosa"')    #Классы обозначаем цветами в зависимости от вида растения.
    print('Element classified as "Iris-setosa"')                         #Точка, добавленная пользователем, будет отображена красным цветом
elif votes[0][1] == 'green' :
    plt.scatter(x, y, c = 'red', label='new object is "Iris-versicolor"')
    print('Element classified as "Iris-versicolor"')         
elif votes[0][1] == 'blue':
    plt.scatter(x, y, c = 'red', label='new object is "Iris-virginica"')
    print('Element classified as "Iris-virginica"')
                                                                                                                
plt.title(title)
plt.xlabel('sepal length')
plt.ylabel('petal length')
plt.xlim(min(sepal)-0.5, max(sepal)+0.5)
plt.ylim(min(petal)-0.5, max(petal)+0.5)
plt.legend()
plt.show()                                              #Метод построения диаграммы класов данных
