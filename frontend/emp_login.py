from tkinter import *
from PIL import ImageTk
import add_account
from tkinter import messagebox
import backend.dbconnection
import inventory



class emp_log:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1397x800+50+50")
        self.root.title('Login Page')
        self.root.resizable(0,0)
        bg_color = "white"

        #----- Variables -----
        self.username_var = StringVar()
        self.pass_var = StringVar()


        #---------- define image ----------
        self.bg_img = ImageTk.PhotoImage(file="13.jpg")
        self.user_icon = PhotoImage(file="16.png")
        self.pass_icon = PhotoImage(file="21.png")
        self.login_icon = PhotoImage(file="23.png")
        self.login_icon2 = PhotoImage(file="27.png")

        my_canvas = Canvas(self.root, highlightthickness=0)
        my_canvas.pack(fill="both", expand=True)
        #------ put image in canvas -------
        my_canvas.create_image(0, 0, image=self.bg_img, anchor=NW)
        #============ Login Frame ============
        main_frame = Frame(self.root, width=600, height=730, bg=bg_color)
        main_frame.place(x=400, y=30)

        lbl_header = Label(main_frame, text="Login", font=("arial rounded mt bold",30, "bold"), bg=bg_color)
        lbl_header.place(x=220, y=50)

        lbl_username = Label(main_frame, text="Username", font=("arial unicode ms",15), bg=bg_color)
        lbl_username.place(x=50, y=175)
        lbl_user_icon = Label(main_frame, height=30, width=30, image=self.user_icon, bg=bg_color)
        lbl_user_icon.place(x=50, y=220)
        ent_username = Entry(main_frame, textvariable=self.username_var, font=("arial unicode ms", 15), width=31, bd=0, bg="#F9F8F8")
        ent_username.place(x=100, y=220)

        lbl_pass = Label(main_frame, text="Password", font=("arial unicode ms", 15), bg=bg_color)
        lbl_pass.place(x=50, y=280)
        lbl_pass_icon = Label(main_frame, height=35, width=30, image=self.pass_icon, bg=bg_color)
        lbl_pass_icon.place(x=49, y=321)
        ent_pass = Entry(main_frame, textvariable=self.pass_var, font=("arial unicode ms", 15), width=31, bd=0, bg="#F9F8F8")
        ent_pass.place(x=100, y=325)

        self.login_btn = Button(main_frame, command=lambda:self.on_login(self.username_var.get(), self.pass_var.get()), image=self.login_icon, bg=bg_color, bd=0)
        self.login_btn.place(x=90, y=500)

        self.login_btn.bind('<Enter>', self.on_touch)
        self.login_btn.bind('<Leave>', self.on_leave)

        btn_create = Button(main_frame, command=self.on_create, text="Create New Account", bg="#011C38", font=("arial unicode ms", 20, "bold"), fg="white", relief=FLAT, activeforeground="red", activebackground="#011C38")
        btn_create.place(x=130, y=600)


    def on_touch(self,e):
        self.login_btn['image'] = self.login_icon2
    def on_leave(self, e):
        self.login_btn['image'] = self.login_icon

    def on_create(self):
        tk = Toplevel()
        add_account.add_info(tk)
        tk.grab_set()

    def on_login(self, username, password):
            db=backend.dbconnection.DBconnect()
            query = "select Username,Password from accounts"
            rows=db.select(query)
            login = None
            for (uname, pas) in rows:
                if username == uname and password == pas:
                    login = True
                    break
                else:
                    login = False
            if  login == True:
                messagebox.showinfo("Login Success","Logged in successfully")
                self.on_loginsuccess()
            elif login == False:
                messagebox.showerror("Error", "Incorrect email or password!")

    def on_loginsuccess(self):
        self.root.destroy()
        tk = Tk()
        obj = inventory.Inventory(tk)
        tk.mainloop()










# root = Tk()
# emp_log(root)
# root.mainloop()

