from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

import mysql.connector

# Connect to MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
    database="Hotel"
)
cursor = db_connection.cursor()

class Customer:
    def __init__(self, root):
        self.root = root
        self.root.title("Add Customer")
        self.root.geometry("1083x405+200+235")
        self.root.resizable(False, False)
        self.root.iconbitmap ("img\\logo.ico")

        self.var_fn = StringVar()
        self.var_ln = StringVar()
        self.var_cin = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_nat = StringVar()

        lab1 = Label(self.root, text='ADD CUSTOMER INFORMATION', font=('arial',18,'bold'), bg='black',fg='white')
        lab1.place(x=0, y=0, width=1083, height=50)

        img4 = Image.open("C:\\Users\\saad\\Desktop\\DG\\miniproject\\img\\logoo.jpg")
        img4 = img4.resize((100, 50))
        self.photo4 = ImageTk.PhotoImage(img4)

        lab = Label(self.root, image=self.photo4, bd=0, relief=RIDGE)
        lab.place(x=0, y=0)

        lab = Label(self.root, image=self.photo4, bd=0, relief=RIDGE)
        lab.place(x=983, y=0)

        labframe2 = LabelFrame(self.root, bd=2, relief=RIDGE, text='CUSTOMER INFO', font=('arial',10,'bold'), padx=2)
        labframe2.place(x=5, y=51 ,width=400,height=352)

        cinlab = Label(labframe2, text='CIN :', font=('arial',12), padx=2, pady=4)
        cinlab.grid(row=0, column=0, sticky=W)

        self.cinentry = Entry(labframe2, textvariable=self.var_cin, font=('arial',12))
        self.cinentry.grid(row=0, column=1)

        fnlab = Label(labframe2, text='First Name :', font=('arialn',12), padx=2, pady=4)
        fnlab.grid(row=1, column=0, sticky=W)

        self.fnentry = Entry(labframe2, textvariable=self.var_fn, font=('arial',12))
        self.fnentry.grid(row=1, column=1)

        lnlab = Label(labframe2, text='Last Name :', font=('arial',12), padx=2, pady=4)
        lnlab.grid(row=2, column=0, sticky=W)

        self.lnentry = Entry(labframe2, textvariable=self.var_ln, font=('arial',12))
        self.lnentry.grid(row=2, column=1)

        phlab = Label(labframe2, text='Phone :', font=('arial',12), padx=2, pady=4)
        phlab.grid(row=3, column=0, sticky=W)

        self.phentry = Entry(labframe2, textvariable=self.var_phone, font=('arial',12))
        self.phentry.grid(row=3, column=1)

        emaillab = Label(labframe2, text='E-mail :', font=('arial',12), padx=2, pady=4)
        emaillab.grid(row=4, column=0, sticky=W)

        self.emailentry = Entry(labframe2, textvariable=self.var_email, font=('arial',12))
        self.emailentry.grid(row=4, column=1)

        addresslab = Label(labframe2, text='Address :', font=('arial',12), padx=2, pady=4)
        addresslab.grid(row=5, column=0, sticky=W)

        self.addressentry = Entry(labframe2, textvariable=self.var_address, font=('arial',12))
        self.addressentry.grid(row=5, column=1)

        natlab = Label(labframe2, text='Nationality :', font=('arial',12), padx=2, pady=4)
        natlab.grid(row=6, column=0, sticky=W)

        self.natentry = Entry(labframe2, textvariable=self.var_nat, font=('arial',12))
        self.natentry.grid(row=6, column=1)

        pilab = Label(labframe2, text='Payment Info :', font=('arial',12), padx=2, pady=4)
        pilab.grid(row=7, column=0, sticky=W)

        self.combo_pi = ttk.Combobox(labframe2, font=('arial', 12, 'bold'), state='readonly')
        self.combo_pi['value'] = ('Cash','Visa','Mastercard')
        self.combo_pi.current(0)
        self.combo_pi.grid(row=7, column=1, padx=2, pady=4)
        self.var_typp = self.combo_pi.get()
        self.combo_pi.bind("<<ComboboxSelected>>", self.update_entry_value)

        btnframe = Frame(labframe2, padx=2, pady=3)
        btnframe.place(x=0, y=260, width= 390, height=100)

        addbtn = Button(btnframe, text='Add', command=self.add_record, font=('arial', 12, 'bold'), bg='black', fg='white', width=8, height=2)
        addbtn.grid(row=0, column=0, padx=3)

        upbtn = Button(btnframe, text='Update', command=self.update, font=('arial', 12, 'bold'), bg='black', fg='white', width=8, height=2)
        upbtn.grid(row=0, column=1, padx=3)

        resbtn = Button(btnframe, text='Reset',command=self.reset, font=('arial', 12, 'bold'), bg='black', fg='white', width=8, height=2)
        resbtn.grid(row=0, column=2, padx=3)

        delbtn = Button(btnframe, text='Delete', command=self.delete, font=('arial', 12, 'bold'), bg='black', fg='white', width=8, height=2)
        delbtn.grid(row=0, column=3, padx=3)

        labframe3 = LabelFrame(self.root, bd=2, relief=RIDGE, text='Show Info ', font=('arial',10,'bold'), padx=2)
        labframe3.place(x=406, y=50 ,width=675,height=352)

        searchlab = Label(labframe3, text='Search By:', font=('arial', 12, 'bold'), bg='red', fg='white', padx=2, pady=4)
        searchlab.grid(row=0, column=0, sticky=W)

        self.var_search = StringVar()
        combo_search = ttk.Combobox(labframe3, textvariable=self.var_search, font=('arial', 12, 'bold'), width=20, state='readonly')
        combo_search['value'] = ('CIN','Phone')
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.var_entsearch = StringVar()
        searchentry = Entry(labframe3, textvariable=self.var_entsearch, font=('arial',12), width=15)
        searchentry.grid(row=0, column=2, padx=2)

        searchbtn = Button(labframe3, text='Search', command=self.search, font=('arial', 12, 'bold'), bg='black', fg='white', width=8)
        searchbtn.grid(row=0, column=3, padx=3)

        showallbtn = Button(labframe3, text='Show All', command=self.view_records, font=('arial', 12, 'bold'), bg='black', fg='white', width=8)
        showallbtn.grid(row=0, column=4, padx=3)

        table = Frame(labframe3, bd=2, relief=RIDGE)
        table.place(x=0, y=50, width=671, height=280)

        scrollx = Scrollbar(table, orient=HORIZONTAL)
        scrolly = Scrollbar(table, orient=VERTICAL)

        self.data_table=ttk.Treeview(table, columns=('CIN', 'First_Name','Last_Name','Phone','Email','Address','Type_Payment','Nationality'),
                                        xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.data_table.xview)
        scrolly.config(command=self.data_table.yview)

        self.data_table.heading('CIN', text='CIN')
        self.data_table.heading('First_Name', text='First Name')
        self.data_table.heading('Last_Name', text='Last Name')
        self.data_table.heading('Phone', text='Phone')
        self.data_table.heading('Email', text='E-mail')
        self.data_table.heading('Address', text='Adress')
        self.data_table.heading('Type_Payment', text='Payment Info')
        self.data_table.heading('Nationality', text='Nationality')

        self.data_table['show']= "headings"

        self.data_table.column('CIN', width=100)
        self.data_table.column('First_Name', width=100)
        self.data_table.column('Last_Name', width=100)
        self.data_table.column('Phone', width=100)
        self.data_table.column('Email', width=100)
        self.data_table.column('Address', width=100)
        self.data_table.column('Type_Payment', width=100)
        self.data_table.column('Nationality', width=100)

        self.data_table.pack(fill=BOTH, expand=1)
        self.data_table.bind("<ButtonRelease-1>", self.get_record)
        self.view_records()

    def update_entry_value(self, event):
            self.var_typp = self.combo_pi.get()
    
    def add_record(self):
        if self.var_fn.get() == "" or  self.var_ln.get() == "" or self.var_cin.get() == "" or self.var_phone.get() == "" or self.var_email.get() == "" or self.var_address.get() == "" or self.var_typp == "" or self.var_nat.get() == "":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        
        else:
            try:
                cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fn.get(),
                    self.var_ln.get(),
                    self.var_cin.get(),
                    self.var_phone.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_typp,
                    self.var_nat.get()
                ))
                messagebox.showinfo("Success","Customer has been added", parent=self.root)
                db_connection.commit()
                self.view_records()
                self.fnentry.delete(0, END)
                self.lnentry.delete(0, END)
                self.cinentry.delete(0, END)
                self.phentry.delete(0, END)
                self.emailentry.delete(0, END)
                self.addressentry.delete(0, END)
                self.natentry.delete(0, END)
                self.combo_pi.current(0)
            
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong{str(es)}", parent=self.root)

    def view_records(self):
        cursor.execute("select CIN, First_Name, Last_Name, Phone, Email, Address, Type_Payment, Nationality from  customer")
        rows = cursor.fetchall()
        self.data_table.delete(*self.data_table.get_children())
        for i in rows:
            self.data_table.insert("", END, values=i)
        db_connection.commit()
    
    def get_record(self, event=""):
        select_row = self.data_table.focus()
        content = self.data_table.item(select_row)
        row = content["values"]

        self.var_fn.set(row[1])
        self.var_ln.set(row[2])
        self.var_cin.set(row[0])
        self.var_phone.set(row[3])
        self.var_email.set(row[4])
        self.var_address.set(row[5])
        self.var_nat.set(row[7])

        if row[6] == "Cash" :
            self.combo_pi.current(0)
        elif row[6] == 'Visa' :
            self.combo_pi.current(1)
        elif row[6] == "Mastercard" :
            self.combo_pi.current(2)
    
    def update(self):
        if self.var_fn.get() == "" or  self.var_ln.get() == "" or self.var_cin.get() == "" or self.var_phone.get() == "" or self.var_email.get() == "" or self.var_address.get() == "" or self.var_typp == "" or self.var_nat.get() == "":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        else :
            cursor.execute("update customer set first_name=%s,last_name=%s,phone=%s,email=%s,address=%s,type_payment=%s,nationality=%s where CIN=%s",(
                    self.var_fn.get(),
                    self.var_ln.get(),
                    self.var_phone.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_typp,
                    self.var_nat.get(),
                    self.var_cin.get()
            ))
            db_connection.commit()
            self.view_records()
            self.fnentry.delete(0, END)
            self.lnentry.delete(0, END)
            self.cinentry.delete(0, END)
            self.phentry.delete(0, END)
            self.emailentry.delete(0, END)
            self.addressentry.delete(0, END)
            self.natentry.delete(0, END)
            self.combo_pi.current(0)
            messagebox.showinfo("Update","Customer information has been update successfully", parent=self.root)

    def reset(self):
        self.fnentry.delete(0, END)
        self.lnentry.delete(0, END)
        self.cinentry.delete(0, END)
        self.phentry.delete(0, END)
        self.emailentry.delete(0, END)
        self.addressentry.delete(0, END)
        self.natentry.delete(0, END)
        self.combo_pi.current(0)

    def delete(self):
        ask = messagebox.askyesno("","do you want delete this customer",parent=self.root)
        if ask == True :
            query = "delete from customer where cin=%s"
            data = (self.var_cin.get(), )
            cursor.execute(query,data)
            db_connection.commit()
            self.view_records()
            self.fnentry.delete(0, END)
            self.lnentry.delete(0, END)
            self.cinentry.delete(0, END)
            self.phentry.delete(0, END)
            self.emailentry.delete(0, END)
            self.addressentry.delete(0, END)
            self.natentry.delete(0, END)
            self.combo_pi.current(0)

    def search(self):
        cursor.execute(f"select cin, first_name, last_name, phone, email, address, type_payment, nationality from customer where {self.var_search.get()} like '%{self.var_entsearch.get()}%'")
        rows = cursor.fetchall()
        self.data_table.delete(*self.data_table.get_children())
        for i in rows:
            self.data_table.insert('', END, values=i)
        db_connection.commit()

if __name__ == "__main__":
    root = Tk()
    Customer(root)
    root.mainloop()