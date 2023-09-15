
from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

conn = mysql.connector.connect(host='localhost', password='mysql#mysql', user='root',port=3306,database="stray_animals_management_system")
cur = conn.cursor()

window = Tk()
window.geometry("1000x800")


def animal_det():
    name = namevalue.get()
    animal_type = typevalue.get()
    age = agevalue.get()
    gender = gendervalue.get()
    location = locationvalue.get()
    health_status = healthvalue.get()
    behavior = behaviorvalue.get()

    insert = 'INSERT INTO animal_info (animal_name, animal_type, age, gender, location, health_status, behavior) VALUES (%s, %s, %s, %s, %s, %s, %s)'

    val = (name, animal_type, age, gender, location, health_status, behavior)
    cur.execute(insert, val)
    conn.commit()

    messagebox.showinfo("Success", "Animal details inserted successfully!")


def getvals():
    print("Accepted")
    animal_det()


# heading
Label(window, text="STRAY ANIMAL MANAGEMENT SYSTEM", font="ar 20 bold").grid(row=0, column=10)
info = Label(window, text="ANIMAL INFORMATION:", font="ar 10 bold")
info.grid(row=3, column=2)

# fields name
name = Label(window, text="ANIMAL")
animal_type = Label(window, text="TYPE")
age = Label(window, text="AGE")
gender = Label(window, text="GENDER")
location = Label(window, text="LOCATION")
health = Label(window, text="HEALTH ISSUES")
behavior = Label(window, text="BEHAVIOR")

name.grid(row=4, column=2)
animal_type.grid(row=5, column=2)
age.grid(row=6, column=2)
gender.grid(row=7, column=2)
location.grid(row=8, column=2)
health.grid(row=9, column=2)
behavior.grid(row=10, column=2)

# variables for storing data
namevalue = StringVar()
typevalue = StringVar()
agevalue = IntVar()
gendervalue = StringVar()
locationvalue = StringVar()
healthvalue = StringVar()
behaviorvalue = StringVar()
checkvalue = IntVar()

# entry fields
nameentry = Entry(window, textvariable=namevalue)
typeentry = Entry(window, textvariable=typevalue)
ageentry = Entry(window, textvariable=agevalue)
genderentry = Entry(window, textvariable=gendervalue)
locationentry = Entry(window, textvariable=locationvalue)
healthentry = Entry(window, textvariable=healthvalue)
behaviorentry = Entry(window, textvariable=behaviorvalue)

nameentry.grid(row=4, column=3)
typeentry.grid(row=5, column=3)
ageentry.grid(row=6, column=3)
genderentry.grid(row=7, column=3)
locationentry.grid(row=8, column=3)
healthentry.grid(row=9, column=3)
behaviorentry.grid(row=10, column=3)

# submit button
Button(text="Submit", command=getvals).grid(row=14, column=3)

r=tk.Tk()
r.title("Animal Details")
r.geometry("1000x500")

cur.execute("SELECT * FROM animal_info")

tree=ttk.Treeview(r)

tree["columns"]=("name","type","age","gender","location","health_status","behavior")


#width
tree.column("name",width=100,minwidth=100,anchor=tk.CENTER)
tree.column("type",width=100,minwidth=100,anchor=tk.CENTER)
tree.column("age",width=100,minwidth=100,anchor=tk.CENTER)
tree.column("gender",width=50,minwidth=150,anchor=tk.CENTER)
tree.column("location",width=100,minwidth=100,anchor=tk.CENTER)
tree.column("health_status",width=100,minwidth=100,anchor=tk.CENTER)
tree.column("behavior",width=100,minwidth=100,anchor=tk.CENTER)

#heading
tree.heading("name",text="Name",anchor=tk.CENTER)
tree.heading("type",text="Animal Type",anchor=tk.CENTER)
tree.heading("age",text="Age",anchor=tk.CENTER)
tree.heading("gender",text="Gender",anchor=tk.CENTER)
tree.heading("location",text="Location",anchor=tk.CENTER)
tree.heading("health_status",text="Health Issue",anchor=tk.CENTER)
tree.heading("behavior",text="Behavior",anchor=tk.CENTER)

i=0
for ro in cur:
    tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6]))

    
tree.pack()


window.mainloop()
