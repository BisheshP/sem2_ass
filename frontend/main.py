from tkinter import *
from PIL import Image, ImageTk
import emp_login

class main:
    def __init__(self, root):
        self.root = root
        self.root.title("B&B Supermarket")
        self.root.geometry("1397x800+50+50")
        self.root.resizable(0, 0)

        self.bg_img = ImageTk.PhotoImage(file="6.jpg")
        self.btn1 = ImageTk.PhotoImage(file="9.jpg")
        self.btn2 = ImageTk.PhotoImage(file="11.jpg")

        my_canvas = Canvas(self.root, highlightthickness=0)
        my_canvas.pack(fill="both", expand=True)
        # put image and text in my_canvas
        my_canvas.create_image(0, 0, image=self.bg_img, anchor=NW)
        my_canvas.create_text(700, 240, text="Login As", font=("arial rounded mt bold", 50), fill="white")

        btn_1 = Button(my_canvas, image=self.btn1, width=140, height=140, bd=0, command=self.emp_logg)
        btn_1.place(x=630, y=360)


    def emp_logg(self):
        self.root.destroy()
        tk = Tk()
        emp_login.emp_log(tk)
        tk.mainloop()


root = Tk()
obj = main(root)
root.mainloop()