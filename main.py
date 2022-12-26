from logic import *
from datetime import datetime
from tkinter import *

flag_for_sort = False
data_for_sort = []
def search_All():
    global flag_for_sort
    global data_for_sort

    box_select_Data.delete(0, END)

    ent_Show_All['state'] = 'normal'
    ent_Show_All.delete('1.0', 'end')
    result = ent_Search_All.get('1.0', 'end-1c')
    result_Data = search_in_Data(result)
    if len(result_Data) == 0 or result == '':
        flag_for_sort = False
        ent_Show_All.insert('end', 'По вашему запросу ничего не найдено, попробуйте проверить '
                                 'регистр или пробелы в запросе, который составляете')
    else:
        data_for_sort = result_Data
        flag_for_sort = True
        for item in result_Data:
            ent_Show_All.insert('end', item + '\n')

        for item in data_for_sort:
            box_select_Data.insert(0, item)

    ent_Show_All['state'] = 'disabled'

def sort_By_Alphabet():
    ent_Show_All['state'] = 'normal'
    ent_Show_All.delete('1.0', 'end')
    if flag_for_sort == True and len(data_for_sort)>1:
        for i in range(len(data_for_sort) - 1):
            for j in range(len(data_for_sort) - i - 1):
                if data_for_sort[j][0] < data_for_sort[j + 1][0]:
                    data_for_sort[j], data_for_sort[j + 1] = data_for_sort[j + 1], data_for_sort[j]
        for item in data_for_sort:
            ent_Show_All.insert(1.0, item + '\n')
    else:
        ent_Show_All.insert('end', 'Нечего сортировать')
    ent_Show_All['state'] = 'disabled'

def sort_By_Date_Of_Change():
    global data_for_sort
    ent_Show_All['state'] = 'normal'
    ent_Show_All.delete('1.0', 'end')
    if flag_for_sort == True and len(data_for_sort) > 1:
        data_for_sort = sort_by_date(data_for_sort)
        for item in data_for_sort:
            ent_Show_All.insert('1.0', item + '\n')
    else:
        ent_Show_All.insert('end', 'Нечего сортировать')
    ent_Show_All['state'] = 'disabled'

def show_Birthdays():
    ent_Show_Birthdays['state'] = 'normal'
    ent_Show_Birthdays.delete('1.0', 'end')
    data_of_birth = show_birth()
    if len(data_of_birth) > 0:
        for item in data_of_birth:
            ent_Show_Birthdays.insert('1.0' ,item + '\n')
    ent_Show_Birthdays['state'] = 'disabled'

#def choose_Data():

#def create_Data():

#def change_Data():

#def delete_Data():


window = Tk()
window.title("Курсовая работа. Выполнил: Голубицкий А.А.")
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w = w // 2  # середина экрана
h = h // 2
w = w - 1275  # смещение от середины
h = h - 700
window.geometry('1150x1300+{}+{}'.format(w, h))
#window.resizable(False, False)
window.configure(background='#D9CDB8')


Label(window, text="Текущая дата: " + datetime.today().strftime("%d-%m-%Y %H:%M"), font='Inter 12', bg='#D9CDB8', ).place(x=20, y=25)
Label(window, text="Записная книжка", font='Inter 19 bold', bg='#D9CDB8', ).place(x=500, y=20)

#Для общего поиска
ent_Search_All = Text(window, fg= 'white', font='Inter 15', bg='#594036', width=75 ,height=1, padx=10, pady=10)
ent_Search_All.place(x=20,y=100)

# scroll = Scrollbar(command=ent_Search_All.yview)

#ent_Search_All.insert(1.0, "Введите запрос")

btn_Search_All = Button(window, text="Поиск", fg= 'white', font='Inter 15', bg='#260101', width=20 ,height=2,
                        command = search_All)
btn_Search_All.place(x=900,y=90)


#Для вывода найденного и его сортировка
ent_Show_All = Text(window, fg= 'white', font='Inter 15', bg='#594036', width=75 ,height=10, padx=10, pady=10, state= 'disabled')
ent_Show_All.place(x=20,y=200)
text_sort = Text(window, borderwidth=0, font='Inter 15', width=20, height=3, bg='#D9CDB8', )
text_sort.tag_configure("tag_name", justify='center')
text_sort.place(x=900, y=220)
text_sort.insert(1.0, "Выполнить сортировку по:")
text_sort.tag_add("tag_name", "1.0", "end")

btn_Sort_By_Alphabet = Button(window, text="Алфавиту", fg= 'white', font='Inter 15', bg='#260101', width=20 ,height=2,
                              command=sort_By_Alphabet)
btn_Sort_By_Alphabet.place(x=900,y=280)
btn_Sort_By_Date_Of_Change = Button(window, text="Дате изменения", fg= 'white', font='Inter 15', bg='#260101', width=20 ,height=2,
                                    command=sort_By_Date_Of_Change)
btn_Sort_By_Date_Of_Change.place(x=900,y=360)

#Просмотр, у кого день рождения
ent_Show_Birthdays = Text(window, fg= 'white', font='Inter 15', bg='#594036', width=75 ,height=10, padx=10, pady=10)
ent_Show_Birthdays.place(x=20,y=500)

btn_Show_Birthdays = Button(window, text="У кого День Рождения", fg= 'white', font='Inter 15', bg='#260101', width=20 ,height=2,
                            command=show_Birthdays)
btn_Show_Birthdays.place(x=900,y=590)

#Изменения данных человека
Label(window, text="Изменить данные в записи", font='Inter 15', bg='#D9CDB8', ).place(x=500, y=770)

box_select_Data = Listbox(window, width=131, height=8, bg='#594036', borderwidth=0,font='Inter 10',fg='white')
box_select_Data.place(x=20,y=800)
btn_Change_Data = Button(window, text="Выбрать запись", fg= 'white', font='Inter 10', bg='#260101', width=20 ,height=2)
btn_Change_Data.place(x=960,y=860)

Label(window, text="ФИО", font='Inter 10 bold', bg='#D9CDB8', ).place(x=20, y=950)
Label(window, text="Адрес", font='Inter 10 bold', bg='#D9CDB8', ).place(x=620, y=950)
ent_Change_Name = Text(window, fg= 'white', font='Inter 10', bg='#594036', width=70 ,height=1, padx=10, pady=10)
ent_Change_Name.place(x=20,y=980)
ent_Change_Adress = Text(window, fg= 'white', font='Inter 10', bg='#594036', width=70 ,height=1, padx=10, pady=10)
ent_Change_Adress.place(x=620,y=980)

Label(window, text="Телефон", font='Inter 10 bold', bg='#D9CDB8', ).place(x=20, y=1020)
Label(window, text="Место работы/учёбы", font='Inter 10 bold', bg='#D9CDB8', ).place(x=620, y=1020)
ent_Change_Phone = Text(window, fg= 'white', font='Inter 10', bg='#594036', width=70 ,height=1, padx=10, pady=10)
ent_Change_Phone.place(x=20,y=1050)
ent_Change_WorkPlace = Text(window, fg= 'white', font='Inter 10', bg='#594036', width=70 ,height=1, padx=10, pady=10)
ent_Change_WorkPlace.place(x=620,y=1050)

Label(window, text="Должность", font='Inter 10 bold', bg='#D9CDB8', ).place(x=20, y=1090)
Label(window, text="Характер", font='Inter 10 bold', bg='#D9CDB8', ).place(x=620, y=1090)
ent_Change_Position = Text(window, fg= 'white', font='Inter 10', bg='#594036', width=70 ,height=1, padx=10, pady=10)
ent_Change_Position.place(x=20,y=1120)
ent_Change_Personality = Text(window, fg= 'white', font='Inter 10', bg='#594036', width=70 ,height=1, padx=10, pady=10)
ent_Change_Personality.place(x=620,y=1120)

Label(window, text="Деловые качества", font='Inter 10 bold', bg='#D9CDB8', ).place(x=20, y=1160)
Label(window, text="Дата рождения", font='Inter 10 bold', bg='#D9CDB8', ).place(x=620, y=1160)
ent_Change_Qualities = Text(window, fg= 'white', font='Inter 10', bg='#594036', width=70 ,height=1, padx=10, pady=10)
ent_Change_Qualities.place(x=20,y=1190)
ent_Change_Birthdate = Text(window, fg= 'white', font='Inter 10', bg='#594036', width=70 ,height=1, padx=10, pady=10)
ent_Change_Birthdate.place(x=620,y=1190)

btn_Change_Data = Button(window, text="Изменить запись", fg= 'white', font='Inter 10', bg='#260101', width=20 ,height=2)
btn_Change_Data.place(x=680,y=1245)
btn_Delete_Data = Button(window, text="Удалить запись", fg= 'white', font='Inter 10', bg='#260101', width=20 ,height=2)
btn_Delete_Data.place(x=910,y=1245)

#Кнопка добавления записи
btn_Сreate_Data = Button(window, text="Добавить запись", fg= 'white', font='Inter 10', bg='#260101', width=20 ,height=2)
btn_Сreate_Data.place(x=180,y=1245)

# for i in ('qwe','qwewq','rewr','werew','erter','ertert','tryrt','trytry','trytry','trytr'):
#     box_select_Data.insert(0,i)


window.mainloop()

#Бизнес-логика (перенести потом в отдельный файл)
