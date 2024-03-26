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

class Billing:
    def __init__(self, root):
        self.root = root
        self.root.title("Billing")
        self.root.geometry("1083x405+200+235")
        self.root.resizable(False, False)
        self.root.iconbitmap ("img\\logo.ico")

        self.billing = None
        self.price = 100
        self.var_no_person = StringVar()
        self.var_cin = StringVar()

        lab1 = Label(self.root, text='Billing Details', font=('arial',18,'bold'), bg='black',fg='white')
        lab1.place(x=0, y=0, width=1083, height=50)

        imgr1 = Image.open("C:\\Users\\saad\\Desktop\\DG\\miniproject\\img\\logoo.jpg")
        imgr1 = imgr1.resize((100, 50))
        self.photor1 = ImageTk.PhotoImage(imgr1)

        lab = Label(self.root, image=self.photor1, bd=0, relief=RIDGE)
        lab.place(x=0, y=0)

        lab = Label(self.root, image=self.photor1, bd=0, relief=RIDGE)
        lab.place(x=983, y=0)

        labframe1 = LabelFrame(self.root, bd=2, relief=RIDGE, text='Billing INFO', font=('arial',10,'bold'), padx=2)
        labframe1.place(x=5, y=51 ,width=380,height=352)

        imgr = Image.open("C:\\Users\\saad\\Desktop\\DG\\miniproject\\img\\billing.jpg")
        imgr = imgr.resize((370, 110))
        self.photor = ImageTk.PhotoImage(imgr)

        labr = Label(labframe1, image=self.photor, bd=0, relief=RIDGE)
        labr.place(x=0, y=0)

        # Room number
        CIN_lab = Label(labframe1, text='CIN :', font=('arialn',12), padx=2, pady=10)
        CIN_lab.place(x=0 , y=115)

        self.cin_entry = Entry(labframe1, textvariable=self.var_cin, font=('arial',12),width=15)
        self.cin_entry.place(x=150 , y=125)

        # Button

        btnfetchdata = Button(labframe1, text='Fetch Data', command=self.fetch_services, font=('arial', 9, 'bold'), bg='black', fg='white', width=8)
        btnfetchdata.place(x=300,y=123)

        # Price_Room

        PriceRoom_lab = Label(labframe1, text='Room Price :', font=('arialn',12), padx=2, pady=10)
        PriceRoom_lab.place(x=0 , y=150)

        self.PriceRoom_entry = Label(labframe1, text=0, font=('arial',12),width=23)
        self.PriceRoom_entry.place(x=150, y=160)

        # Price

        Price_lab = Label(labframe1, text='Price :', font=('arialn',12), padx=2, pady=10)
        Price_lab.place(x=0 , y=185)

        self.Price_entry = Label(labframe1, text=0, font=('arial',12),width=23)
        self.Price_entry.place(x=150, y=195)

        # btn

        btnframe = Frame(labframe1, padx=2, pady=3)
        btnframe.place(x=5, y=220, width= 360, height=200)

        addbtn = Button(btnframe, text='Buy', command=self.add_record, font=('arial', 12, 'bold'), bg='black', fg='white', width=36, height=2)
        addbtn.grid(row=0, column=0, padx=2, pady=2, columnspan=2)

        resbtn = Button(btnframe, text='Reset',command=self.reset, font=('arial', 12, 'bold'), bg='black', fg='white', width=17, height=2)
        resbtn.grid(row=1, column=0, padx=0, pady=2)

        delbtn = Button(btnframe, text='Delete', command=self.delete, font=('arial', 12, 'bold'), bg='black', fg='white', width=17, height=2)
        delbtn.grid(row=1, column=1, padx=0, pady=2)
        
        #fetch data
        framefetch = Frame(self.root, bd=2, relief=RIDGE)
        framefetch.place(x=386, y=51, width= 293, height=99)

        tablefetch = Frame(framefetch, bd=2, relief=RIDGE)
        tablefetch.place(x=0, y=0, width=290, height=99)

        scrollxfetch = Scrollbar(tablefetch, orient=HORIZONTAL)
        scrollyfetch = Scrollbar(tablefetch, orient=VERTICAL)

        self.data_tablefetch=ttk.Treeview(tablefetch, columns=('TYPE_SERVICE','PRICE'),
                                        xscrollcommand=scrollxfetch.set, yscrollcommand=scrollyfetch.set)
        
        scrollxfetch.pack(side=BOTTOM, fill=X)
        scrollyfetch.pack(side=RIGHT, fill=Y)

        scrollxfetch.config(command=self.data_tablefetch.xview)
        scrollyfetch.config(command=self.data_tablefetch.yview)
        
        self.data_tablefetch.heading('TYPE_SERVICE', text='Service Type')
        self.data_tablefetch.heading('PRICE', text='Price')


        self.data_tablefetch['show']= "headings"

        self.data_tablefetch.column('TYPE_SERVICE', width=100)
        self.data_tablefetch.column('PRICE', width=100)

        self.data_tablefetch.pack(fill=BOTH, expand=1)

        img = "C:\\Users\\saad\\Desktop\\DG\\miniproject\\img\\billing1.jpg"
        imgr2 = Image.open(img)
        imgr2 = imgr2.resize((200, 100))
        self.photor2 = ImageTk.PhotoImage(imgr2)

        self.labimg = Label(self.root, image=self.photor2, bd=0, relief=RIDGE)
        self.labimg.place(x=880, y=51)

        img1 = "C:\\Users\\saad\\Desktop\\DG\\miniproject\\img\\billing2.jpeg"
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
        combo_search['value'] = ('CIN','ID Billing')
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

        self.data_table=ttk.Treeview(table, columns=('ID_BILLING','CIN', 'PRICE','DATE_BILLING'),
                                        xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.data_table.xview)
        scrolly.config(command=self.data_table.yview)
        
        self.data_table.heading('ID_BILLING', text='Billing ID')
        self.data_table.heading('CIN', text='CIN')
        self.data_table.heading('PRICE', text=' Price')
        self.data_table.heading('DATE_BILLING', text='Billing Date')

        self.data_table['show']= "headings"

        self.data_table.column('ID_BILLING', width=100)
        self.data_table.column('CIN', width=100)
        self.data_table.column('PRICE', width=100)
        self.data_table.column('DATE_BILLING', width=100)

        self.data_table.pack(fill=BOTH, expand=1)
        self.data_table.bind("<ButtonRelease-1>", self.get_record)
        self.view_records()


    def fetch_services(self):
        query = "select type_sevice, price_service from Service Where cin=%s"
        data = (self.cin_entry.get(),)
        cursor.execute(query,data)

        rows = cursor.fetchall()
        self.data_tablefetch.delete(*self.data_tablefetch.get_children())
        for i in rows:
            self.data_tablefetch.insert("", END, values=i)
        db_connection.commit()

        query = "select price from room join booking on booking.no_room = room.Room_number where booking.cin=%s and (current_date()) = booking.check_out"
        data = (self.cin_entry.get(),)
        cursor.execute(query,data)
        
        pr = cursor.fetchone()[0]
        if pr == None :
            pass
        else :
            self.PriceRoom_entry.config(text=pr)
            db_connection.commit()

        query = "select sum(price_service) from Service Where cin=%s"
        data = (self.cin_entry.get(),)
        cursor.execute(query,data)
        
        p = cursor.fetchone()[0]
        if p == None :
            price = int(pr)
            self.Price_entry.config(text=price)
        else :
            price = int(p) + int(pr)
            self.Price_entry.config(text=price)
        

    def get_record_count(self):
        cursor.execute("SELECT COUNT(*) FROM billing")
        record_count = cursor.fetchone()[0]
        return record_count


    def add_record(self):
        if self.var_cin.get() == "" :
            messagebox.showerror("Error","All fields are required", parent=self.root)
        else:
            try:
                current_date = date.today()
                        
                cursor.execute("insert into Billing values(%s,%s,%s,%s)",(
                    self.get_record_count()+1,
                    self.Price_entry.cget("text"),
                    current_date,
                    self.cin_entry.get()
                ))
                messagebox.showinfo("Success","Then pay the bill", parent=self.root)
                db_connection.commit()
                self.view_records()

                query = "delete from service where CIN=%s"
                data = (self.cin_entry.get(),)
                cursor.execute(query,data)
                db_connection.commit()

                self.cin_entry.delete(0, END)
                self.PriceRoom_entry.config(text=0)
                self.Price_entry.config(text=0)
                
            
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong{str(es)}", parent=self.root)

    def view_records(self):
        cursor.execute("select id_billing, cin, price, Date_billing from Billing")
        rows = cursor.fetchall()
        self.data_table.delete(*self.data_table.get_children())
        for i in rows:
            self.data_table.insert("", END, values=i)
        db_connection.commit()
        
    def get_record(self, event=""):
        select_row = self.data_table.focus()
        content = self.data_table.item(select_row)
        row = content["values"]
        
        self.billing = row[0]
        self.var_cin.set(row[1])
        self.Price_entry.config(text=row[2])
    
    def reset(self):
        self.cin_entry.delete(0, END)
        self.PriceRoom_entry.config(text=0)
        self.Price_entry.config(text=0)
            
    def delete(self):
        ask = messagebox.askyesno("","do you want delete this Bill",parent=self.root)
        if ask == True :
            parameter = [self.billing]
            query = "delete from billing where id_billing=%s"
            data = (parameter)
            cursor.execute(query,data)
            db_connection.commit()
            self.view_records()
            self.cin_entry.delete(0, END)
            self.PriceRoom_entry.config(text=0)
            self.Price_entry.config(text=0)

    def search(self):
        ('CIN','ID Billing')
        if self.var_search.get() == 'CIN' :
            cursor.execute(f"select Id_billing, cin, price, Date_billing from Billing where cin like '%{self.var_entsearch.get()}%'")
        elif self.var_search.get() == 'ID Billing' :
            cursor.execute(f"select Id_billing, cin, price, Date_billing from Billing where id_billing like '%{self.var_entsearch.get()}%'")
            
        rows = cursor.fetchall()
        self.data_table.delete(*self.data_table.get_children())
        for i in rows:
            self.data_table.insert('', END, values=i)
        db_connection.commit()

if __name__ == "__main__":
    root = Tk()
    Billing(root)
    root.mainloop()