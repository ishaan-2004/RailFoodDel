'''
Online Railway Food Delivery System
Before running the program kindly install the following modules by
typing the given pip install commands in the Terminal
=> pip install mysql.connector
'''


from tkinter import *
import mysql.connector
from tkinter import messagebox
from menu import *


def register():

    root = Tk()
    root.title('RAILWAY FOOD DELIVERY SYSTEM')
    root.geometry('600x700')
    root.config(bg="#447c84")

    # Creating Database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password123",
        database="railfood_del"
    )
    c = mydb.cursor()

    c.execute("CREATE DATABASE IF NOT EXISTS railfood_del")
    c.execute("CREATE TABLE IF NOT EXISTS customers(name VARCHAR(250), \
        contact BIGINT(10), \
            pnr VARCHAR(100), \
                station VARCHAR(250), \
                    tno INT(10), \
                        sno VARCHAR(100), \
                            cno VARCHAR(100), \
                                user_id INT AUTO_INCREMENT PRIMARY KEY) ")

    def clr():
        fname.delete(0, END)
        contact.delete(0, END)
        pnr.delete(0, END)
        station.delete(0, END)
        tno.delete(0, END)
        sno.delete(0, END)
        cno.delete(0, END)

    def submit():

        warn = ""
        fname_check = fname.get()
        contact_check = contact.get()
        pnr_check = pnr.get()
        station_check = station.get()
        tno_check = tno.get()
        sno_check = sno.get()
        cno_check = cno.get()
        check_count = 0

        if fname_check == "":
            warn = "Name can't be left empty !"
        else:
            check_count += 1
        if contact_check == "":
            warn = "Contact can't be left empty!"
        else:
            check_count += 1
        if station_check == "":
            warn = "Station can't be left empty!"
        else:
            check_count += 1
        if pnr_check == "":
            warn = "PNR can't be left empty!"
        else:
            check_count += 1
        if tno_check == "":
            warn = "Train Number can't be left empty!"
        else:
            check_count += 1
        if sno_check == "":
            warn = "Seat Number can't be left empty!"
        else:
            check_count += 1
        if cno_check == "":
            warn = "Coach Number can't be left empty!"
        else:
            check_count += 1

        if check_count == 7:

            try:

                sql_command = "INSERT INTO customers (name,contact,station,pnr,tno,sno,cno) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                values = (fname.get(), contact.get(), station.get(),
                          pnr.get(), tno.get(), sno.get(), cno.get())
                c.execute(sql_command, values)

                mydb.commit()

                clr()
                messagebox.showinfo('confirmation', 'Record Saved')

            except Exception as ep:
                messagebox.showerror('', ep)
        else:
            messagebox.showerror('Error', warn)

    # Frames

    frame = Frame(root, padx=20, pady=20)
    frame.pack(expand=True)

    # Labels

    Label(
        frame,
        text="Railway Food Delivery System",
        font=("Times", "24", "bold")
    ).grid(row=0, columnspan=3, pady=10)

    Label(
        frame,
        text='Name',
        font=("Times", "14")
    ).grid(row=1, column=0, pady=10)

    Label(
        frame,
        text='Contact',
        font=("Times", "14")
    ).grid(row=2, column=0, pady=10)

    Label(
        frame,
        text='Station',
        font=("Times", "14")
    ).grid(row=3, column=0, pady=10)

    Label(
        frame,
        text='PNR',
        font=("Times", "14")
    ).grid(row=4, column=0, pady=10)

    Label(
        frame,
        text='Train Number',
        font=("Times", "14")
    ).grid(row=5, column=0, pady=10)

    Label(
        frame,
        text='Seat Number',
        font=("Times", "14")
    ).grid(row=6, column=0, pady=10)

    Label(
        frame,
        text='Coach Number',
        font=("Times", "14")
    ).grid(row=7, column=0, pady=10)

    # Entry Widgets

    fname = Entry(frame, width=30)
    contact = Entry(frame, width=30)
    station = Entry(frame, width=30)
    pnr = Entry(frame, width=30)
    tno = Entry(frame, width=30)
    sno = Entry(frame, width=30)
    cno = Entry(frame, width=30)

    fname.grid(row=1, column=1)
    contact.grid(row=2, column=1)
    station.grid(row=3, column=1)
    pnr.grid(row=4, column=1)
    tno.grid(row=5, column=1)
    sno.grid(row=6, column=1)
    cno.grid(row=7, column=1)

    # Buttons

    clear = Button(frame, text="Clear", padx=20, pady=10, relief=SOLID,font=(
        "Times", "14", "bold"), command=lambda: clr())
    reg = Button(frame, text="Proceed", padx=20, pady=10, relief=SOLID, font=(
        "Times", "14", "bold"), command=lambda: [submit(), root.destroy(), menu()])
    ext = Button(frame, text="Exit", padx=20, pady=10, relief=SOLID, font=(
        "Times", "14", "bold"), command=lambda: [root.destroy()])

    clear.grid(row=12, column=0, pady=20)
    reg.grid(row=12, column=1, pady=20)
    ext.grid(row=12, column=2, pady=20)

    root.mainloop()


# __main__
register()
