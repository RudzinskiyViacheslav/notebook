import pickle
from datetime import datetime

# with open('DataBase.pickle', 'rb') as f:
#     All = pickle.load(f)

AllData = []
name = 'Рудзинский Вячеслав Викторович'
adress = 'Южнобутовскя 113'
phone = '89346481674'
birth = '27.03.1999'
workplace = 'МГТУ Баумана'
position = 'Студент'
personality = 'Добрый'
qualities = 'Исполнительный'
correction_date = datetime(2022,12,23,12,34,18).strftime("%Y-%m-%d %H:%M:%S")

name2 = 'Голубицкий Авдей Александрович'
adress2 = 'Лазарева 113'
phone2 = '89256481674'
birth2 = '23.12.1999'
workplace2 = 'МИИТ'
position2 = 'Студент'
personality2 = 'Тихий'
qualities2 = 'Гулена'
correction_date2 = datetime(2022,11,18,16,55,28).strftime("%Y-%m-%d %H:%M:%S")

AllData.append({'name': name,'adress': adress, 'phone': phone, 'birth': birth,'workplace': workplace,
                'position': position,'personality': personality,'qualities': qualities,'correction_date': correction_date})
AllData.append({'name': name2,'adress': adress2, 'phone': phone2, 'birth': birth2, 'workplace': workplace2,
                'position': position2,'personality': personality2,'qualities': qualities2,'correction_date': correction_date2})

with open('DataBase.pickle', 'wb') as f:
    AllData = pickle.dump(AllData, f)