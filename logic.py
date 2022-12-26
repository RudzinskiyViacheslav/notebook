from datetime import datetime
from tkinter import *
import os
import pickle

#AllData = []
my_Data_Base = None
def data_Init():
    global AllData
    global my_Data_Base

    with open('DataBase.pickle', 'rb') as f:
        AllData = pickle.load(f)
    print(AllData)
    print(type(AllData))

    # name = 'Рудзинский Вячеслав Викторович'
    # adress = 'Южнобутовскя 113'
    # phone = '89346481674'
    # birth = '27.03.1999'
    # workplace = 'МГТУ Баумана'
    # position = 'Студент'
    # personality = 'Добрый'
    # qualities = 'Исполнительный'
    # correction_date = datetime(2022,12,23,12,34,18).strftime("%Y-%m-%d %H:%M:%S")
    #
    # name2 = 'Голубицкий Авдей Александрович'
    # adress2 = 'Лазарева 113'
    # phone2 = '89256481674'
    # birth2 = '23.12.1999'
    # workplace2 = 'МИИТ'
    # position2 = 'Студент'
    # personality2 = 'Тихий'
    # qualities2 = 'Гулена'
    # correction_date2 = datetime(2022,11,18,16,55,28).strftime("%Y-%m-%d %H:%M:%S")
    #
    # AllData.append({'name': name,'adress': adress, 'phone': phone, 'birth': birth,'workplace': workplace,
    #                 'position': position,'personality': personality,'qualities': qualities,'correction_date': correction_date})
    # AllData.append({'name': name2,'adress': adress2, 'phone': phone2, 'birth': birth2, 'workplace': workplace2,
    #                 'position': position2,'personality': personality2,'qualities': qualities2,'correction_date': correction_date2})

def data_Rewrite():
    global my_Data_Base
    global AllData

    with open('DataBase.pickle', 'wb') as f:
        pickle.dump(AllData, f)

def search_All_Data():
    result_Data = []
    index_Data = []
    i = 0

    for item in AllData:
        data_to_append = ''
        for value in item.values():
            data_to_append += str(value)
            data_to_append += ', '
        result_Data.append(data_to_append)
        index_Data.append(i)

        i += 1

    return result_Data, index_Data
def search_in_Data(text):
    result_Data= []
    index_Data = []
    i = 0
    flag = False

    for item in AllData:
        for value in item.values():
            if type(value) != datetime and text != '':
                if text in value:
                    flag = True

        if flag == True:
            data_to_append = ''
            for value in item.values():
                data_to_append += str(value)
                data_to_append += ', '
            result_Data.append(data_to_append)
            index_Data.append(i)

        flag = False
        i += 1

    return result_Data, index_Data

def sort_by_date(list_of_data):
    sorted_list = []
    for i in range (len(list_of_data)):
        sorted_list.append(list(list_of_data[i].split(', ')))
        sorted_list[i].pop()
        sorted_list[i][len(sorted_list[i])-1] = datetime.strptime(sorted_list[i][len(sorted_list[i])-1], "%Y-%m-%d %H:%M:%S")
    for i in range(len(sorted_list) - 1):
        for j in range(len(sorted_list) - i - 1):
            if sorted_list[j][len(sorted_list[i])-1] > sorted_list[j + 1][len(sorted_list[i])-1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    data_to_return = []
    for person in sorted_list:
        data_to_append = ''
        for item in person:
            data_to_append += str(item)
            data_to_append += ', '
        data_to_return.append(data_to_append)
    return data_to_return

def show_birth():
    result_Data = []
    current_Date = datetime.today()
    for item in AllData:
        if (datetime.strptime(item['birth'], "%d.%m.%Y")).day == current_Date.day:
            result_Data.append('Сегодня день рождения у {0}! Позвоните по номеру {1} '
                               'и поздравьте!'.format(item['name'], item['phone']))
            return result_Data

def update_Data(data_To_Update, index):
    AllData[index].update(data_To_Update)

def delete_Data_From_List(index):
    AllData.pop(index)

def create_Data_To_List(data):
    AllData.append(data)
