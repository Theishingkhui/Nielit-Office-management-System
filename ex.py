# project library managment devops

# interface GUI tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# library for images
from PIL import Image, ImageTk

image1 = 'library.png'
image2 = 'image2.png'
image3 = 'finance.png'

import random

# database
import sqlite3


def e_main():
    class invmenu:

        def __init__(self):
            self.root = Toplevel()
            self.root.title('Menu')
            self.root.state('zoomed')
            conn = sqlite3.connect('e.db')

            # create table item info
            conn.execute('''create table if not exists item_info
            (
            First Name VARTEXT NOT NULL,
            Last Name VARTEXT NOT NULL,
            ID VARCHAR PRIMARY KEY NOT NULL,
            Deparment VARTEXT NOT NULL,
            Shift VARTEXT NOT NULL,
            Pay FLOAT NOT NULL);''')

            conn.commit()
            # create table item issued
            conn.execute('''create table if not exists item_issued
            (
            First Name VARTEXT NOT NULL,
            Last Name VARTEXT NOT NULL,
            ID VARCHAR PRIMARY KEY NOT NULL,
            Deparment VARTEXT NOT NULL,
            Shift VARTEXT NOT NULL,
            Pay FLOAT NOT NULL);''')
            conn.commit()
            conn.close()

        def canvases(self, images):
            w = self.root.winfo_screenwidth()
            h = self.root.winfo_screenheight()

            photo = Image.open(images)
            photo1 = photo.resize((w, h), Image.ANTIALIAS)
            photo2 = ImageTk.PhotoImage(photo1)

            self.canvas = Canvas(self.root, width='%d' % w, height='%d' % h)
            self.canvas.grid(row=0, column=0)
            self.canvas.grid_propagate(0)
            self.canvas.create_image(0, 0, anchor=NW, image=photo2)
            self.canvas.image = photo2
            return self.canvas

        def emp(self):
            self.a.destroy()
            self.a = self.canvases(image2)
            l1 = Button(self.a, text='Add Employee', font='Papyrus 22 bold', fg='Orange', bg='Black', width=15, padx=10,
                        command=self.addemp).place(x=12, y=100)
            l2 = Button(self.a, text='Search Employee', font='Papyrus 22 bold', fg='Orange', bg='Black', width=15, padx=10,
                        command=self.searchemp).place(x=12, y=200)

            l4 = Button(self.a, text='Show Employee List', font='Papyrus 22 bold', fg='Orange', bg='Black', width=15,
                        padx=10, command=self.all).place(x=12, y=300)
            l4 = Button(self.a, text='<< Mark attendance', font='Papyrus 22 bold', fg='Orange', bg='Black', width=15, padx=10,
                        command=self.maininvmenu).place(x=12, y=500)

        def additem(self):
            self.afn = StringVar()
            self.aln = StringVar()
            self.aid = StringVar()
            self.adep = StringVar()
            self.ash = StringVar()
            self.apay = IntVar()

            self.f1 = Frame(self.a, height=500, width=650, bg='black')
            self.f1.place(x=500, y=100)
            l1 = Label(self.f1, text='EMP ID : ', font='Papyrus 12 bold', fg='Orange', bg='Black', pady=1).place(x=50,
                                                                                                                  y=50)
            e1 = Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.aid).place(x=150, y=50)
            l2 = Label(self.f1, text='Item : ', font='Papyrus 12 bold', fg='Orange', bg='Black', pady=1).place(x=50,
                                                                                                               y=100)
            e2 = Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.afn).place(x=150, y=100)
            l3 = Label(self.f1, text='Company : ', font='Papyrus 12 bold', fg='orange', bg='Black', pady=1).place(x=50,
                                                                                                                  y=150)
            e3 = Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.aln).place(x=150, y=150)
            l4 = Label(self.f1, text='Amount : ', font='Papyrus 12 bold', fg='orange', bg='Black', pady=1).place(x=50,
                                                                                                                 y=200)
            e2 = Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.adep).place(x=150, y=200)
            l4 = Label(self.f1, text='Copies : ', font='Papyrus 12 bold', fg='orange', bg='Black', pady=1).place(x=50,
                                                                                                                 y=250)
            e2 = Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.apay).place(x=150, y=250)
            l5 = Label(self.f1, text='Location : ', font='Papyrus 12 bold', fg='orange', bg='Black', pady=1).place(x=50,
                                                                                                                   y=300)
            e3 = Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.ash).place(x=150, y=300)
            self.f1.grid_propagate(0)
            b1 = Button(self.f1, text='Add', font='Papyrus 10 bold', fg='black', bg='orange', width=15, bd=3,
                        command=self.adddata).place(x=150, y=400)
            b2 = Button(self.f1, text='Back', font='Papyrus 10 bold', fg='black', bg='orange', width=15, bd=3,
                        command=self.rm).place(x=350, y=400)

        def rm(self):
            self.f1.destroy()

        def maininvmenu(self):
            self.root.destroy()
            a = invmenu()

        # add item information to database
        def adddata(self):
            a = self.afn.get()
            b = self.aln.get()
            c = self.aid.get()
            d = self.adep.get()
            e = self.ash.get()
            f = self.apay.get()

            conn = sqlite3.connect('e.db')
            try:
                if (a and b and c and d and f) == "":
                    messagebox.showinfo("Error", "Fields cannot be empty.")
                else:
                    conn.execute("insert into item_info \
                    values (?,?,?,?,?,?)",
                                 (a.capitalize(), b.capitalize(), c.capitalize(), d.capitalize(), e, f.capitalize(),));
                    conn.commit()
                    messagebox.showinfo("Success", "Employee added successfully")
            except sqlite3.IntegrityError:
                messagebox.showinfo("Error", "Employee already exist.")

            conn.close()

        # search methode
        def search(self):

            self.sid = StringVar()
            self.f1 = Frame(self.a, height=500, width=650, bg='black')
            self.f1.place(x=500, y=100)
            l1 = Label(self.f1, text='Enter data ', font=('Papyrus 10 bold'), bd=2, fg='orange',
                       bg='black').place(x=20, y=40)
            e1 = Entry(self.f1, width=25, bd=5, bg='orange', fg='black', textvariable=self.sid).place(x=260, y=40)
            b1 = Button(self.f1, text='Search', bg='orange', font='Papyrus 10 bold', width=9, bd=2,
                        command=self.serch1).place(x=500, y=37)
            b1 = Button(self.f1, text='Back', bg='orange', font='Papyrus 10 bold', width=10, bd=2,
                        command=self.rm).place(x=250, y=450)

        def create_tree(self, plc, lists):
            self.tree = ttk.Treeview(plc, height=13, column=(lists), show='headings')
            n = 0
            while n is not len(lists):
                self.tree.heading("#" + str(n + 1), text=lists[n])
                self.tree.column("" + lists[n], width=100)
                n = n + 1
            return self.tree

        def serch1(self):
            k = self.sid.get()

            if k != "":
                self.list4 = ("Employee ID", "First Name", "Last Name", "Department", "Pay", "Shift")
                self.trees = self.create_tree(self.f1, self.list4)
                self.trees.place(x=25, y=150)
                conn = sqlite3.connect('e.db')

                c = conn.execute("select * from item_info where ID=? OR ITEM=? OR COMPANY=? OR AMOUNT=?",
                                 (k.capitalize(), k.capitalize(), k.capitalize(), k.capitalize(),))
                a = c.fetchall()
                if len(a) != 0:
                    for row in a:
                        self.trees.insert("", END, values=row)
                    conn.commit()
                    conn.close()
                    self.trees.bind('<<TreeviewSelect>>')
                    self.variable = StringVar(self.f1)
                    self.variable.set("Select Action:")

                    self.cm = ttk.Combobox(self.f1, textvariable=self.variable, state='readonly',
                                           font='Papyrus 15 bold', height=50, width=15, )
                    self.cm.config(values=('Add Copies', 'Delete Copies', 'Remove Employee'))

                    self.cm.place(x=50, y=100)
                    self.cm.pack_propagate(0)

                    self.cm.bind("<<ComboboxSelected>>", self.combo)
                    self.cm.selection_clear()
                else:
                    messagebox.showinfo("Error", "Data not found")



            else:
                messagebox.showinfo("Error", "Search field cannot be empty.")

        def combo(self, event):
            self.var_Selected = self.cm.current()
            # l7=Label(self.f1,text='copies to update: ',font='Papyrus 10 bold',bd=1).place(x=250,y=700)
            if self.var_Selected == 0:
                self.copies(self.var_Selected)
            elif self.var_Selected == 1:
                self.copies(self.var_Selected)
            elif self.var_Selected == 2:
                self.deleteitem()

        # delete methode

        def deleteitem(self):
            try:
                self.curItem = self.trees.focus()

                self.c1 = self.trees.item(self.curItem, "values")[0]
                b1 = Button(self.f1, text='Update', font='Papyrus 10 bold', width=9, bd=3, command=self.delete2).place(
                    x=500, y=97)

            except:
                messagebox.showinfo("Empty", "Please select something.")

        def delete2(self):
            conn = sqlite3.connect('e.db')
            cd = conn.execute("select * from item_issued where Employee_ID=?", (self.c1,))
            ab = cd.fetchall()
            if ab != 0:
                conn.execute("DELETE FROM item_info where ID=?", (self.c1,));
                conn.commit()
                messagebox.showinfo("Successful", "Item Deleted sucessfully.")
                self.trees.delete(self.curItem)
            else:
                messagebox.showinfo("Error", "Item is Issued.\nItem cannot be deleted.")
            conn.commit()
            conn.close()

        # copie methode

        def copies(self, varr):
            try:
                curItem = self.trees.focus()
                self.c1 = self.trees.item(curItem, "values")[0]
                self.c2 = self.trees.item(curItem, "values")[4]
                self.scop = IntVar()
                self.e5 = Entry(self.f1, width=20, textvariable=self.scop)
                self.e5.place(x=310, y=100)
                if varr == 0:
                    b5 = Button(self.f1, text='Update', font='Papyrus 10 bold', bg='orange', fg='black', width=9, bd=3,
                                command=self.copiesadd).place(x=500, y=97)
                if varr == 1:
                    b6 = Button(self.f1, text='Update', font='Papyrus 10 bold', bg='orange', fg='black', width=9, bd=3,
                                command=self.copiesdelete).place(x=500, y=97)
            except:
                messagebox.showinfo("Empty", "Please select something.")

        def copiesadd(self):
            no = self.e5.get()
            if int(no) >= 0:

                conn = sqlite3.connect('e.db')

                conn.execute("update item_info set COPIES=COPIES+? where ID=?", (no, self.c1,))
                conn.commit()

                messagebox.showinfo("Updated", "Copies added sucessfully.")
                self.serch1()
                conn.close()

            else:
                messagebox.showinfo("Error", "No. of copies cannot be negative.")

        def copiesdelete(self):
            no1 = self.e5.get()
            if int(no1) >= 0:
                if int(no1) <= int(self.c2):
                    conn = sqlite3.connect('e.db')

                    conn.execute("update item_info set COPIES=COPIES-? where ID=?", (no1, self.c1,))
                    conn.commit()
                    conn.close()

                    messagebox.showinfo("Updated", "Deleted sucessfully")
                    self.serch1()

                else:
                    messagebox.showinfo("Maximum", "No. of copies to delete exceed available copies.")
            else:
                messagebox.showinfo("Error", "No. of copies cannot be negative.")

        def all(self):
            self.f1 = Frame(self.a, height=500, width=650, bg='black')
            self.f1.place(x=500, y=100)
            b1 = Button(self.f1, text='Back', bg='orange', fg='black', width=10, bd=3, command=self.rm).place(x=250,
                                                                                                              y=400)
            conn = sqlite3.connect('e.db')
            self.list3 = ("ITEM ID", "ITEM", "COMPANY", "AMOUNT", "COPIES", "LOCATION")
            self.treess = self.create_tree(self.f1, self.list3)
            self.treess.place(x=25, y=50)
            c = conn.execute("select * from item_info")
            g = c.fetchall()
            if len(g) != 0:
                for row in g:
                    self.treess.insert('', END, values=row)
            conn.commit()
            conn.close()


    # ===================START=======================
    def canvases(images, w, h):
        photo = Image.open(images)
        photo1 = photo.resize((w, h), Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(photo1)

        # photo2 = ImageTk.PhotoImage(Image.open(images).resize((w, h)),Image.ANTIALIAS)
        canvas = Canvas(root, width='%d' % w, height='%d' % h)
        canvas.grid(row=0, column=0)
        canvas.grid_propagate(0)
        canvas.create_image(0, 0, anchor=NW, image=photo2)
        canvas.image = photo2
        return canvas

    root = Toplevel()
    root.title("LOGIN")
    """width = 400
    height = 280
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)"""

    # root.state('zoomed')
    # root.resizable(0, 0)
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    canvas = canvases(image3, w, h)

    # photo=PhotoImage(file=images)

    # ==============================METHODS========================================
    def Database():
        global conn, cursor
        conn = sqlite3.connect("python1.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `login` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
        cursor.execute("SELECT * FROM `login` WHERE `username` = 'admin' AND `password` = 'admin'")
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO `login` (username, password) VALUES('eadmin', 'eadmin')")
            conn.commit()

    def Login(event=None):
        Database()

        if USERNAME.get() == "" or PASSWORD.get() == "":
            messagebox.showinfo("Error", "Please complete the required field!")
            lbl_text.config(text="Please complete the required field!", fg="red")
        else:
            cursor.execute("SELECT * FROM `login` WHERE `username` = ? AND `password` = ?",
                           (USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
                # HomeWindow()
                # Top.destroy()
                root.destroy()

                a = libmenu()

            else:
                messagebox.showinfo("Error", "Invalid username or password.")
                # lbl_text.config(text="Invalid username or password", fg="red")
                USERNAME.set("")
                PASSWORD.set("")
        cursor.close()
        conn.close()

    # ==============================VARIABLES======================================
    USERNAME = StringVar()
    PASSWORD = StringVar()

    # ==============================FRAMES=========================================
    '''Top = Frame(root, bd=2,  relief=RIDGE)
    Top.pack(side=TOP, fill=X)
    Form = Frame(root, height=200)
    Form.pack(side=BOTTOM, pady=20)'''
    # ==============================LABELS=========================================
    lbl_title = Label(canvas, text="ADMIN   LOGIN", font=('Papyrus', 30, 'bold',), bg='black', fg='orange')
    lbl_title.place(x=500, y=100)
    lbl_username = Label(canvas, text="Username:", font=('Papyrus', 15, 'bold'), bd=4, bg='black', fg='orange')
    lbl_username.place(x=500, y=230)
    lbl_password = Label(canvas, text="Password :", font=('Papyrus', 15, 'bold'), bd=3, bg='black', fg='orange')
    lbl_password.place(x=500, y=330)
    lbl_text = Label(canvas)
    lbl_text.place(x=450, y=500)
    lbl_text.grid_propagate(0)

    # ==============================ENTRY WIDGETS==================================
    username = Entry(canvas, textvariable=USERNAME, font=(14), bg='black', fg='orange', bd=6)
    username.place(x=650, y=230, )
    password = Entry(canvas, textvariable=PASSWORD, show="*", font=(14), bg='black', fg='orange', bd=6)
    password.place(x=650, y=330)

    # ==============================BUTTON WIDGETS=================================
    btn_login = Button(canvas, text="LOGIN", font=('Papyrus 15 bold'), width=25, command=Login, bg='black', fg='orange')
    btn_login.place(x=500, y=400)
    btn_login.bind('<Return>', Login)
    root.mainloop()
