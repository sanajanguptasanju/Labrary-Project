from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime



class LibraryManagementSystem:
    def __init__(self, root):
        self.add_data = None
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        # ==============================variable=============================
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.auther_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finalprice = StringVar()

        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd=10, relief=RIDGE,
                         font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=450)

        # ===========================================DataFrameLeft=======================

        DataFrameLeft = LabelFrame(frame, text="Library Mambarship Information", bg="powder blue", fg="green", bd=10,
                                   relief=RIDGE, font=("times new roman", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=780, height=350)

        lblMember = Label(DataFrameLeft, bg="powder blue", text="Member type", font=("times new roman", 12, "bold"),
                          padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, textvariable=self.member_var, font=("times new roman", 12, "bold"),
                                 width=27, state="readonly")
        comMember["value"] = ("Admin Staff", "Student", "Lecturer")
        comMember.current(0)
        comMember.grid(row=0, column=1)

        lblPRN_NO = Label(DataFrameLeft, font=("arial", 12, "bold"), text="PRN NO:", padx=2, pady=6, bg="powder blue")
        lblPRN_NO.grid(row=1, column=0, sticky=W)
        txtPRN_NO = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.prn_var, width=26)
        txtPRN_NO.grid(row=1, column=1)

        lbltitle = Label(DataFrameLeft, font=("arial", 12, "bold"), text="ID NO:", padx=2, pady=6, bg="powder blue")
        lbltitle.grid(row=2, column=0, sticky=W)
        txttitle = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.id_var, width=26)
        txttitle.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="FirstName", padx=2, pady=6,
                             bg="powder blue")
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.firstname_var, width=26)
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="LastName", padx=2, pady=6,
                            bg="powder blue")
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.lastname_var, width=26)
        txtLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address1", padx=2, pady=6,
                            bg="powder blue")
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.address1_var, width=26)
        txtAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address2", padx=2, pady=6,
                            bg="powder blue")
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.address2_var, width=26)
        txtAddress2.grid(row=6, column=1)

        lblPostCode = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Post Code", padx=2, pady=6,
                            bg="powder blue")
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.postcode_var, width=26)
        txtPostCode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Mobile", padx=2, pady=6, bg="powder blue")
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.mobile_var, width=26)
        txtMobile.grid(row=8, column=1)

        lblBookId = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book ID:", padx=2, pady=6, bg="powder blue")
        lblBookId.grid(row=0, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.bookid_var, width=26)
        txtBookId.grid(row=0, column=3)

        lblBookTitle = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book Title:", padx=2, pady=6,
                             bg="powder blue")
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.booktitle_var, width=26)
        txtBookTitle.grid(row=1, column=3)

        lblAuther = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Auther Name:", padx=2, pady=6,
                          bg="powder blue")
        lblAuther.grid(row=2, column=2, sticky=W)
        txtAuther = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.auther_var, width=26)
        txtAuther.grid(row=2, column=3)

        lblDateBorrowed = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Borrowed:", padx=2, pady=6,
                                bg="powder blue")
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.dateborrowed_var, width=26)
        txtDateBorrowed.grid(row=3, column=3)

        lblDateDue = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Due:", padx=2, pady=6,
                           bg="powder blue")
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.datedue_var, width=26)
        txtDateDue.grid(row=4, column=3)

        lblDaysOnBook = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Days On Book:", padx=2, pady=6,
                              bg="powder blue")
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.daysonbook_var, width=26)
        txtDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Late Return Fine:", padx=2, pady=6,
                                  bg="powder blue")
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.latereturnfine_var,
                                  width=26)
        txtLateReturnFine.grid(row=6, column=3)

        lblDateOverdate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Over Due:", padx=2, pady=6,
                                bg="powder blue")
        lblDateOverdate.grid(row=7, column=2, sticky=W)
        txtDateOverdate = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.dateoverdue_var, width=26)
        txtDateOverdate.grid(row=7, column=3)

        lblActualPrice = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Actual Price:", padx=2, pady=6,
                               bg="powder blue")
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.finalprice, width=26)
        txtActualPrice.grid(row=8, column=3)

        # =======================================DataFrame Right=============================

        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue", fg="green", bd=12, relief=RIDGE,
                                    font=("arial", 12, "bold"))
        DataFrameRight.place(x=800, y=5, width=560, height=350)

        self.txtBox = Text(DataFrameRight, font=("arial", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")

        listBooks = ['Python', 'Java', 'Data Structure', 'C++', 'C', 'Php', 'Web Technology',
                     'A Better India: A Better World', 'A Passage to India', 'A Revenue Stamp', 'Death of a City',
                     'Pinjar', 'A Suitable Boy']

        def SelectBook(event):
            value = str(listBox.get(listBox.curselection()))
            x = value
            if (x == "Python"):
                self.bookid_var.set("BH1234H")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Guido Van Ressoum")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.200")
                self.dateoverdue_var.set("NO")
                self.finalprice.set("Rs.700")

            elif (x == "Java"):
                self.bookid_var.set("BH1235GH")
                self.booktitle_var.set("basic java")
                self.auther_var.set("James Gosling")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.300")
                self.dateoverdue_var.set("NO")
                self.finalprice.set("Rs.200")

            elif (x == "Data Structure"):
                self.bookid_var.set("AB5541N")
                self.booktitle_var.set("data")
                self.auther_var.set("Mickel")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.200")
                self.dateoverdue_var.set("NO")
                self.finalprice.set("Rs.500")

            elif (x == "C++"):
                self.bookid_var.set("BH1234H")
                self.booktitle_var.set("C12")
                self.auther_var.set("Bjarne Strostups")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.200")
                self.dateoverdue_var.set("NO")
                self.finalprice.set("Rs.300")

            elif (x == "C"):
                self.bookid_var.set("A187H")
                self.booktitle_var.set("basic C")
                self.auther_var.set("Dennis Ritche")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.200")
                self.dateoverdue_var.set("NO")
                self.finalprice.set("Rs.250")

            elif (x == "Php"):
                self.bookid_var.set("GHH2J")
                self.booktitle_var.set("basic php")
                self.auther_var.set("Ramaus")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.200")
                self.dateoverdue_var.set("NO")
                self.finalprice.set("Rs.350")

            elif (x == "Web Technology"):
                self.bookid_var.set("TY677")
                self.booktitle_var.set("web")
                self.auther_var.set("Akshi Kumar")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.200")
                self.dateoverdue_var.set("NO")
                self.finalprice.set("Rs.500")

            elif (x == "A Better India:"):
                self.bookid_var.set("A187H")
                self.booktitle_var.set("basic ")
                self.auther_var.set("Dennis")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.200")
                self.dateoverdue_var.set("NO")
                self.finalprice.set("Rs.600")

        listBox = Listbox(DataFrameRight, font=("arial", 12, "bold"), width=20, height=16)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)

        # =======================================Button Frame==================================

        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1400, height=70)

        btnAddData = Button(Framebutton, command=self.add_data, text="Add Data", font=("arial", 12, "bold"), width=22,
                            bg="blue", fg="white")
        btnAddData.grid(row=0, column=0)

        btnAddData = Button(Framebutton, text="Show Data", font=("arial", 12, "bold"), width=22, bg="blue", fg="white")
        btnAddData.grid(row=0, column=1)

        btnAddData = Button(Framebutton, text="Update", font=("arial", 12, "bold"), width=22, bg="blue", fg="white")
        btnAddData.grid(row=0, column=2)

        btnAddData = Button(Framebutton, text="Delete", font=("arial", 12, "bold"), width=22, bg="blue", fg="white")
        btnAddData.grid(row=0, column=3)

        btnAddData = Button(Framebutton, text="Reset", font=("arial", 12, "bold"), width=22, bg="blue", fg="white")
        btnAddData.grid(row=0, column=4)

        btnAddData = Button(Framebutton, text="Exit", font=("arial", 12, "bold"), width=22, bg="blue", fg="white")
        btnAddData.grid(row=0, column=5)

        # =====================================Information Frame===============================
        FrameDetails = Frame(self.root, bd=10, relief=RIDGE, padx=10, bg="powder blue")
        FrameDetails.place(x=0, y=590, width=1530, height=210)

        Table_Frame = Frame(FrameDetails, bd=3, relief=RIDGE, bg="powder blue")
        Table_Frame.place(x=0, y=0, width=1330, height=100)

        xscroll = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(Table_Frame, columns=(
        "membertype", "prnno", "title", 'firstname', 'lastname', 'address1', 'address2',
        'postid', 'mobile', 'bookid', 'booktitle', 'auther', 'dateborrowed', 'datedue', 'days', 'latereturnfine',
        'dateoverdue', 'finalprice'), xscrollcommand=xscroll.set, yscrollcommand=xscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("prnno", text="PRN NO")
        self.library_table.heading("title", text="Title")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address1")
        self.library_table.heading("address2", text="Address2")
        self.library_table.heading("postid", text="Post ID")
        self.library_table.heading("mobile", text="Mobile")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("auther", text="Auther")
        self.library_table.heading("dateborrowed", text="Date of Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="DaysOnBook")
        self.library_table.heading("latereturnfine", text="LateReturnFine")
        self.library_table.heading("dateoverdue", text="DateOverDue")
        self.library_table.heading("finalprice", text="Final Price")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("membertype", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("title", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("auther", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)

        self.fatch_data()

        def add_data(self):
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="table")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.member_var.get(),
                self.prn_no.get(),
                self.id_var.get(),

                self.firstname.get(),
                self.lastname.get(),
                self.address1.get(),
                self.address2.get(),
                self.postcode_var.get(),
                self.mobile_var.get(),
                self.bookid_var.get(),
                self.booktitle_var.get(),
                self.auther_var.get(),
                self.dateborrowed_var.get(),
                self.datedue_var.get(),
                self.daysonbook_var.get(),
                self.latereturnfine_var.get(),
                self.dateoverdue_var.get(),
                self.finalprice_var.get(),
            ))

            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success", "Member has been inserted successfully.")

        def fatch_data(self):
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="table")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from library")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.library_table.delete(*self.library_table.get_children())
                for i in rows:
                    self.library_table.insert("", END, values=i)
                conn.commit()
            conn.close()

    def fatch_data(self):
        pass


if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
