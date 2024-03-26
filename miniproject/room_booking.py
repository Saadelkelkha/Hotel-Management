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

class Booking:
    def __init__(self, root):
        self.root = root
        self.root.title("Booking")
        self.root.geometry("1083x405+200+235")
        self.root.resizable(False, False)
        self.root.iconbitmap ("img\\logo.ico")

        self.booking = None
        self.var_cin = StringVar()
        self.var_check_in = StringVar()
        self.var_check_out = StringVar()
        self.var_no_room = StringVar()
        self.var_no_day = StringVar()

        lab1 = Label(self.root, text='Room Booking Details', font=('arial',18,'bold'), bg='black',fg='white')
        lab1.place(x=0, y=0, width=1083, height=50)

        imgr1 = Image.open("C:\\Users\\saad\\Desktop\\DG\\miniproject\\img\\logoo.jpg")
        imgr1 = imgr1.resize((100, 50))
        self.photor1 = ImageTk.PhotoImage(imgr1)

        lab = Label(self.root, image=self.photor1, bd=0, relief=RIDGE)
        lab.place(x=0, y=0)

        lab = Label(self.root, image=self.photor1, bd=0, relief=RIDGE)
        lab.place(x=983, y=0)

        labframe1 = LabelFrame(self.root, bd=2, relief=RIDGE, text='Room Booking INFO', font=('arial',10,'bold'), padx=2)
        labframe1.place(x=5, y=51 ,width=380,height=352)

        # CIN
        cin_lab = Label(labframe1, text='CIN :', font=('arialn',12), padx=2, pady=10)
        cin_lab.grid(row=0, column=0, sticky=W)

        self.cin_entry = Entry(labframe1, textvariable=self.var_cin, font=('arial',12),width=15)
        self.cin_entry.grid(row=0, column=1, sticky=W)

        # Button

        btnfetchdata = Button(labframe1, text='Fetch Data', command=self.fetch_contact, font=('arial', 9, 'bold'), bg='black', fg='white', width=8)
        btnfetchdata.place(x=300,y=6)

        # CHECK IN DATE

        Check_in_date_lab = Label(labframe1, text='Check_In Date :', font=('arialn',12), padx=2, pady=10)
        Check_in_date_lab.grid(row=1, column=0, sticky=W)

        self.Check_in_date_entry = Entry(labframe1, textvariable=self.var_check_in ,font=('arial',12),width=23)
        self.Check_in_date_entry.grid(row=1, column=1)

        # CHECK OUT DATE

        Check_out_date_lab = Label(labframe1, text='Check_Out Date :', font=('arialn',12), padx=2, pady=10)
        Check_out_date_lab.grid(row=2, column=0, sticky=W)

        self.Check_out_date_entry = Entry(labframe1, textvariable=self.var_check_out, font=('arial',12),width=23)
        self.Check_out_date_entry.grid(row=2, column=1)

        # Room type 

        room_type_lab = Label(labframe1, text='Room type :', font=('arialn',12), padx=2, pady=10)
        room_type_lab.grid(row=3, column=0, sticky=W)

        self.room_type_entry = ttk.Combobox(labframe1, font=('arial', 13, 'bold'), state='readonly')
        self.room_type_entry['value'] = ('Deluxe','Superior','Classic','Suite')
        self.room_type_entry.current(0)
        self.room_type_entry.grid(row=3, column=1, padx=2, pady=4)
        self.var_typp = self.room_type_entry.get()
        self.room_type_entry.bind("<<ComboboxSelected>>", self.update_room_type_value)

        # No Room 

        no_room_lab = Label(labframe1, text='No Room :', font=('arialn',12), padx=2, pady=10)
        no_room_lab.grid(row=4, column=0, sticky=W)

        self.no_room_entry = Entry(labframe1, textvariable=self.var_no_room, font=('arial',12),width=23)
        self.no_room_entry.grid(row=4, column=1)

        # No of Days 

        No_of_Days_lab = Label(labframe1, text='No of Days :', font=('arialn',12), padx=2, pady=10)
        No_of_Days_lab.grid(row=5, column=0, sticky=W)

        self.No_of_Days_entry = Entry(labframe1, textvariable=self.var_no_day, font=('arial',12),width=23)
        self.No_of_Days_entry.grid(row=5, column=1)

        # btn

        btnframe = Frame(labframe1, padx=2, pady=3)
        btnframe.place(x=0, y=270, width= 370, height=30)

        addbtn = Button(btnframe, text='Add', command=self.add_record, font=('arial', 12, 'bold'), bg='black', fg='white', width=8)
        addbtn.grid(row=0, column=0, padx=1)

        upbtn = Button(btnframe, text='Update', command=self.update, font=('arial', 12, 'bold'), bg='black', fg='white', width=8)
        upbtn.grid(row=0, column=1, padx=1)

        resbtn = Button(btnframe, text='Reset',command=self.reset, font=('arial', 12, 'bold'), bg='black', fg='white', width=8)
        resbtn.grid(row=0, column=2, padx=1)

        delbtn = Button(btnframe, text='Delete', command=self.delete, font=('arial', 12, 'bold'), bg='black', fg='white', width=8)
        delbtn.grid(row=0, column=3, padx=1)

        #fetch data

        img = "C:\\Users\\saad\\Desktop\\DG\\miniproject\\img\\deluxe.jpeg"
        imgr2 = Image.open(img)
        imgr2 = imgr2.resize((200, 100))
        self.photor2 = ImageTk.PhotoImage(imgr2)

        self.labimg = Label(self.root, image=self.photor2, bd=0, relief=RIDGE)
        self.labimg.place(x=880, y=51)

        img1 = "C:\\Users\\saad\\Desktop\\DG\\miniproject\\img\\suite.jpg"
        imgr3 = Image.open(img1)
        imgr3 = imgr3.resize((200, 100))
        self.photor3 = ImageTk.PhotoImage(imgr3)

        self.labimg = Label(self.root, image=self.photor3, bd=0, relief=RIDGE)
        self.labimg.place(x=680, y=51)

    
        # frame search 
        
        labframe2 = LabelFrame(self.root, bd=2, relief=RIDGE, text='Show Booking Info ', font=('arial',10,'bold'), padx=2)
        labframe2.place(x=386, y=150 ,width=695,height=352)

        searchlab = Label(labframe2, text='Search By:', font=('arial', 12, 'bold'), bg='red', fg='white', padx=2, pady=4)
        searchlab.grid(row=0, column=0, sticky=W)

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

        self.data_table=ttk.Treeview(table, columns=('ID_BOOKING','CIN', 'Booking_date','Check-IN','Check-OUT','Number_of_Days','Room_number','Room_Type'),
                                        xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.data_table.xview)
        scrolly.config(command=self.data_table.yview)
        
        self.data_table.heading('ID_BOOKING', text='Booking ID')
        self.data_table.heading('CIN', text='CIN')
        self.data_table.heading('Booking_date', text='Booking date')
        self.data_table.heading('Check-IN', text='Check-IN')
        self.data_table.heading('Check-OUT', text='Check-OUT')
        self.data_table.heading('Number_of_Days', text='Number of Days')
        self.data_table.heading('Room_number', text='Room Number')
        self.data_table.heading('Room_Type', text='Room Type')

        self.data_table['show']= "headings"

        self.data_table.column('ID_BOOKING', width=100)
        self.data_table.column('CIN', width=100)
        self.data_table.column('Booking_date', width=100)
        self.data_table.column('Check-IN', width=100)
        self.data_table.column('Check-OUT', width=100)
        self.data_table.column('Number_of_Days', width=100)
        self.data_table.column('Room_number', width=100)
        self.data_table.column('Room_Type', width=100)

        self.data_table.pack(fill=BOTH, expand=1)
        self.data_table.bind("<ButtonRelease-1>", self.get_record)
        self.view_records()

    def update_room_type_value(self, event):
        self.var_typp = self.room_type_entry.get()

    def fetch_contact(self):
        if self.var_cin.get()=='':
            messagebox.showerror('Error','Please enter CIN',parent=self.root)
        else:
            query = ('Select first_Name, last_name, email, address from customer where  cin=%s')
            value = (self.cin_entry.get(),)
            cursor.execute(query,value)
            row = cursor.fetchone()

            if row == None :
                messagebox.showerror("Error", 'No Customer Found with this CIN', parent=self.root)
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
        cursor.execute("SELECT COUNT(*) FROM Booking")
        record_count = cursor.fetchone()[0]
        return record_count


    def add_record(self):
        if self.var_check_in.get() == "" or  self.var_check_out.get() == "" or self.var_cin.get() == "" or self.var_no_day.get() == "" or self.var_no_room.get() == "":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        else:
            if re.search(r"\d{4}-\d{2}-\d{2}",self.var_check_in.get()) == FALSE or re.search(r"\d{4}-\d{2}-\d{2}",self.var_check_out.get()) == FALSE:
                messagebox.showerror("Error","Enter the date on the following form: YYYY-MM-DD", parent=self.root)
            else:
                query = ('Select Availabe_status from room where room_number=%s')
                value = (self.var_no_room.get(),)
                cursor.execute(query,value)
                Availabe_status_room = cursor.fetchone()
                if Availabe_status_room == 'Booked up' or Availabe_status_room == 'In maintenance':
                    messagebox.showerror("Room is not available", "Room is not available" ,parent=self.root)
                else:
                    try:
                        current_date = date.today()
                        
                        cursor.execute("insert into Booking values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                        self.get_record_count()+1,
                        current_date,
                        self.var_check_in.get(),
                        self.var_check_out.get(),
                        self.var_no_day.get(),
                        self.var_no_room.get(),
                        self.room_type_entry.get(),
                        self.cin_entry.get()
                        ))
                        messagebox.showinfo("Success","Booking has been added", parent=self.root)
                        db_connection.commit()
                        self.view_records()
                        self.cin_entry.delete(0, END)
                        self.Check_in_date_entry.delete(0, END)
                        self.Check_out_date_entry.delete(0, END)
                        self.no_room_entry.delete(0, END)
                        self.No_of_Days_entry.delete(0, END)
                        self.room_type_entry.current(0)
            
                    except Exception as es:
                        messagebox.showwarning("Warning",f"Some thing went wrong{str(es)}", parent=self.root)

    def view_records(self):
        cursor.execute("select id_booking, cin, bo_date, check_in, check_out, no_days, no_room, room_type from  booking")
        rows = cursor.fetchall()
        self.data_table.delete(*self.data_table.get_children())
        for i in rows:
            self.data_table.insert("", END, values=i)
        db_connection.commit()
        
    def get_record(self, event=""):
        select_row = self.data_table.focus()
        content = self.data_table.item(select_row)
        row = content["values"]
        
        self.booking = row[0]
        self.var_cin.set(row[1])
        self.var_check_in.set(row[3])
        self.var_check_out.set(row[4])
        self.var_no_room.set(row[6])
        self.var_no_day.set(row[5])

        if  row[7] == 'Deluxe':
            self.room_type_entry.current(0)
        elif row [7]=="Superior":
            self.room_type_entry.current(1)
        elif row [7]=="Classic":
            self.room_type_entry.current(2)
        else:
            self.room_type_entry.current(3)

    def update(self):
        if self.var_check_in.get() == "" or  self.var_check_out.get() == "" or self.var_cin.get() == "" or self.var_no_day.get() == "" or self.var_no_room.get() == "":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        else:
            if re.search(r"\d{4}-\d{2}-\d{2}",self.var_check_in.get()) == FALSE or re.search(r"\d{4}-\d{2}-\d{2}",self.var_check_out.get()) == FALSE:
                messagebox.showerror("Error","Enter the date on the following form: YYYY-MM-DD", parent=self.root)
            else:
                cursor.execute("update booking set check_in=%s,check_out=%s,no_days=%s,cin=%s,no_room=%s,room_type=%s where ID_Booking=%s",(
                    self.Check_in_date_entry.get(),
                    self.Check_out_date_entry.get(),
                    self.No_of_Days_entry.get(),
                    self.cin_entry.get(),
                    self.no_room_entry.get(),
                    self.room_type_entry.get(),
                    self.booking
                ))
                db_connection.commit()
                self.view_records()
                self.cin_entry.delete(0, END)
                self.Check_in_date_entry.delete(0, END)
                self.Check_out_date_entry.delete(0, END)
                self.no_room_entry.delete(0, END)
                self.No_of_Days_entry.delete(0, END)
                self.room_type_entry.current(0)
                messagebox.showinfo("Update","Booking information has been update successfully", parent=self.root)
    
    def reset(self):
        self.cin_entry.delete(0, END)
        self.Check_in_date_entry.delete(0, END)
        self.Check_out_date_entry.delete(0, END)
        self.no_room_entry.delete(0, END)
        self.No_of_Days_entry.delete(0, END)
        self.room_type_entry.current(0)
            
    def delete(self):
        ask = messagebox.askyesno("","do you want delete this booking",parent=self.root)
        if ask == True :
            query = "delete from booking where ID_booking=%s"
            data = (self.booking, )
            cursor.execute(query,data)
            db_connection.commit()
            self.view_records()
            self.cin_entry.delete(0, END)
            self.Check_in_date_entry.delete(0, END)
            self.Check_out_date_entry.delete(0, END)
            self.no_room_entry.delete(0, END)
            self.No_of_Days_entry.delete(0, END)
            self.room_type_entry.current(0)
    
    def search(self):
        cursor.execute(f"select ID_booking, cin, bo_date, check_in, check_out, no_days, no_room, room_type from booking where {self.var_search.get()} like '%{self.var_entsearch.get()}%'")
        rows = cursor.fetchall()
        self.data_table.delete(*self.data_table.get_children())
        for i in rows:
            self.data_table.insert('', END, values=i)
        db_connection.commit()

if __name__ == "__main__":
    root = Tk()
    Booking(root)
    root.mainloop()