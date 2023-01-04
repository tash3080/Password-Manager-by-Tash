from tkinter import *
from tkinter import ttk
import random
import string
import database

database.create_table()

class Interface:
    def __init__(self, root) -> None:
        self.root = root
        self.pw_len = StringVar()
        self.password = StringVar()
        self.website = StringVar()
        self.username = StringVar()
        self.email = StringVar()
        self.passwd = str()

        self.frame1 = Frame(self.root)
        self.frame1.grid()

        self.frame2 = Frame(self.frame1, width= 15)

        label1_pw = Label(self.frame1, text="Password", width= 15)
        label2_uid = Label(self.frame1, text="Username")
        label3_em = Label(self.frame1, text="Email")
        label4_site = Label(self.frame1, text="Site")

        label5_pl = Label(self.frame2, text= "PW Length")

        entry1_pw = Entry(self.frame1, width= 20, textvariable=self.password)
        entry2_uid = Entry(self.frame1, textvariable=self.username)
        entry3_em = Entry(self.frame1, textvariable= self.email)
        entry4_site = Entry(self.frame1, textvariable=self.website)

        entry5_pl = Entry(self.frame2, width=5, textvariable=self.pw_len)

        button1_gen = Button(self.frame1, text="Generate", width=10, command=self.generate)
        button2_save = Button(self.frame1, text="Save", width=10, command=self.save)
        button3_search = Button(self.frame1, text="Search", width=10, command=self.search)
        button4_show = Button(self.frame1, text="Show all", width=10, command=self.show_all)
        button5_update = Button(self.frame1, text="Update", width=10, command=self.update)
        button6_del = Button(self.frame1, text="Delete", width=10, command=self.delete)

        label5_pl.grid(row=0, column=0)
        entry5_pl.grid(row=0, column=1)

        label1_pw.grid(row=0, column=0)
        entry1_pw.grid(row=0, column=1)
        self.frame2.grid(row=0, column=2)

        label2_uid.grid(row=1, column= 0)
        entry2_uid.grid(row=1, column= 1)
        button1_gen.grid(row=1, column= 2)

        label3_em.grid(row=2, column= 0)
        entry3_em.grid(row=2, column= 1)
        button2_save.grid(row=2, column= 2)

        label4_site.grid(row=3, column= 0)
        entry4_site.grid(row=3, column= 1)
        button3_search.grid(row=3, column= 2)

        button4_show.grid(row=4, column= 0)
        button5_update.grid(row=4, column= 1)
        button6_del.grid(row=4, column= 2)

        self.pw_data = ttk.Treeview(self.frame1)
        self.pw_data["columns"] = ("site", "email", "username", "password")
        self.pw_data.column("#0", width=0, stretch= NO)
        self.pw_data.column("site", width=20)
        self.pw_data.column("email", width=20)
        self.pw_data.column("username", width=20)
        self.pw_data.column("password", width=20)
        self.pw_data.heading("site", text="Site")
        self.pw_data.heading("email", text="Email")
        self.pw_data.heading("username", text="Username")
        self.pw_data.heading("password", text="Password")

        self.pw_data.grid(row=5, column=0, columnspan= 3, sticky= "nsew")

    def generate(self):
        all = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
        temp = random.sample(all,int(self.pw_len.get()))
        self.passwd = "".join(temp)
        self.password.set(self.passwd)

    def save(self):
        database.save(self.website.get(), self.username.get(), self.email.get(), self.password.get())
        self.pw_data.insert(parent='', text='', index='end', 
                    values=(self.website.get(), self.username.get(), self.email.get(), self.password.get()))

    def search(self):
        result = database.search(self.website.get())
        for row in result:
            self.pw_data.insert(parent="", text="", index='end', values=(row[0], row[1], row[2], row[3]))

    def show_all(self):
        data = database.show_all()
        for row in data:
            self.pw_data.insert(parent="", text="", index='end', values=(row[0], row[1], row[2], row[3]))

    def update(self):
        cred = database.update(self.password.get(), self.website.get(), self.email.get())
        for row in cred:
            self.pw_data.insert(parent="", text="", index='end', values=(row[0], row[1], row[2], row[3]))

    def delete(self):
        database.delete(self.website.get(), self.email.get(), self.password.get())

if __name__ == '__main__':
    app = Tk()
    app.title('Password Manager')
    app.configure(background= "#7acdfa")
    interface = Interface(app)
    app.mainloop()
    