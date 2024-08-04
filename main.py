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

def notify():
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
        notification.notify(title='Your event', message=notification_text)
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


root = Tk(className='Orchestarate organizer')
root.geometry('800x530+500+210')
rootf = Frame(root)
rootf.grid(row=0, column=0)
cal = Calendar(rootf, selectmode='day', font=('Arial', 16, 'bold'))
cal.grid(row=0, column=0, padx=200)
b1 = Button(root, text="see day's tasks", command=tasks)
b1.place(x=350, y=350)

root.mainloop()


