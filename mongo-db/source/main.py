from pymongo import MongoClient
import random
from russian_names import RussianNames
import multiprocessing


def f(x, y):
    client = MongoClient()
    db = client['MongoDB']
    roomers = db['Main']
    tryfalse = [True, False]
    typerooms = ['На 3 человек', 'На 2 человек']
    mani = ['бюджет', 'контракт']
    payment = [1700, 2000, 1500, 1400]
    exit = ['Зашёл в общежитие', 'Вышел из общежитие']
    date = ['01.09.2018-31.08.2021', '01.09.2019-31.08.2021', '01.09.2020-31.08.2021', '01.09.2017-31.08.2021',
            '01.09.2016-31.08.2021']
    data = []
    j = 1
    floor = 1
    nomer = '0'
    nameid = 0
    x = int(x) - 99
    for o in range(x, y):
        for i in range(900):
            room = random.choice(typerooms)
            if room == 'На 3 человек':
                liferoom = random.randint(1, 3)
            else:
                liferoom = random.randint(1, 2)
            post_data = {
                'Идентификатор': int("451" + str(i + o)),
                'ФИО': RussianNames().get_person(),
                'Льготы': random.choice(tryfalse),
                'Вид обучения': random.choice(mani),
                'Сумма оплаты ': random.choice(payment),
                'Период посещения ': random.choice(exit),
                'Общежитие ': {'Местоположение': "Общежитие " + str(o),
                               'Количество комнат в здании': 180},
                'Комната': {'Номер комнаты': str(floor) + str(nomer), 'Тип комнаты': room,
                            'Проживающих': liferoom,
                            'Когда проводили дезинфекцию дата': str(random.randint(1, 31)) + '.03.2021',
                            'Клопы': random.choice(tryfalse),
                            'Предупреждения': random.randint(0, 3)},
                'Период с/по': random.choice(date)
            }
            nameid += 1
            if i % 5 == 0:
                j += 1
                nomer = j
                if j % 10 == 0:
                    nomer = '0' + str(j)
                if j % 15 == 0:
                    floor += 1
            data.append(post_data)
        roomers.insert_many(data)
        data = []
        print(o)


if __name__ == '__main__':

    procs = []
    numbers = [903, 1805, 2708, 3610, 4512, 5414]
    numbers = []
    for i in range(4000, 6000, 200):
        numbers.append(i)
    start = 1
    end = 902
    for index, number in enumerate(numbers):
        p = multiprocessing.Process(target=f, args=(number, number,))
        procs.append(p)
        p.start()

    for proc in procs:
        proc.join()
