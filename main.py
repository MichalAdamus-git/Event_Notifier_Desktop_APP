# Calendar app with notifier
from tkinter import *
from tkinter import messagebox
from tkcalendar import *
import random
import string
from plyer import notification
from datetime import *
import time
import threading
import sqlite3
from time import sleep

def load_events():
    global my_custom_db 
    my_custom_db = sqlite3.connect("events.db")
    cursor = my_custom_db.cursor()
#   cursor.execute("CREATE TABLE events(event_time TEXT, event_description TEXT, event_displayed INTEGER DEFAULT 0")
    closed = False
    while True:
        if stop_loading:
            my_custom_db.close()
            closed = True
        if stop_loading == False and closed == True:
            closed = False
            my_custom_db = sqlite3.connect("events.db")
            cursor = my_custom_db.cursor()
        if stop_loading == False and closed == False:
            for row in cursor.execute("SELECT * FROM events"):
                crt = datetime.now()
                ct = str(str(crt.year) + '-' + str(crt.month) + '-' + str(crt.day) + ' ' + str(crt.hour) + ':' + str(crt.minute))
                mct = datetime.strptime(ct, '%Y-%m-%d %H:%M')
                if row[0] == mct and row[3] == 0:
                    params = row[0]
                    notification.notify(title='Your event', message=row_to_list[2])
                    cursor.execute("UPDATE events SET event_displayed = 1 WHERE event_name = ?", params)

def notify():

    global stop_loading
    stop_loading = True
    today_data = cal.get_date()
    try:
        db_thread1 = sqlite3.connect("events.db")
        cursor = db_thread1.cursor()
        hour = H1e.get()
        if hour[2] != ':':
            hour_formatting = hour[0:2] + ':' + hour[3:]
        else:
            hour_formatting = hour
        event_time_string = today_data + ' ' + hour_formatting
        data = [h, notification_text, 0]
        db_thread1.execute("INSERT INTO events VALUES(?,?,?)", data)
        db_thread1.commit()
        sleep(5)
        db_thread1.close()
        stop_loading = False
    except Exception as e:
        print(e)

def nn():
    t=threading.Thread(target=notify)
    global notification_text
    notification_text=D1e.get('1.0',END)
    t.start()

'''
    print(len(H1e.get()))
    hour = H1e.get()
    print(hour)
    try:
        h = datetime.strptime(hour, '%H:%M')
        crt = datetime.now()
        print(crt)
        ct = str(str(crt.hour) + ':' + str(crt.minute))
        mct = datetime.strptime(ct, '%H:%M')
        abc = h - mct
        fgh = abc.total_seconds()
        time.sleep(fgh)
        try:
            notification.notify(title='Your event', message=notification_text)
            print('should be done')
        except:
            print('failed')
    except:
        pass

def notify1():
    hour1=new_he.get()
    h1 = datetime.strptime(hour1, '%H:%M')
    crt = datetime.now()
    print(crt)
    ct = str(str(crt.hour) + ':' + str(crt.minute))
    mct = datetime.strptime(ct, '%H:%M')
    abc = h1 - mct
    fgh = abc.total_seconds()
    time.sleep(fgh)
    notification.notify(title='Your event', message=new_nt)

def notify2():
    hour2=nnew_he.get()
    h2 = datetime.strptime(hour2, '%H:%M')
    crt = datetime.now()
    print(crt)
    ct = str(str(crt.hour) + ':' + str(crt.minute))
    mct = datetime.strptime(ct, '%H:%M')
    abc = h2 - mct
    fgh = abc.total_seconds()
    time.sleep(fgh)
    notification.notify(title='Your event', message=nnew_nt)


def nn():
    t=threading.Thread(target=notify)
    global notification_text
    notification_text=D1e.get('1.0',END)
    t.start()
def nn1():
    global new_nt
    new_nt=new_description.get('1.0',END)
    t = threading.Thread(target=notify1)
    t.start()
def nn2():
    global nnew_nt
    nnew_nt=nnew_description.get('1.0', END)
    t = threading.Thread(target=notify2)
    t.start()
'''
def tasks():
    root2 = Toplevel(bg='light blue')
    root2.geometry('600x750+600+210')
    title_label = Label(root2, text='Assign your events for' + " " + cal.get_date(), font=('Ariel', 15))
    title_label.place(x=150, y=10)
    H1l = LabelFrame(root2, text='Hour', font=('Arial', 12, 'bold'))
    H1l.grid(row=0, column=0, padx=20, pady=20)
    global H1e
    H1e = Entry(H1l, textvariable=StringVar, font=('Arial', 10), width=5)
    H1e.grid(row=0, column=0)
    D1l = LabelFrame(root2, text='Description', font=('Arial', 12, 'bold'))
    D1l.grid(row=0, column=1, padx=30, rowspan=2, pady=70)
    global D1e
    D1e = Text(D1l, font=('Arial', 12, 'bold'), width=25, height=5)
    D1e.grid(row=0, column=0)

    def tevent():
        n = 1
        if True:
            nnew_label = LabelFrame(root2, text='Hour' + str(n + 1), font=('Arial', 12))
            nnew_label.grid(row=n + 2, column=0, padx=20)
            nnew_desclabel = LabelFrame(root2, text='Description', font=('Arial', 10))
            nnew_desclabel.grid(row=n + 2, column=1, pady=40)
            global nnew_he
            nnew_he = Entry(nnew_label, textvariable=StringVar, font=('Arial', 10), width=5)
            nnew_he.grid(row=0, column=0)
            global nnew_description
            nnew_description = Text(nnew_desclabel, font=('Arial', 12, 'bold'), width=25, height=4)
            nnew_description.grid(row=0, column=0)
            b3.destroy()
            b4 = Button(root2, text='add new event')
            b4.place(x=275, y=510)
            bn2 = Button(root2, text="set notification", command=nn2)
            bn2.place(x=170, y=510)

    def new_event():
        n = 0
        if True:
            new_label = LabelFrame(root2, text='Hour' + str(n + 1), font=('Arial', 12))
            new_label.grid(row=n + 2, column=0, padx=20)
            new_desclabel = LabelFrame(root2, text='Description', font=('Arial', 10))
            new_desclabel.grid(row=n + 2, column=1)
            global new_he
            new_he = Entry(new_label, textvariable=StringVar, font=('Arial', 10), width=5)
            new_he.grid(row=0, column=0)
            global new_description
            new_description = Text(new_desclabel, font=('Arial', 12, 'bold'), width=25, height=4)
            new_description.grid(row=0, column=0)
            n += 1
            b2.destroy()
            global b3
            b3 = Button(root2, text='add new event', command=tevent)
            b3.place(x=275, y=380)
            bn1=Button(root2,text="set notification", command=nn1)
            bn1.place(x=170,y=380)

    b2 = Button(root2, text='add new event', command=new_event)
    b2.place(x=275, y=225)

    bn=Button(root2,text='set notification',command=nn)
    bn.place(x=170,y=225)

global stop_loading
stop_loading = False

event_loading = threading.Thread(target=load_events)
event_loading.start()

root = Tk(className='Orchestarate organizer')
root.geometry('800x530+500+210')
rootf = Frame(root)
rootf.grid(row=0, column=0)
cal = Calendar(rootf, selectmode='day', font=('Arial', 16, 'bold'), date_pattern = 'yyyy-mm-dd')
cal.grid(row=0, column=0, padx=200)
b1 = Button(root, text="see day's tasks", command=tasks)
b1.place(x=350, y=350)

root.mainloop()



