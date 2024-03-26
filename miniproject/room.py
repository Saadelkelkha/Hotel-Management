from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import re
from datetime import date

import mysql.connector

# Connect to MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
    database="Hotel"
)
cursor = db_connection.cursor()

class Room:
    def __init__(self, root):
        self.root = root
        self.root.title("Room")
        self.root.geometry("1083x405+200+235")
        self.root.resizable(False, False)
        self.root.iconbitmap ("img\\logo.ico")

        self.var_floor = StringVar()
        self.var_price = StringVar()

        lab1 = Label(self.root, text='Room Adding Details', font=('arial',18,'bold'), bg='black',fg='white')
        lab1.place(x=0, y=0, width=1083, height=50)

        imgr1 = Image.open("C:\\Users\\saad\\Desktop\\DG\\miniproject\\img\\logoo.jpg")
        imgr1 = imgr1.resize((100, 50))
        self.photor1 = ImageTk.PhotoImage(imgr1)

        lab = Label(self.root, image=self.photor1, bd=0, relief=RIDGE)
        lab.place(x=0, y=0)

        lab = Label(self.root, image=self.photor1, bd=0, relief=RIDGE)
        lab.place(x=983, y=0)

        labframe1 = LabelFrame(self.root, bd=4, relief=RIDGE, text='Room INFO', font=('arial',10,'bold'), padx=2)
        labframe1.place(x=5, y=51 ,width=380,height=352)

        img = "C:\\Users\\saad\\Desktop\\DG\\miniproject\\img\\OIP.jpeg"
        imgr2 = Image.open(img)
        imgr2 = imgr2.resize((185, 100))
        self.photor2 = ImageTk.PhotoImage(imgr2)

        self.labimg = Label(labframe1, image=self.photor2, bd=0, relief=RIDGE)
        self.labimg.grid(row=0, column=0, sticky=W)

        img1 = "C:\\Users\\saad\\Desktop\\DG\\miniproject\\img\\Superior.jpg"
        imgr3 = Image.open(img1)
        imgr3 = imgr3.resize((185, 100))
        self.photor3 = ImageTk.PhotoImage(imgr3)

        self.labimg = Label(labframe1, image=self.photor3, bd=0, relief=RIDGE)
        self.labimg.grid(row=0, column=1, sticky=W)

        # Room Number
        Number_room_lab = Label(labframe1, text='Room Number :', font=('arialn',12), padx=2, pady=3)
        Number_room_lab.grid(row=1, column=0, sticky=W)

        self.Number_room_entry = Label(labframe1, text=self.get_record_count() + 1, font=('arial',12), width=15)
        self.Number_room_entry.grid(row=1, column=1, sticky=W)

        # floor

        floor_lab = Label(labframe1, text='Floor :', font=('arialn',12), padx=2, pady=3)
        floor_lab.grid(row=2, column=0, sticky=W)

        self.floor_entry = Entry(labframe1, textvariable=self.var_floor ,font=('arial',12),width=15)
        self.floor_entry.grid(row=2, column=1, sticky=W)

        # Room type 

        room_type_lab = Label(labframe1, text='Room type :', font=('arialn',12), padx=2, pady=3)
        room_type_lab.grid(row=3, column=0, sticky=W)
        
        self.var_typp = StringVar()
        self.room_type_entry = ttk.Combobox(labframe1, textvariable=self.var_typp,font=('arial', 13, 'bold'), state='readonly',width=13)
        self.room_type_entry['value'] = ('Deluxe','Superior','Classic','Suite')
        self.room_type_entry.current(0)
        self.room_type_entry.grid(row=3, column=1, padx=2, pady=4, sticky=W)


        # Price

        Price_lab = Label(labframe1, text='Price :', font=('arialn',12), padx=2, pady=3)
        Price_lab.grid(row=4, column=0, sticky=W)

        self.Price_entry = Entry(labframe1, textvariable=self.var_price ,font=('arial',12),width=15)
        self.Price_entry.grid(row=4, column=1, sticky=W)

        # Availabe_status
        room_type_lab = Label(labframe1, text='Availabe Status :', font=('arialn',12), padx=2, pady=3)
        room_type_lab.grid(row=5, column=0, sticky=W)
        
        self.var_Availabe_status = StringVar()
        self.Availabe_status_entry = ttk.Combobox(labframe1, textvariable=self.var_Availabe_status, font=('arial', 13, 'bold'), state='readonly',width=13)
        self.Availabe_status_entry['value'] = ('Availabe','Booked up','In maintenance')
        self.Availabe_status_entry.current(0)
        self.Availabe_status_entry.grid(row=5, column=1, padx=2, pady=4, sticky=W)

        # btn

        btnframe = Frame(labframe1, padx=2, pady=3)
        btnframe.place(x=0, y=270, width= 370, height=100)

        addbtn = Button(btnframe, text='Add', command=self.add_record, font=('arial', 12, 'bold'), bg='black', fg='white', width=8, height=2)
        addbtn.grid(row=0, column=0, padx=1)

        upbtn = Button(btnframe, text='Update', command=self.update, font=('arial', 12, 'bold'), bg='black', fg='white', width=8, height=2)
        upbtn.grid(row=0, column=1, padx=1)

        resbtn = Button(btnframe, text='Reset',command=self.reset, font=('arial', 12, 'bold'), bg='black', fg='white', width=8, height=2)
        resbtn.grid(row=0, column=2, padx=1)

        delbtn = Button(btnframe, text='Delete', command=self.delete, font=('arial', 12, 'bold'), bg='black', fg='white', width=8, height=2)
        delbtn.grid(row=0, column=3, padx=1)
        
        # frame search 
        
        labframe2 = LabelFrame(self.root, bd=2, relief=RIDGE, text='Show Rooms Info ', font=('arial',10,'bold'), padx=2)
        labframe2.place(x=386, y=51 ,width=695,height=452)

        searchlab = Label(labframe2, text='Search By:', font=('arial', 12, 'bold'), bg='red', fg='white', padx=2, pady=4)
        searchlab.grid(row=0, column=0, sticky=W)

        self.var_search = StringVar()
        combo_search = ttk.Combobox(labframe2, textvariable=self.var_search, font=('arial', 12, 'bold'), width=20, state='readonly')
        combo_search['value'] = ('Room Number','Room Type','Availabe Status')
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.var_entsearch = StringVar()
        searchentry = Entry(labframe2, textvariable=self.var_entsearch, font=('arial',12), width=15)
        searchentry.grid(row=0, column=2, padx=2)

        searchbtn = Button(labframe2, text='Search', command=self.search, font=('arial', 12, 'bold'), bg='black', fg='white', width=8)
        searchbtn.grid(row=0, column=3, padx=3)

        showallbtn = Button(labframe2, text='Show All', command=self.view_records, font=('arial', 12, 'bold'), bg='black', fg='white', width=8)
        showallbtn.grid(row=0, column=4, padx=3)

        # Show Data 

        table = Frame(labframe2, bd=2, relief=RIDGE)
        table.place(x=0, y=50, width=671, height=290)

        scrollx = Scrollbar(table, orient=HORIZONTAL)
        scrolly = Scrollbar(table, orient=VERTICAL)

        self.data_table=ttk.Treeview(table, columns=('Room_number', 'Floor','Room_Type','Availabe_status','price'),
                                        xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.data_table.xview)
        scrolly.config(command=self.data_table.yview)

        self.data_table.heading('Room_number', text='Room Number')
        self.data_table.heading('Floor', text='Floor')
        self.data_table.heading('Room_Type', text='Room Type')
        self.data_table.heading('Availabe_status', text='Availabe Status')
        self.data_table.heading('price', text='Price')

        self.data_table['show']= "headings"

        self.data_table.column('Room_number', width=100)
        self.data_table.column('Floor', width=100)
        self.data_table.column('Room_Type', width=100)
        self.data_table.column('Availabe_status', width=100)
        self.data_table.column('price', width=100)

        self.data_table.pack(fill=BOTH, expand=1)
        self.data_table.bind("<ButtonRelease-1>", self.get_record)
        self.view_records()

    def get_record_count(self):
        cursor.execute("SELECT COUNT(*) FROM Room")
        record_count = cursor.fetchone()[0]
        return record_count

    def add_record(self):
        if self.var_floor.get() == "" or  self.var_price.get() == "" :
            messagebox.showerror("Error","All fields are required", parent=self.root)
        else:
            try:
                    cursor.execute("insert into Room values(%s,%s,%s,%s,%s)",(
                    self.get_record_count()+1,
                    self.var_typp.get(),
                    self.var_floor.get(),
                    self.var_Availabe_status.get(),
                    self.var_price.get(),
                    ))
                    messagebox.showinfo("Success","Room has been added", parent=self.root)
                    db_connection.commit()
                    self.view_records()
                    self.Number_room_entry.config(text=self.get_record_count() + 1)
                    self.floor_entry.delete(0, END)
                    self.Price_entry.delete(0, END)
                    self.room_type_entry.current(0)
                    self.Availabe_status_entry.current(0)
            
            except Exception as es:
                    messagebox.showwarning("Warning",f"Some thing went wrong{str(es)}", parent=self.root)

    def view_records(self):
        cursor.execute("select Room_number, floor, room_type, Availabe_status, price from  Room")
        rows = cursor.fetchall()
        self.data_table.delete(*self.data_table.get_children())
        for i in rows:
            self.data_table.insert("", END, values=i)
        db_connection.commit()

    def get_record(self, event=""):
        select_row = self.data_table.focus()
        content = self.data_table.item(select_row)
        row = content["values"]

        self.Number_room_entry.config(text=row[0])
        self.var_floor.set(row[1])
        self.var_price.set(row[4])

        if  row[2] == 'Deluxe':
            self.room_type_entry.current(0)
        elif row [2]=="Superior":
            self.room_type_entry.current(1)
        elif row [2]=="Classic":
            self.room_type_entry.current(2)
        elif  row [2]=="Suite":
            self.room_type_entry.current(3)
        
        if row[3] == 'Availabe' :
            self.Availabe_status_entry.current(0)
        elif row[3] == 'Booked up' :
            self.Availabe_status_entry.current(1)
        elif row[3] == 'In maintenance' :
            self.Availabe_status_entry.current(2)

    def update(self):
        if self.var_floor.get() == "" or  self.var_price.get() == "" :
            messagebox.showerror("Error","All fields are required", parent=self.root)
        else:
                cursor.execute("update Room set Room_Type=%s,floor=%s,Availabe_status=%s,price=%s where Room_number=%s",(
                    self.var_typp.get(),
                    self.var_floor.get(),
                    self.var_Availabe_status.get(),
                    self.var_price.get(),
                    self.get_record_count()
                ))
                db_connection.commit()
                self.view_records()
                self.Number_room_entry.config(text=self.get_record_count() + 1)
                self.floor_entry.delete(0, END)
                self.Price_entry.delete(0, END)
                self.room_type_entry.current(0)
                self.Availabe_status_entry.current(0)
                messagebox.showinfo("Update","Room information has been update successfully", parent=self.root)
    
    def reset(self):
        self.Number_room_entry.config(text=self.get_record_count() + 1)
        self.floor_entry.delete(0, END)
        self.Price_entry.delete(0, END)
        self.room_type_entry.current(0)
        self.Availabe_status_entry.current(0)
            
    def delete(self):
        ask = messagebox.askyesno("","do you want delete this Room",parent=self.root)
        if ask == True :
            query = "delete from Room where Room_number=%s"
            data = (self.Number_room_entry["text"],)
            cursor.execute(query,data)
            db_connection.commit()
            self.view_records()
            self.Number_room_entry.config(text=self.get_record_count() + 1)
            self.floor_entry.delete(0, END)
            self.Price_entry.delete(0, END)
            self.room_type_entry.current(0)
            self.Availabe_status_entry.current(0)
    
    def search(self):
        if self.var_search.get() == 'Room Number' :
            cursor.execute(f"select Room_number, floor, Room_Type, Availabe_status, price from Room where Room_number like '%{self.var_entsearch.get()}%'")
        elif self.var_search.get() == 'Room Type' :
            cursor.execute(f"select Room_number, floor, Room_Type, Availabe_status, price from Room where Room_Type like '%{self.var_entsearch.get()}%'")
        elif self.var_search.get() == 'Availabe Status' :
            cursor.execute(f"select Room_number, floor, Room_Type, Availabe_status, price from Room where Availabe_status like '%{self.var_entsearch.get()}%'")
        rows = cursor.fetchall()
        self.data_table.delete(*self.data_table.get_children())
        for i in rows:
            self.data_table.insert('', END, values=i)
        db_connection.commit()

if __name__ == "__main__":
    root = Tk()
    Room(root)
    root.mainloop()