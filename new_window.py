from logic import *
import tkinter
from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo

def create_New_Window(window):
    def add_Data():
        add_Name = ent_Add_Name.get('1.0', 'end-1c')
        add_Adress = ent_Add_Adress.get('1.0', 'end-1c')
        add_Phone = ent_Add_Phone.get('1.0', 'end-1c')
        add_Birthdate = ent_Add_Birthdate.get('1.0', 'end-1c')
        add_Workplace = ent_Add_WorkPlace.get('1.0', 'end-1c')
        add_Position = ent_Add_Position.get('1.0', 'end-1c')
        add_Personality = ent_Add_Personality.get('1.0', 'end-1c')
        add_Qualities = ent_Add_Qualities.get('1.0', 'end-1c')
        add_Correction_Date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        add_New_Data = {'name': add_Name, 'adress': add_Adress, 'phone': add_Phone, 'birth': add_Birthdate,
                         'workplace': add_Workplace, 'position': add_Position, 'personality': add_Personality,
                         'qualities': add_Qualities, 'correction_date': add_Correction_Date}
        print(add_New_Data)
        for value in add_New_Data.values():
            if value == '':
                tkinter.messagebox.showwarning(title=None, message='Заполните все поля',)
                break
        else:
            create_Data_To_List(add_New_Data)
            window2.destroy()
    
    window2 = tkinter.Toplevel(window)
    window2.geometry('740x600')
    window2.configure(background='#D9CDB8')

    Label(window2, text="Добавить новую запись", font='Inter 19 bold', bg='#D9CDB8', ).place(x=220, y=20)

    Label(window2, text="ФИО", font='Inter 10 bold', bg='#D9CDB8', ).place(x=20, y=100)
    Label(window2, text="Адрес", font='Inter 10 bold', bg='#D9CDB8', ).place(x=380, y=100)

    ent_Add_Name = Text(window2, fg= 'white', font='Inter 10', bg='#594036', width=45 ,height=1, padx=10, pady=10,)
    ent_Add_Name.place(x=20,y=130)

    ent_Add_Adress = Text(window2, fg= 'white', font='Inter 10', bg='#594036', width=45 ,height=1, padx=10, pady=10,)
    ent_Add_Adress.place(x=380,y=130)

    Label(window2, text="Телефон", font='Inter 10 bold', bg='#D9CDB8', ).place(x=20, y=180)
    Label(window2, text="Место работы/учёбы", font='Inter 10 bold', bg='#D9CDB8', ).place(x=380, y=180)

    ent_Add_Phone = Text(window2, fg= 'white', font='Inter 10', bg='#594036', width=45 ,height=1, padx=10, pady=10,)
    ent_Add_Phone.place(x=20,y=210)

    ent_Add_WorkPlace = Text(window2, fg= 'white', font='Inter 10', bg='#594036', width=45 ,height=1, padx=10, pady=10,)
    ent_Add_WorkPlace.place(x=380,y=210)

    Label(window2, text="Должность", font='Inter 10 bold', bg='#D9CDB8', ).place(x=20, y=260)
    Label(window2, text="Характер", font='Inter 10 bold', bg='#D9CDB8', ).place(x=380, y=260)
    ent_Add_Position = Text(window2, fg= 'white', font='Inter 10', bg='#594036', width=45 ,height=1, padx=10, pady=10,)
    ent_Add_Position.place(x=20,y=290)
    ent_Add_Personality = Text(window2, fg= 'white', font='Inter 10', bg='#594036', width=45 ,height=1, padx=10, pady=10,)
    ent_Add_Personality.place(x=380,y=290)

    Label(window2, text="Деловые качества", font='Inter 10 bold', bg='#D9CDB8', ).place(x=20, y=340)
    Label(window2, text="Дата рождения", font='Inter 10 bold', bg='#D9CDB8', ).place(x=380, y=340)

    ent_Add_Qualities = Text(window2, fg= 'white', font='Inter 10', bg='#594036', width=45 ,height=1, padx=10, pady=10,)
    ent_Add_Qualities.place(x=20,y=370)

    ent_Add_Birthdate = Text(window2, fg= 'white', font='Inter 10', bg='#594036', width=45 ,height=1, padx=10, pady=10,)
    ent_Add_Birthdate.place(x=380,y=370)

    btn_Сreate_New_Data = Button(window2, text="Добавить запись", fg='white', font='Inter 10', bg='#260101', width=20,
                             height=2, command=add_Data)
    btn_Сreate_New_Data.place(x=280, y=430)

