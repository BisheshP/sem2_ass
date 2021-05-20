from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import random
import model.emp_login_model
import backend.dbconnection


class add_info:
    def __init__(self, root):
        self.root = root
        self.root.title("Create New Account")
        self.root.geometry("1397x800+100+50")
        self.root.resizable(0, 0)
        self.db = backend.dbconnection.DBconnect()

        #----- Variables -----
        # self.id = StringVar()
        self.fname = StringVar()
        self.lname = StringVar()
        self.address = StringVar()
        self.gender = StringVar()
        self.mobile = StringVar()
        self.username = StringVar()
        self.password = StringVar()

        #----- defining image -----
        self.bg_img = ImageTk.PhotoImage(file="13.jpg")

        my_canvas = Canvas(self.root, highlightthickness=0)
        my_canvas.pack(fill="both", expand=True)
        # ------ put image in canvas -------
        my_canvas.create_image(0, 0, image=self.bg_img, anchor=NW)

        main_frame = Frame(self.root, width=1201, height=740, bg="white")
        main_frame.place(x=98, y=30)
        frame_1 = Frame(main_frame, width=1337, height=150, bg="white")
        frame_1.place(x=0, y=0)
        frame_2 = Frame(main_frame, width=1217, height=440, bg="white", padx=20, pady=10)
        frame_2.place(x=60, y=150)
        frame_3 = Frame(main_frame, width=1337, height=120, bg="white")
        frame_3.place(x=0, y=620)

        # ------ frame_1 ------
        lbl_title = Label(frame_1, text="Sign Up", font=("arial", 30, "bold"), bg="white")
        lbl_title.place(y=45, x=450)
        lbl_subtitle = Label(frame_1, text="It's quick and easy.", font="arial 10", bg="white", fg="grey")
        lbl_subtitle.place(y=112, x=470)

        #------- frame_2 ------
        lbl_lname = Label(frame_2, text="Last name", bg="white", font=("arial unicode ms",15))
        lbl_lname.place(x=549, y=10)
        ent_lname = Entry(frame_2, textvariable=self.lname, width=40, bd=0, bg="#F9F8F8", font=("arial unicode ms", 13))
        ent_lname.place(x=549, y=50)
        lbl_fname = Label(frame_2, text="First name", bg="white", font=("arial unicode ms",15))
        lbl_fname.place(x=10, y=10)
        self.ent_fname = Entry(frame_2, textvariable=self.fname, width=40, bd=0, bg="#F9F8F8", font=("arial unicode ms", 13))
        self.ent_fname.place(x=10, y=50)
        #------ frame_2_row1 ---------
        lbl_add = Label(frame_2, text="Address", bg="white", font=("arial unicode ms",15))
        lbl_add.place(x=10, y=110)
        ent_add = Entry(frame_2, textvariable=self.address, width=40, bd=0, bg="#F9F8F8", font=("arial unicode ms", 13))
        ent_add.place(x=10, y=150)
        lbl_gender = Label(frame_2, text="Gender", bg="white", font=("arial unicode ms",15))
        lbl_gender.place(x=549, y=110)
        ent_gender = Entry(frame_2, textvariable=self.gender, width=40, bd=0, bg="#F9F8F8", font=("arial unicode ms", 13))
        ent_gender.place(x=549, y=150)
        #------ frame_2_row2 ---------
        lbl_ph = Label(frame_2, text="Mobile No.", bg="white", font=("arial unicode ms",15))
        lbl_ph.place(x=10, y=210)
        ent_ph = Entry(frame_2, textvariable=self.mobile, width=40, bd=0, bg="#F9F8F8", font=("arial unicode ms", 13))
        ent_ph.place(x=10, y=250)
        # lbl_cost = Label(frame_2, text="---", bg="white", font=("arial unicode ms",15))
        # lbl_cost.place(x=549, y=210)
        # ent_cost = Entry(frame_2, width=40, bd=0, bg="#F9F8F8", font=("arial unicode ms", 13))
        # ent_cost.place(x=549, y=250)
        # ------ frame_2_row3 ---------
        lbl_uname = Label(frame_2, text="Username", bg="white", font=("arial unicode ms",15))
        lbl_uname.place(x=10, y=310)
        ent_uname = Entry(frame_2, textvariable=self.username, width=40, bd=0, bg="#F9F8F8", font=("arial unicode ms", 13))
        ent_uname.place(x=10, y=350)
        lbl_pass = Label(frame_2, text="Password", bg="white", font=("arial unicode ms",15))
        lbl_pass.place(x=549, y=310)
        ent_pass = Entry(frame_2, textvariable=self.password, width=40, bd=0, bg="#F9F8F8", font=("arial unicode ms", 13))
        ent_pass.place(x=549, y=350)

        # ------- frame_3 ------
        btn_add = Button(frame_3, text="ADD", width=15, height=2, bg="red", fg="white", command=self.add)
        btn_add.place(x=415, y=0)
        btn_clear = Button(frame_3, text="CLEAR", width=15, height=2, bg="red", fg="white", command=self.clear)
        btn_clear.place(x=620, y=0)

    #-------- Functions --------
    def clear(self):
        # self.id.set("")
        self.fname.set("")
        self.lname.set("")
        self.address.set("")
        self.gender.set("")
        self.mobile.set("")
        self.username.set("")
        self.password.set("")
        self.ent_fname.focus_set()


    def add(self):

        # try:
            # id = self.id.get()
            fname = self.fname.get()
            lname = self.lname.get()
            address = self.address.get()
            gender = self.gender.get()
            mobile = self.mobile.get()
            username = self.username.get()
            password = self.password.get()
            if fname == "" or lname == "" or address == "" or gender == "" or mobile == "" or username =="" or password=="":
                messagebox.showerror("Error", "Please fill in all the required details.")
            else:
                u = model.emp_login_model.Emp_info( fname, lname, address, gender, mobile, username, password)
                query = "insert into accounts(first_name, last_name, address, gender, mobile, username, password) values (%s,%s,%s,%s,%s,%s,%s)"
                values = (u.get_fname(), u.get_lname(),u.get_address(),u.get_gender(),u.get_mobile(),u.get_username(),u.get_password())
                self.db.insert(query, values)
                messagebox.showinfo("Inventory", "Record inserted successfully!")
                self.root.destroy()


        # except:
        #     messagebox.showerror("Error", "Repitition of ID, Please Try Again.")


#
# win = Tk()
# obj = add_info(win)
# win.mainloop()