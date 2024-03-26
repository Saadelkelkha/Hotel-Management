from tkinter import *
from PIL import Image,ImageTk
from customer import Customer
from room_booking  import  Booking
from room  import  Room
from service import Service
from biling import Billing


class Hotel:
    def __init__(self, main):
        self.main = main
        self.main.title("Hotel Management System")
        self.main.geometry("1283x640+0+0")
        self.main.resizable(False, False)
        self.main.iconbitmap ("img\\logo.ico")

        frame1 = Frame(self.main, width=200, height=640, bg='black')
        frame1.place(x=0, y=0)

        img1 = Image.open("C:\\Users\\saad\\Desktop\\DG\\miniproject\\img\\OIP (4).jpg")
        img1 = img1.resize((200, 160))
        self.photo1 = ImageTk.PhotoImage(img1)

        lab = Label(frame1, image=self.photo1, bd=4, relief=RIDGE)
        lab.place(x=0, y=0)

        img2 = Image.open("C:\\Users\\saad\\Desktop\\DG\\miniproject\\img\\OIP.jpg")
        img2 = img2.resize((200, 160))
        self.photo2 = ImageTk.PhotoImage(img2)

        lab = Label(frame1, image=self.photo2, bd=4, relief=RIDGE)
        lab.place(x=0, y=160)

        img3 = Image.open("C:\\Users\\saad\\Desktop\\DG\\miniproject\\img\\3.jpg")
        img3 = img3.resize((200, 160))
        self.photo3 = ImageTk.PhotoImage(img3)

        lab = Label(frame1, image=self.photo3, bd=4, relief=RIDGE)
        lab.place(x=0, y=320)

        img4 = Image.open("C:\\Users\\saad\\Desktop\\DG\\miniproject\\img\\R.jpg")
        img4 = img4.resize((200, 160))
        self.photo4 = ImageTk.PhotoImage(img4)

        lab = Label(frame1, image=self.photo4, bd=4, relief=RIDGE)
        lab.place(x=0, y=480)

        frame2 = Frame(self.main, width=1083, height=155)
        frame2.place(x=200, y=0)

        img5 = Image.open("C:\\Users\\saad\\Desktop\\DG\\miniproject\\img\\banner.jpg")
        img5 = img5.resize((1083, 155))
        self.photo5 = ImageTk.PhotoImage(img5)

        lab = Label(frame2, image=self.photo5, bd=4, relief=RIDGE)
        lab.pack()

        frame3 = Frame(self.main, width=1080, height=42, bg='black')
        frame3.place(x=200, y=162)

        button_width = 216

        customer_button = Button(frame3, text="Customer", bd=4, relief=RIDGE, font=('Helvetica', 14, 'bold'), fg='white', bg='black', width=17 , command=self.customer_window)
        customer_button.place(x=button_width*0, y=0)

        Booking_button = Button(frame3, text="Booking", bd=4, relief=RIDGE, font=('Helvetica', 14, 'bold'), fg='white', bg='black', width=17 , command=self.booking_window)
        Booking_button.place(x=button_width*1, y=0)
        
        Rooms_button = Button(frame3, text="Rooms", bd=4, relief=RIDGE, font=('Helvetica', 14, 'bold'), fg='white', bg='black', width=17 , command=self.room_window)
        Rooms_button.place(x=button_width*2, y=0)

        Service_button = Button(frame3, text="Service", bd=4, relief=RIDGE, font=('Helvetica', 14, 'bold'), fg='white', bg='black', width=17 , command=self.service_window)
        Service_button.place(x=button_width*3, y=0)

        Biling_button = Button(frame3, text="Biling", bd=4, relief=RIDGE, font=('Helvetica', 14, 'bold'), fg='white', bg='black',width=17 , command=self.billing_window)
        Biling_button.place(x=button_width*4, y=0)

        frame4 = Frame(self.main, width=1083, height=438)
        frame4.place(x=200, y=205)

        img6 = Image.open("C:\\Users\\saad\\Desktop\\DG\\miniproject\\img\\mamounia.jpg")
        img6 = img6.resize((1083, 430))
        self.photo6 = ImageTk.PhotoImage(img6)

        lab = Label(frame4, image=self.photo6, bd=4, relief=RIDGE)
        lab.pack()
    
    def customer_window(self):
        self.cust_window = Toplevel(self.main)
        self.app = Customer(self.cust_window)

    def booking_window(self):
        self.book_window = Toplevel(self.main)
        self.app = Booking(self.book_window)

    def room_window(self):
        self.Room_window = Toplevel(self.main)
        self.app = Room(self.Room_window)

    def service_window(self):
        self.Service_window = Toplevel(self.main)
        self.app = Service(self.Service_window)

    def billing_window(self):
        self.Billing_window = Toplevel(self.main)
        self.app = Billing(self.Billing_window)


if __name__ == "__main__":
    main = Tk()
    Hotel(main)
    main.mainloop()