import tkinter

from logic import *
from new_window import *
from datetime import datetime
from tkinter import *

flag_for_sort = False
data_for_sort = []
index_for_sort = []
select_Data_Index = None

def search_All():
    global flag_for_sort
    global data_for_sort
    global index_for_sort

    index_for_sort = []
    box_select_Data.delete(0, END)

    ent_Show_All['state'] = 'normal'
    ent_Show_All.delete('1.0', 'end')
    result = ent_Search_All.get('1.0', 'end-1c')
    result_Data, index_for_sort = search_in_Data(result)
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
            box_select_Data.insert('end', item)

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
    if not data_of_birth:
        ent_Show_Birthdays.insert('end', 'Сегодня ни у кого нет дня рождения')
    else:
        for item in data_of_birth:
            ent_Show_Birthdays.insert('1.0' ,item + '\n')
    ent_Show_Birthdays['state'] = 'disabled'

def choose_Data():
    global select_Data_Index

    select_Data_Index = box_select_Data.curselection()[0]
    list_Of_Data_To_Change = data_for_sort[select_Data_Index].split(', ')
    list_Of_Data_To_Change.pop()

    ent_Change_Name['state'] = 'normal'
    ent_Change_Adress['state'] = 'normal'
    ent_Change_Phone['state'] = 'normal'
    ent_Change_Birthdate['state'] = 'normal'
    ent_Change_WorkPlace['state'] = 'normal'
    ent_Change_Position['state'] = 'normal'
    ent_Change_Personality['state'] = 'normal'
    ent_Change_Qualities['state'] = 'normal'

    ent_Change_Name.delete('1.0', 'end')
    ent_Change_Adress.delete('1.0', 'end')
    ent_Change_Phone.delete('1.0', 'end')
    ent_Change_Birthdate.delete('1.0', 'end')
    ent_Change_WorkPlace.delete('1.0', 'end')
    ent_Change_Position.delete('1.0', 'end')
    ent_Change_Personality.delete('1.0', 'end')
    ent_Change_Qualities.delete('1.0', 'end')

    ent_Change_Name.insert('end', list_Of_Data_To_Change[0])
    ent_Change_Adress.insert('end', list_Of_Data_To_Change[1])
    ent_Change_Phone.insert('end', list_Of_Data_To_Change[2])
    ent_Change_Birthdate.insert('end', list_Of_Data_To_Change[3])
    ent_Change_WorkPlace.insert('end', list_Of_Data_To_Change[4])
    ent_Change_Position.insert('end', list_Of_Data_To_Change[5])
    ent_Change_Personality.insert('end', list_Of_Data_To_Change[6])
    ent_Change_Qualities.insert('end', list_Of_Data_To_Change[7])

    btn_Change_Data['state'] = 'normal'
    btn_Delete_Data['state'] = 'normal'


def create_Data():
    create_New_Window(window)



def change_Data():
    update_Name = ent_Change_Name.get('1.0', 'end-1c')
    update_Adress = ent_Change_Adress.get('1.0', 'end-1c')
    update_Phone = ent_Change_Phone.get('1.0', 'end-1c')
    update_Birthdate = ent_Change_Birthdate.get('1.0', 'end-1c')
    update_Workplace = ent_Change_WorkPlace.get('1.0', 'end-1c')
    update_Position = ent_Change_Position.get('1.0', 'end-1c')
    update_Personality = ent_Change_Personality.get('1.0', 'end-1c')
    update_Qualities = ent_Change_Qualities.get('1.0', 'end-1c')
    update_Correction_Date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    updating_Data = {'name': update_Name,'adress': update_Adress, 'phone': update_Phone, 'birth': update_Birthdate,
                     'workplace': update_Workplace, 'position': update_Position, 'personality': update_Personality,
                     'qualities': update_Qualities,'correction_date': update_Correction_Date}
    print(updating_Data)
    update_Data(updating_Data, index_for_sort[select_Data_Index])

    research_Data()

def research_Data():
    search_All()

    ent_Change_Name.delete('1.0', 'end')
    ent_Change_Adress.delete('1.0', 'end')
    ent_Change_Phone.delete('1.0', 'end')
    ent_Change_Birthdate.delete('1.0', 'end')
    ent_Change_WorkPlace.delete('1.0', 'end')
    ent_Change_Position.delete('1.0', 'end')
    ent_Change_Personality.delete('1.0', 'end')
    ent_Change_Qualities.delete('1.0', 'end')

    ent_Change_Name['state'] = 'disabled'
    ent_Change_Adress['state'] = 'disabled'
    ent_Change_Phone['state'] = 'disabled'
    ent_Change_Birthdate['state'] = 'disabled'
    ent_Change_WorkPlace['state'] = 'disabled'
    ent_Change_Position['state'] = 'disabled'
    ent_Change_Personality['state'] = 'disabled'
    ent_Change_Qualities['state'] = 'disabled'
    btn_Change_Data['state'] = 'disabled'
    btn_Delete_Data['state'] = 'disabled'


def delete_Data():
    delete_Data_From_List(select_Data_Index)

    research_Data()

def show_All_Data():
    global flag_for_sort
    global data_for_sort
    global index_for_sort

    index_for_sort = []
    box_select_Data.delete(0, END)

    ent_Show_All['state'] = 'normal'
    ent_Show_All.delete('1.0', 'end')
    result_Data, index_for_sort = search_All_Data()
    if len(result_Data) == 0:
        flag_for_sort = False
        ent_Show_All.insert('end', 'Записная книжка пуста')
    else:
        data_for_sort = result_Data
        flag_for_sort = True
        for item in result_Data:
            ent_Show_All.insert('end', item + '\n')

        for item in data_for_sort:
            box_select_Data.insert('end', item)

    ent_Show_All['state'] = 'disabled'

def clear_All_Data():
    ent_Show_All['state'] = 'normal'
    ent_Show_All.delete('1.0', 'end')
    ent_Show_All['state'] = 'disabled'
    box_select_Data.delete(0, END)

def on_Closing():
    data_Rewrite()
    window.destroy()

data_Init()
window = Tk()
window.title("Курсовая работа. Выполнил: Голубицкий А.А.")
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w = w // 2  # середина экрана
h = h // 2
w = w - 1275  # смещение от середины
h = h - 700
window.geometry('2100x800+{}+{}'.format(w, h))
# window.geometry('2150x1300')
#window.resizable(False, False)
window.configure(background='#D9CDB8')


Label(window, text="Текущая дата: " + datetime.today().strftime("%d-%m-%Y %H:%M"), font='Inter 12', bg='#D9CDB8', ).place(x=20, y=25)
Label(window, text="Записная книжка", font='Inter 19 bold', bg='#D9CDB8', ).place(x=500, y=20)

btn_Show_All = Button(window,text="Показать все записи", fg= 'white', font='Inter 15', bg='#260101', width=20 ,height=2,
                        command = show_All_Data)
btn_Show_All.place(x=900,y=20)

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
text_sort = Text(window, borderwidth=0, font='Inter 14', width=30, height=1, bg='#D9CDB8', )
text_sort.tag_configure("tag_name", justify='left')
text_sort.place(x=900, y=200)
text_sort.insert(1.0, "Выполнить сортировку по:")
text_sort.tag_add("tag_name", "1.0", "end")

btn_Sort_By_Alphabet = Button(window, text="Алфавиту", fg= 'white', font='Inter 15', bg='#260101', width=20 ,height=2,
                              command=sort_By_Alphabet)
btn_Sort_By_Alphabet.place(x=900,y=230)
btn_Sort_By_Date_Of_Change = Button(window, text="Дате изменения", fg= 'white', font='Inter 15', bg='#260101', width=20 ,height=2,
                                    command=sort_By_Date_Of_Change)
btn_Sort_By_Date_Of_Change.place(x=900,y=300)

btn_Clear_Everything = Button(window, text="Очистить поле", fg= 'white', font='Inter 15', bg='#260101', width=20 ,height=2,
                              command=clear_All_Data)
btn_Clear_Everything.place(x= 900, y=385)

#Просмотр, у кого день рождения
ent_Show_Birthdays = Text(window, fg= 'white', font='Inter 15', bg='#594036', width=75 ,height=10, padx=10, pady=10,
                          state='disabled')
ent_Show_Birthdays.place(x=20,y=500)

btn_Show_Birthdays = Button(window, text="У кого День Рождения", fg= 'white', font='Inter 15', bg='#260101', width=20 ,height=2,
                            command=show_Birthdays)
btn_Show_Birthdays.place(x=900,y=590)

#Изменения данных человека
Label(window, text="Изменить данные в записи", font='Inter 15', bg='#D9CDB8', ).place(x=1500, y=25)

box_select_Data = Listbox(window, width=131, height=8, bg='#594036', borderwidth=0,font='Inter 10',fg='white')
box_select_Data.place(x=1160,y=90)

btn_Choose_Data = Button(window, text="Выбрать запись", fg= 'white', font='Inter 15', bg='#260101', width=20 ,height=2,
                         command=choose_Data)
btn_Choose_Data.place(x=1500,y=250)

Label(window, text="ФИО", font='Inter 10 bold', bg='#D9CDB8', ).place(x=1160, y=350)
Label(window, text="Адрес", font='Inter 10 bold', bg='#D9CDB8', ).place(x=1620, y=350)

ent_Change_Name = Text(window, fg= 'white', font='Inter 10', bg='#594036', width=60 ,height=1, padx=10, pady=10,
                       state='disabled')
ent_Change_Name.place(x=1160,y=380)

ent_Change_Adress = Text(window, fg= 'white', font='Inter 10', bg='#594036', width=60 ,height=1, padx=10, pady=10,
                         state='disabled')
ent_Change_Adress.place(x=1620,y=380)

Label(window, text="Телефон", font='Inter 10 bold', bg='#D9CDB8', ).place(x=1160, y=420)
Label(window, text="Место работы/учёбы", font='Inter 10 bold', bg='#D9CDB8', ).place(x=1620, y=420)

ent_Change_Phone = Text(window, fg= 'white', font='Inter 10', bg='#594036', width=60 ,height=1, padx=10, pady=10,
                        state='disabled')
ent_Change_Phone.place(x=1160,y=450)

ent_Change_WorkPlace = Text(window, fg= 'white', font='Inter 10', bg='#594036', width=60 ,height=1, padx=10, pady=10,
                            state='disabled')
ent_Change_WorkPlace.place(x=1620,y=450)

Label(window, text="Должность", font='Inter 10 bold', bg='#D9CDB8', ).place(x=1160, y=490)
Label(window, text="Характер", font='Inter 10 bold', bg='#D9CDB8', ).place(x=1620, y=490)

ent_Change_Position = Text(window, fg= 'white', font='Inter 10', bg='#594036', width=60 ,height=1, padx=10, pady=10,
                           state='disabled')
ent_Change_Position.place(x=1160,y=520)
ent_Change_Personality = Text(window, fg= 'white', font='Inter 10', bg='#594036', width=60 ,height=1, padx=10, pady=10,
                              state='disabled')
ent_Change_Personality.place(x=1620,y=520)

Label(window, text="Деловые качества", font='Inter 10 bold', bg='#D9CDB8', ).place(x=1160, y=560)
Label(window, text="Дата рождения", font='Inter 10 bold', bg='#D9CDB8', ).place(x=1620, y=560)

ent_Change_Qualities = Text(window, fg= 'white', font='Inter 10', bg='#594036', width=60 ,height=1, padx=10, pady=10,
                            state='disabled')
ent_Change_Qualities.place(x=1160,y=590)

ent_Change_Birthdate = Text(window, fg= 'white', font='Inter 10', bg='#594036', width=60 ,height=1, padx=10, pady=10,
                            state='disabled')
ent_Change_Birthdate.place(x=1620,y=590)

btn_Change_Data = Button(window, text="Изменить запись", fg= 'white', font='Inter 15', bg='#260101', width=20 ,height=2,
                         command=change_Data, state='disabled')
btn_Change_Data.place(x=1500,y=660)
btn_Delete_Data = Button(window, text="Удалить запись", fg= 'white', font='Inter 15', bg='#260101', width=20 ,height=2,
                         command= delete_Data, state='disabled')
btn_Delete_Data.place(x=1800,y=660)

#Кнопка добавления записи
btn_Сreate_Data = Button(window, text="Добавить запись", fg= 'white', font='Inter 15', bg='#260101', width=20 ,height=2,
                         command=create_Data)
btn_Сreate_Data.place(x=1200,y=660)

window.protocol("WM_DELETE_WINDOW", on_Closing)
window.mainloop()
