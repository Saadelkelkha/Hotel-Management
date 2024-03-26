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

class Service:
    def __init__(self, root):
        self.root = root
        self.root.title("Service")
        self.root.geometry("1083x405+200+235")
        self.root.resizable(False, False)
        self.root.iconbitmap ("img\\logo.ico")

        self.service = None
        self.price = 100
        self.var_no_person = StringVar()
        self.var_no_room = StringVar()

        lab1 = Label(self.root, text='Service Details', font=('arial',18,'bold'), bg='black',fg='white')
        lab1.place(x=0, y=0, width=1083, height=50)

        imgr1 = Image.open("C:\\Users\\saad\\Desktop\\DG\\miniproject\\img\\logoo.jpg")
        imgr1 = imgr1.resize((100, 50))
        self.photor1 = ImageTk.PhotoImage(imgr1)

        lab = Label(self.root, image=self.photor1, bd=0, relief=RIDGE)
        lab.place(x=0, y=0)

        lab = Label(self.root, image=self.photor1, bd=0, relief=RIDGE)
        lab.place(x=983, y=0)

        labframe1 = LabelFrame(self.root, bd=2, relief=RIDGE, text='Service INFO', font=('arial',10,'bold'), padx=2)
        labframe1.place(x=5, y=51 ,width=380,height=352)

        imgr = Image.open("C:\\Users\\saad\\Desktop\\DG\\miniproject\\img\\sevice.jpeg")
        imgr = imgr.resize((370, 110))
        self.photor = ImageTk.PhotoImage(imgr)

        labr = Label(labframe1, image=self.photor, bd=0, relief=RIDGE)
        labr.place(x=0, y=0)

        # Room number
        no_room_lab = Label(labframe1, text='Room Number :', font=('arialn',12), padx=2, pady=10)
        no_room_lab.place(x=0 , y=115)

        self.no_room_entry = Entry(labframe1, textvariable=self.var_no_room, font=('arial',12),width=15)
        self.no_room_entry.place(x=150 , y=125)

        # Button

        btnfetchdata = Button(labframe1, text='Fetch Data', command=self.fetch_contact, font=('arial', 9, 'bold'), bg='black', fg='white', width=8)
        btnfetchdata.place(x=300,y=123)

        # Service Type

        Service_Type_lab = Label(labframe1, text='Service Type :', font=('arialn',12), padx=2, pady=10)
        Service_Type_lab.place(x=0 , y=150)

        self.var_typs = StringVar()
        self.Service_Type_entry = ttk.Combobox(labframe1, textvariable=self.var_typs, font=('arial', 13, 'bold'), state='readonly')
        self.Service_Type_entry['value'] = ('Breakfast Service','Lunch Service','Dinner Service','In-Room Dining')
        self.Service_Type_entry.current(0)
        self.Service_Type_entry.place(x=150, y=160)
        self.Service_Type_entry.bind("<<ComboboxSelected>>", self.update_price)

        # Number Person
        no_person_lab = Label(labframe1, text='Number Of Person :', font=('arialn',12), padx=2, pady=10)
        no_person_lab.place(x=0 , y=185)

        self.no_person_entry = Entry(labframe1, textvariable=self.var_no_person, font=('arial',12),width=22)
        self.no_person_entry.place(x=150 , y=195)

        # Price

        Price_lab = Label(labframe1, text='Price :', font=('arialn',12), padx=2, pady=10)
        Price_lab.place(x=0 , y=220)

        self.Price_entry = Label(labframe1, text=100, font=('arial',12),width=23)
        self.Price_entry.place(x=190 , y=230)

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
        
        #fetch data

        img = "C:\\Users\\saad\\Desktop\\DG\\miniproject\\img\\serviceroom.jpeg"
        imgr2 = Image.open(img)
        imgr2 = imgr2.resize((200, 100))
        self.photor2 = ImageTk.PhotoImage(imgr2)

        self.labimg = Label(self.root, image=self.photor2, bd=0, relief=RIDGE)
        self.labimg.place(x=880, y=51)

        img1 = "C:\\Users\\saad\\Desktop\\DG\\miniproject\\img\\roomservice.jpg"
        imgr3 = Image.open(img1)
        imgr3 = imgr3.resize((200, 100))
        self.photor3 = ImageTk.PhotoImage(imgr3)

        self.labimg = Label(self.root, image=self.photor3, bd=0, relief=RIDGE)
        self.labimg.place(x=680, y=51)

    
        # frame search 
        
        labframe2 = LabelFrame(self.root, bd=2, relief=RIDGE, text='Show Booking Info ', font=('arial',10,'bold'), padx=2)
        labframe2.place(x=386, y=150 ,width=695,height=352)

        searchlab = Label(labframe2, text='Search By:', font=('arial', 12, 'bold'), bg='red', fg='white', padx=2, pady=4)
        searchlab.grid(row=0, column=0)

        self.var_search = StringVar()
        combo_search = ttk.Combobox(labframe2, textvariable=self.var_search, font=('arial', 12, 'bold'), width=20, state='readonly')
        combo_search['value'] = ('CIN','Room')
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
        table.place(x=0, y=50, width=671, height=190)

        scrollx = Scrollbar(table, orient=HORIZONTAL)
        scrolly = Scrollbar(table, orient=VERTICAL)

        self.data_table=ttk.Treeview(table, columns=('ID_SERVICE','CIN', 'NO_ROOM','TYPE_SERVICE','price_service','date_service','no_person'),
                                        xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.data_table.xview)
        scrolly.config(command=self.data_table.yview)
        
        self.data_table.heading('ID_SERVICE', text='Service ID')
        self.data_table.heading('CIN', text='CIN')
        self.data_table.heading('NO_ROOM', text='Room Number')
        self.data_table.heading('TYPE_SERVICE', text='Service Type')
        self.data_table.heading('price_service', text='Price')
        self.data_table.heading('date_service', text='Service date')
        self.data_table.heading('no_person', text='Number Of Person')

        self.data_table['show']= "headings"

        self.data_table.column('ID_SERVICE', width=100)
        self.data_table.column('CIN', width=100)
        self.data_table.column('NO_ROOM', width=100)
        self.data_table.column('TYPE_SERVICE', width=100)
        self.data_table.column('price_service', width=100)
        self.data_table.column('date_service', width=100)
        self.data_table.column('no_person', width=100)

        self.data_table.pack(fill=BOTH, expand=1)
        self.data_table.bind("<ButtonRelease-1>", self.get_record)
        self.view_records()

    
    def update_price(self, event):
        if self.var_typs.get() == 'Breakfast Service' :
            self.Price_entry.config(text=100)
            self.price = 100
        elif self.var_typs.get( )== 'Lunch Service':
            self.Price_entry.config(text=300)
            self.price = 300
        elif self.var_typs.get( )== 'Dinner Service':
            self.Price_entry.config(text=200)
            self.price = 200
        elif self.var_typs.get( )== 'In-Room Dining':
            self.Price_entry.config(text=550)
            self.price = 550

    def fetch_contact(self):
        if self.var_no_room.get()=='':
            messagebox.showerror('Error','Please enter CIN',parent=self.root)
        else:
            query = ('Select first_Name, last_name, email, address from customer join booking on customer.CIN=booking.CIN where booking.no_room=%s and (current_date()) between check_in and check_out')
            value = (self.var_no_room.get(),)
            cursor.execute(query,value)
            row = cursor.fetchone()

            if row == None :
                messagebox.showerror("Error", 'No Customer Found with this Room', parent=self.root)
            else:
                db_connection.commit()
                showdataframe = Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=386,y=51,width=295,height=100)

                label_firstname = Label(showdataframe,text="First Name:",font=('arial',10,'bold'))
                label_firstname.place(x=0,y=0)

                label_firstname_value = Label(showdataframe,text=row[0],font=('arial',10,'bold'))
                label_firstname_value.place(x=120,y=0)

                label_Last_Name = Label(showdataframe,text="Last Name:",font=('arial',10,'bold'))
                label_Last_Name.place(x=0,y=20)

                label_Last_Name_value = Label(showdataframe,text=row[1],font=('arial',10,'bold'))
                label_Last_Name_value.place(x=120,y=20)

                label_Email = Label(showdataframe,text="E-mail:",font=('arial',10,'bold'))
                label_Email.place(x=0,y=40)

                label_Email_value = Label(showdataframe,text=row[2],font=('arial',10,'bold'))
                label_Email_value.place(x=120,y=40)

                label_Address = Label(showdataframe,text="Address:",font=('arial',10,'bold'))
                label_Address.place(x=0,y=60)

                label_Address_value = Label(showdataframe,text=row[3],font=('arial',10,'bold'))
                label_Address_value.place(x=120,y=60)
        

    def get_record_count(self):
        cursor.execute("SELECT COUNT(*) FROM Service")
        record_count = cursor.fetchone()[0]
        return record_count


    def add_record(self):
        if self.var_no_room.get() == "" or  self.var_typs.get() == "" or self.var_no_person.get() == "" :
            messagebox.showerror("Error","All fields are required", parent=self.root)
        else:
            try:
                query = ('Select CIN from booking  where booking.no_room=%s and (current_date()) between check_in and check_out')
                value = (self.var_no_room.get(),)
                cursor.execute(query,value)
                cin = cursor.fetchone()[0]
                current_date = date.today()
                        
                cursor.execute("insert into Service values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.get_record_count()+1,
                    self.Service_Type_entry.get(),
                    self.price,
                    current_date,
                    self.var_no_room.get(),
                    self.var_no_person.get(),
                    cin,
                ))
                messagebox.showinfo("Success","Service has been added", parent=self.root)
                db_connection.commit()
                self.view_records()
                self.no_room_entry.delete(0, END)
                self.no_person_entry.delete(0, END)
                self.Service_Type_entry.current(0)
                self.Price_entry.config(text=100)
            
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong{str(es)}", parent=self.root)

    def view_records(self):
        cursor.execute("select id_sevice, cin, no_room, type_sevice, price_service, date_service, no_person from  Service")
        rows = cursor.fetchall()
        self.data_table.delete(*self.data_table.get_children())
        for i in rows:
            self.data_table.insert("", END, values=i)
        db_connection.commit()
        
    def get_record(self, event=""):
        select_row = self.data_table.focus()
        content = self.data_table.item(select_row)
        row = content["values"]
        
        self.service = row[0]
        self.var_no_room.set(row[2])
        self.Price_entry.config(text=row[4])
        self.var_no_person.set(row[6])
        if  row[3] == 'Breakfast Service':
            self.Service_Type_entry.current(0)
        elif row [3]=="Lunch Service":
            self.Service_Type_entry.current(1)
        elif row [3]=="Dinner Service":
            self.Service_Type_entry.current(2)
        elif row [3]=="In-Room Dining":
            self.Service_Type_entry.current(3)

    def update(self):
        if self.var_no_room.get() == "" or  self.var_typs.get() == "" or self.var_no_person.get() == "":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        else:
                cursor.execute("update service set no_room=%s,type_sevice=%s,no_person=%s,price_service=%s where ID_Sevice=%s",(
                    self.no_room_entry.get(),
                    self.Service_Type_entry.get(),
                    self.no_person_entry.get(),
                    self.price,
                    self.service
                ))
                db_connection.commit()
                self.view_records()
                self.no_room_entry.delete(0, END)
                self.no_person_entry.delete(0, END)
                self.Service_Type_entry.current(0)
                self.Price_entry.config(text=100)
                messagebox.showinfo("Update","Service information has been update successfully", parent=self.root)
    
    def reset(self):
        self.no_room_entry.delete(0, END)
        self.no_person_entry.delete(0, END)
        self.Service_Type_entry.current(0)
        self.Price_entry.config(text=100)
            
    def delete(self):
        ask = messagebox.askyesno("","do you want delete this Service",parent=self.root)
        if ask == True :
            query = "delete from service where ID_sevice=%s"
            data = (self.service,)
            cursor.execute(query,data)
            db_connection.commit()
            self.view_records()
            self.no_room_entry.delete(0, END)
            self.no_person_entry.delete(0, END)
            self.Service_Type_entry.current(0)
            self.Price_entry.config(text=100)

    def search(self):
        if self.var_search.get() == 'CIN' :
            cursor.execute(f"select id_sevice, cin, no_room, type_sevice, price_service, date_service, no_person from Service where CIN like '%{self.var_entsearch.get()}%'")
        elif self.var_search.get() == 'Room' :
            cursor.execute(f"select id_sevice, cin, no_room, type_sevice, price_service, date_service, no_person from Service where no_room like '%{self.var_entsearch.get()}%'")

        rows = cursor.fetchall()
        self.data_table.delete(*self.data_table.get_children())
        for i in rows:
            self.data_table.insert('', END, values=i)
        db_connection.commit()

if __name__ == "__main__":
    root = Tk()
    Service(root)
    root.mainloop()