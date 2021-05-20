from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import model.inventory_model
import backend.dbconnection
class Functions:
    def mergesort(self, alist):
        if len(alist) > 1:
            mid = len(alist) // 2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]
            self.mergesort(lefthalf)
            self.mergesort(righthalf)
            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    alist[k] = lefthalf[i]
                    i = i + 1

                else:
                    alist[k] = righthalf[j]
                    j += 1
                k += 1
            while i < len(lefthalf):
                alist[k] = lefthalf[i]
                i += 1
                k += 1
            while j < len(righthalf):
                alist[k] = righthalf[j]
                j += 1
                k += 1
        return alist
    def binary_primary(self, list, item):
        if list == []:
            return ValueError
        self.list = list
        self.item = item
        max = len(list) - 1
        min = 0
        while min <= max:
            mid = (min + max) // 2
            if self.list[mid] == self.item:
                return mid
            elif self.list[mid] > self.item:
                max = mid - 1
            else:
                min = mid + 1
        return -1


class Inventory(Functions):
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory")
        self.root.geometry("1397x800+50+50")
        bg_color = "white"
        self.db = backend.dbconnection.DBconnect()

        self.bg_img = ImageTk.PhotoImage(file="13.jpg")
        my_canvas = Canvas(self.root, highlightthickness=0)
        my_canvas.pack(fill="both", expand=True)
        # put image and text in my_canvas
        my_canvas.create_image(0, 0, image=self.bg_img, anchor=NW)

        #----- Variables -----
        self.id_var = StringVar()
        self.name_var = StringVar()
        self.category_var = StringVar()
        self.qty_var = StringVar()
        self.mrp_var = StringVar()
        self.cost_var = StringVar()
        self.ph_var = StringVar()
        self.search_by_var = StringVar()
        self.search_txt_var = StringVar()
        self.sort_by_var = StringVar()

        #----- main_frame -----
        main_frame = Frame(self.root, width=1337, height=740, bg="white")
        main_frame.place(x=30, y=30)
        lbl_heading = Label(main_frame, text="Inventory Management", font=("arial unicode ms bold",30, "bold"), bg=bg_color )
        lbl_heading.place(relwidth=1, y=25)

        #----- manage_frame -----
        manage_frame = LabelFrame(main_frame, text="Menu", bg=bg_color, bd=2, font=("arial unicode ms", 12))
        manage_frame.place(x=20, y=120, width=400, height=603)

        m_title = Label(manage_frame, text="Manage Product", bg=bg_color, font=("arial unicode ms", 20, "bold"))
        m_title.place(relwidth=1, y=5)

        lbl_id = Label(manage_frame, text="Product ID :", font=("arial unicode ms", 12), bg=bg_color)
        lbl_id.place(x=5, y=70)
        self.ent_id = Entry(manage_frame, textvariable=self.id_var, font=("arial unicode ms", 13),relief=FLAT, bd=0, bg="#F9F8F8")
        self.ent_id.place(x=120, y=70, width=270)

        lbl_name = Label(manage_frame, text="Name\t  :", font=("arial unicode ms", 12), bg=bg_color)
        lbl_name.place(x=5, y=115)
        ent_name = Entry(manage_frame, textvariable=self.name_var, font=("arial unicode ms", 13), relief=FLAT, bd=0,
                         bg="#F9F8F8")
        ent_name.place(x=120, y=115, width=270)

        lbl_category = Label(manage_frame, text="Category\t  :", font=("arial unicode ms", 12), bg=bg_color)
        lbl_category.place(x=5, y=160)
        combo_category = ttk.Combobox(manage_frame, textvariable=self.category_var, font=("arial unicode ms", 12), state="readonly")
        combo_category ['values'] = ('Fridge', 'Pantry', 'Basket')
        combo_category.place(x=120, y=160, width=270)

        lbl_qty = Label(manage_frame, text="In Stock\t  :", font=("arial unicode ms", 12), bg=bg_color)
        lbl_qty.place(x=5, y=205)
        ent_qty = Entry(manage_frame, textvariable=self.qty_var, font=("arial unicode ms", 13), relief=FLAT, bd=0, bg="#F9F8F8")
        ent_qty.place(x=120, y=205, width=270)

        lbl_mrp = Label(manage_frame, text="MRP\t  :", font=("arial unicode ms", 12), bg=bg_color)
        lbl_mrp.place(x=5, y=250)
        ent_mrp = Entry(manage_frame, textvariable=self.mrp_var, font=("arial unicode ms", 13), relief=FLAT, bd=0, bg="#F9F8F8")
        ent_mrp.place(x=120, y=250, width=270)

        lbl_cost = Label(manage_frame, text="Cost Price :", font=("arial unicode ms", 12), bg=bg_color)
        lbl_cost.place(x=5, y=295)
        ent_cost = Entry(manage_frame, textvariable=self.cost_var, font=("arial unicode ms", 13), relief=FLAT, bd=0, bg="#F9F8F8")
        ent_cost.place(x=120, y=295, width=270)

        lbl_ph = Label(manage_frame, text="Vendor No :", font=("arial unicode ms", 12), bg=bg_color)
        lbl_ph.place(x=5, y=340)
        ent_ph = Entry(manage_frame, textvariable=self.ph_var, font=("arial unicode ms", 13), relief=FLAT, bd=0, bg="#F9F8F8")
        ent_ph.place(x=120, y=340, width=270)

        #---------- btn_frame ----------
        btn_frame = Frame(manage_frame, relief=RIDGE, bg=bg_color)
        btn_frame.place(x=0, y=390, width=395, height=65)

        btn_add = Button(btn_frame, command=self.add_students, text="Add", font=("arial unicode ms",13), width=6, height=1, bg="red", fg="white", activebackground="red")
        btn_add.grid(row=0, column=0, padx=6, pady=5)
        btn_update = Button(btn_frame, command=self.update, text="Update", font=("arial unicode ms",13), width=6, height=1, bg="red", fg="white", activebackground="red")
        btn_update.grid(row=0, column=1, padx=3, pady=5)
        btn_delete = Button(btn_frame, command=self.delete, text="Delete", font=("arial unicode ms",13), width=6, height=1, bg="red", fg="white", activebackground="red")
        btn_delete.grid(row=0, column=2, padx=6, pady=5)
        btn_clear = Button(btn_frame, command=self.clear, text="Clear", font=("arial unicode ms",13), width=6, height=1, bg="red", fg="white", activebackground="red")
        btn_clear.grid(row=0, column=3, padx=3, pady=5)

        #---------- Sorting ----------
        lbl_sort = Label(manage_frame, text="Sort By: ", font=("arial unicode ms",13), bg=bg_color)
        lbl_sort.place(x=5, y=460)

        self.combo_sort = ttk.Combobox(manage_frame, font=("arial unicode ms", 12), textvariable=self.sort_by_var, state="readonly")
        self.combo_sort['values'] = ('Product ID','Name','Category', 'In Stock', 'MRP', 'Cost', 'Vendor No.')
        self.combo_sort.place(x=100, y=460, width=270)
        self.combo_sort.current(0)

        btn_sort = Button(manage_frame, command=self.sorting, text = "Sort", font=("arial unicode ms", 13), width=10, height=1, bg="red", fg="white", activebackground="red")
        btn_sort.place(x=120, y=510)

        # ---------- Search ----------
        lbl_search = Label(main_frame, text="Search By: ", font=("arial unicode ms", 15), bg=bg_color)
        lbl_search.place(x=440, y=140)

        lbl2_search = Label(main_frame, text="Product ID", font=("arial unicode ms", 15), bg=bg_color)
        lbl2_search.place(x=580, y=140)

        # lbl2_search = ttk.Combobox(main_frame, textvariable=self.search_by_var, font=("arial unicode ms", 12), width=15, state="readonly")
        # lbl2_search['values'] = ('Product ID')
        # combo_search.place(x=580, y=142)
        # combo_search.current(0)
        ent_search = Entry(main_frame, textvariable=self.search_txt_var, font=("arial unicode ms", 13), width=20, relief=FLAT, bg="#F9F8F8")
        ent_search.place(x=820, y=142)

        btn_search = Button(main_frame, command=self.search, text="Search", font=("arial unicode ms", 12), height=1, width=8, bg="red", fg=bg_color, activebackground="red")
        btn_search.place(x=1090, y=136)
        btn_showall = Button(main_frame, command=self.fetch_data, text="Show All", font=("arial unicode ms", 12), height=1, width=8, bg="red", fg=bg_color, activebackground="red")
        btn_showall.place(x=1205, y=136)


        #----- Table_Frame -----
        table_frame = Frame(main_frame, highlightbackground="grey", highlightthickness=1, bg="white")
        table_frame.place(x=430, y=190, width=900, height=532)
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,column=("roll", "name", "email", "gender", "contact", "dob", "address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("roll", text="Product ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("email", text="Category")
        self.student_table.heading("gender", text="In Stock")
        self.student_table.heading("contact", text="MRP")
        self.student_table.heading("dob", text="Cost Price")
        self.student_table.heading("address", text="Vendor No.")

        self.student_table['show'] = 'headings'
        self.student_table.column("roll", width=80)
        self.student_table.column("name", width=180)
        self.student_table.column("email", width=180)
        self.student_table.column("gender", width=80)
        self.student_table.column("contact", width=100)
        self.student_table.column("dob", width=150)
        self.student_table.column("address", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.fetch_data()
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)

    def add_students(self):
        try:
            id = self.id_var.get()
            name = self.name_var.get()
            category = self.category_var.get()
            qty = self.qty_var.get()
            mrp = self.mrp_var.get()
            cost = self.cost_var.get()
            ph = self.ph_var.get()
            if id=="" or name=="" or category=="" or qty=="" or mrp=="" or cost=="" or ph=="":
                messagebox.showerror("Error", "All fields are required to fill.")
            else:
                u = model.inventory_model.Inventory_m(id, name, category, qty, mrp, cost, ph)
                query = "insert into inventoryyy values (%s,%s,%s,%s,%s,%s,%s)"
                values = (u.get_id(), u.get_name(), u.get_category(), u.get_qty(), u.get_mrp(), u.get_cost(), u.get_ph())
                self.db.insert(query, values)
                self.clear()
                self.fetch_data()
                messagebox.showinfo("Success", "Record inserted successfully!")
        except:
            messagebox.showerror("Error", "The product id you entered is not an integer value OR it is already in use. Please select a different one and try again.")

    def fetch_data(self):
        self.combo_sort.current(0)
        db = backend.dbconnection.DBconnect()
        query = "select * from inventoryyy"
        rows = db.select(query)
        if len(rows)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)

    def clear(self):
        self.id_var.set("")
        self.name_var.set("")
        self.category_var.set("")
        self.qty_var.set("")
        self.mrp_var.set("")
        self.cost_var.set("")
        self.ph_var.set("")
        self.ent_id.focus()
        self.ent_id['state'] = "normal"

    def get_cursor(self, ev):
        # self.ent_id['state'] = "readonly"
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.id_var.set(row[0])
        self.name_var.set(row[1])
        self.category_var.set(row[2])
        self.qty_var.set(row[3])
        self.mrp_var.set(row[4])
        self.cost_var.set(row[5])
        self.ph_var.set(row[6])

    def update(self):
        db = backend.dbconnection.DBconnect()
        id = self.id_var.get()
        name = self.name_var.get()
        category = self.category_var.get()
        qty = self.qty_var.get()
        mrp = self.mrp_var.get()
        cost = self.cost_var.get()
        ph = self.ph_var.get()
        if id=="" or name=="" or category=="" or qty=="" or mrp=="" or cost=="" or ph=="":
            messagebox.showerror("Error", "All fields are required to fill.")
        else:
            u = model.inventory_model.Inventory_m(id, name, category, qty, mrp, cost, ph)
            query = "update inventoryyy set name=%s,category=%s,quantity=%s,mrp=%s,cost_price=%s,vendor_no=%s where id=%s"
            values = (u.get_name(), u.get_category(), u.get_qty(), u.get_mrp(), u.get_cost(), u.get_ph(), u.get_id())
            db.update(query, values)
            self.fetch_data()
            self.clear()
            messagebox.showinfo("Success", "Record updated successfully!")

    def delete(self):
        id = self.id_var.get()
        db = backend.dbconnection.DBconnect()
        query = "delete from inventoryyy where id=%s"
        value = (id, )
        db.delete(query, value)
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Success", "Record deleted successfully!")

    def sorting(self):
        db = backend.dbconnection.DBconnect()
        query = "select * from inventoryyy"
        rows = db.select(query)
        myStack = []
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            if self.sort_by_var.get()=="Product ID":
                for row in rows:
                    myStack.append(row[0])
                self.sorted = self.mergesort(myStack)
                print(self.sorted)
                print(rows)
                for i in self.sorted:
                    for row in rows:
                        if i == row[0]:
                            self.student_table.insert('', END, value=row)
            elif self.sort_by_var.get()=="Name":
                for row in rows:
                    myStack.append(row[1])
                self.sorted = self.mergesort(myStack)
                print(self.sorted)
                for i in self.sorted:
                    for row in rows:
                        if i == row[1]:
                            self.student_table.insert('', END, value=row)
                            rows.remove(row)
            elif self.sort_by_var.get()=="Category":
                for row in rows:
                    myStack.append(row[2])
                self.sorted = self.mergesort(myStack)
                print(self.sorted)
                for i in self.sorted:
                    for row in rows:
                        if i == row[2]:
                            self.student_table.insert('', END, value=row)
                            rows.remove(row)
            elif self.sort_by_var.get()=="In Stock":
                for row in rows:
                    myStack.append(row[3])
                self.sorted = self.mergesort(myStack)
                print(self.sorted)
                for i in self.sorted:
                    for row in rows:
                        if i == row[3]:
                            self.student_table.insert('', END, value=row)
                            rows.remove(row)
            elif self.sort_by_var.get()=="MRP":
                for row in rows:
                    myStack.append(row[4])
                self.sorted = self.mergesort(myStack)
                print(self.sorted)
                for i in self.sorted:
                    for row in rows:
                        if i == row[4]:
                            self.student_table.insert('', END, value=row)
                            rows.remove(row)
            elif self.sort_by_var.get()=="Cost":
                for row in rows:
                    myStack.append(row[5])
                self.sorted = self.mergesort(myStack)
                print(self.sorted)
                for i in self.sorted:
                    for row in rows:
                        if i == row[5]:
                            self.student_table.insert('', END, value=row)
                            rows.remove(row)
            elif self.sort_by_var.get()=="Vendor No.":
                for row in rows:
                    myStack.append(row[6])
                self.sorted = self.mergesort(myStack)
                print(self.sorted)
                for i in self.sorted:
                    for row in rows:
                        if i == row[6]:
                            self.student_table.insert('', END, value=row)
                            rows.remove(row)






    # def sort_by_id(self):
    #     db = backend.dbconnection.DBconnect()
    #     query = "select * from inventoryyy"
    #     rows = db.select(query)
    #     myStack = []
    #     if len(rows) != 0:
    #         self.student_table.delete(*self.student_table.get_children())
    #         for row in rows:
    #             myStack.append(row[0])
    #         self.sorted = self.mergesort(myStack)
    #         print(self.sorted)
    #         print(rows)
    #         for i in self.sorted:
    #             for row in rows:
    #                 if i == row[0]:
    #                     self.student_table.insert('', END, value=row)


    def search(self):
        db = backend.dbconnection.DBconnect()
        query = "select * from inventoryyy"
        rows = db.select(query)
        myStack = []
        # if len(rows) != 0:
        #     self.student_table.delete(*self.student_table.get_children())
        for row in rows:
            myStack.append(row[0])
        self.sorted = self.mergesort(myStack)
        item = int(self.search_txt_var.get())
        sorted = self.sorted
        index = self.binary_primary(sorted, item)
        for row in rows:
            if sorted[index] == row[0]:
                self.student_table.delete(*self.student_table.get_children())
                self.student_table.insert('', END, value=row)














#
#
# win = Tk()
# obj = Inventory(win)
# win.mainloop()