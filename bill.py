from tkinter import *
import random
import os
from tkinter import messagebox

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#badc57"

        title = Label(self.root, text="Billing Software",
                      font=('times new roman', 30, 'bold'),
                      pady=2, bd=12, bg=bg_color, fg="Black", relief=GROOVE)
        title.pack(fill=X)

        # ================= Variables =================
        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.hand_gloves = IntVar()
        self.dettol = IntVar()
        self.newsprin = IntVar()
        self.thermal_gun = IntVar()

        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.daal = IntVar()
        self.flour = IntVar()
        self.maggi = IntVar()

        self.sprite = IntVar()
        self.limka = IntVar()
        self.mazza = IntVar()
        self.coke = IntVar()
        self.fanta = IntVar()
        self.mountain_duo = IntVar()

        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()

        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()

        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        self.search_bill = StringVar()
        self.bill_no.set(str(random.randint(1000, 9999)))

        # ================= Customer Frame =================
        F1 = LabelFrame(self.root, text="Customer Details",
                        font=('times new roman', 15, 'bold'),
                        bd=10, fg="Black", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        Label(F1, text="Customer Name", bg=bg_color,
              font=('times new roman', 15, 'bold')).grid(row=0, column=0, padx=20)
        Entry(F1, textvariable=self.c_name, width=15,
              font='arial 15', bd=7).grid(row=0, column=1)

        Label(F1, text="Phone No", bg=bg_color,
              font=('times new roman', 15, 'bold')).grid(row=0, column=2, padx=20)
        Entry(F1, textvariable=self.c_phone, width=15,
              font='arial 15', bd=7).grid(row=0, column=3)

        Label(F1, text="Bill No", bg=bg_color,
              font=('times new roman', 15, 'bold')).grid(row=0, column=4, padx=20)
        Entry(F1, textvariable=self.search_bill, width=15,
              font='arial 15', bd=7).grid(row=0, column=5)

        Button(F1, text="Search", command=self.find_bill,
               width=10, font='arial 12 bold').grid(row=0, column=6, padx=10)

        # ================= Medical =================
        F2 = LabelFrame(self.root, text="Medical",
                        font=('times new roman', 15, 'bold'),
                        bd=10, bg=bg_color)
        F2.place(x=5, y=180, width=325, height=380)

        med_items = [
            ("Sanitizer", self.sanitizer),
            ("Mask", self.mask),
            ("Hand Gloves", self.hand_gloves),
            ("Dettol", self.dettol),
            ("Newsprint", self.newsprin),
            ("Thermal Gun", self.thermal_gun)
        ]

        for i, (name, var) in enumerate(med_items):
            Label(F2, text=name, bg=bg_color,
                  font=('times new roman', 16, 'bold')).grid(row=i, column=0, sticky='W')
            Entry(F2, textvariable=var, width=10,
                  font=('times new roman', 16), bd=5).grid(row=i, column=1)

        # ================= Grocery =================
        F3 = LabelFrame(self.root, text="Grocery",
                        font=('times new roman', 15, 'bold'),
                        bd=10, bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        grocery_items = [
            ("Rice", self.rice),
            ("Food Oil", self.food_oil),
            ("Wheat", self.wheat),
            ("Daal", self.daal),
            ("Flour", self.flour),
            ("Maggi", self.maggi)
        ]

        for i, (name, var) in enumerate(grocery_items):
            Label(F3, text=name, bg=bg_color,
                  font=('times new roman', 16, 'bold')).grid(row=i, column=0, sticky='W')
            Entry(F3, textvariable=var, width=10,
                  font=('times new roman', 16), bd=5).grid(row=i, column=1)

        # ================= Cold Drinks =================
        F4 = LabelFrame(self.root, text="Cold Drinks",
                        font=('times new roman', 15, 'bold'),
                        bd=10, bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)

        cold_items = [
            ("Sprite", self.sprite),
            ("Limka", self.limka),
            ("Mazza", self.mazza),
            ("Coke", self.coke),
            ("Fanta", self.fanta),
            ("Mountain Dew", self.mountain_duo)
        ]

        for i, (name, var) in enumerate(cold_items):
            Label(F4, text=name, bg=bg_color,
                  font=('times new roman', 16, 'bold')).grid(row=i, column=0, sticky='W')
            Entry(F4, textvariable=var, width=10,
                  font=('times new roman', 16), bd=5).grid(row=i, column=1)

        # ================= Bill Area =================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)

        Label(F5, text="Bill Area", font='arial 15 bold').pack(fill=X)
        scroll = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT, fill=Y)
        scroll.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ================= Buttons =================
        F6 = Frame(self.root, bd=10, relief=GROOVE)
        F6.place(x=0, y=560, relwidth=1, height=140)

        Button(F6, text="Total", command=self.total,
               bg="#535C68", fg="white", width=12,
               font='arial 13 bold').grid(row=0, column=0, padx=10)

        Button(F6, text="Generate Bill", command=self.bill_area,
               bg="#535C68", fg="white", width=12,
               font='arial 13 bold').grid(row=0, column=1, padx=10)

        Button(F6, text="Clear", command=self.clear_data,
               bg="#535C68", fg="white", width=12,
               font='arial 13 bold').grid(row=0, column=2, padx=10)

        Button(F6, text="Exit", command=self.exit_app,
               bg="#535C68", fg="white", width=12,
               font='arial 13 bold').grid(row=0, column=3, padx=10)

        self.welcome_bill()

    # ================= TOTAL =================
    def total(self):
        self.med_total = (
            self.sanitizer.get()*2 +
            self.mask.get()*5 +
            self.hand_gloves.get()*12 +
            self.dettol.get()*30 +
            self.newsprin.get()*5 +
            self.thermal_gun.get()*15
        )
        self.gro_total = (
            self.rice.get()*10 +
            self.food_oil.get()*10 +
            self.wheat.get()*10 +
            self.daal.get()*6 +
            self.flour.get()*8 +
            self.maggi.get()*5
        )
        self.cold_total = (
            self.sprite.get()*10 +
            self.limka.get()*10 +
            self.mazza.get()*10 +
            self.coke.get()*10 +
            self.fanta.get()*10 +
            self.mountain_duo.get()*10
        )

        self.med_tax = round(self.med_total * 0.05, 2)
        self.gro_tax = round(self.gro_total * 0.05, 2)
        self.cold_tax = round(self.cold_total * 0.1, 2)

        self.total_bill = self.med_total + self.gro_total + self.cold_total + self.med_tax + self.gro_tax + self.cold_tax

    # ================= BILL =================
    def welcome_bill(self):
        self.txtarea.delete("1.0", END)
        self.txtarea.insert(END, "Welcome Retail Store\n")
        self.txtarea.insert(END, f"Bill No: {self.bill_no.get()}\n")
        self.txtarea.insert(END, f"Customer: {self.c_name.get()}\n")
        self.txtarea.insert(END, f"Phone: {self.c_phone.get()}\n")
        self.txtarea.insert(END, "-"*40 + "\n")
        self.txtarea.insert(END, "Product\tQty\tPrice\n")
        self.txtarea.insert(END, "-"*40 + "\n")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer details required")
            return

        self.total()
        self.welcome_bill()

        self.txtarea.insert(END, f"Medical Total:\t\tRs.{self.med_total}\n")
        self.txtarea.insert(END, f"Grocery Total:\t\tRs.{self.gro_total}\n")
        self.txtarea.insert(END, f"Cold Drinks Total:\tRs.{self.cold_total}\n")
        self.txtarea.insert(END, "-"*40 + "\n")
        self.txtarea.insert(END, f"TOTAL BILL:\t\tRs.{self.total_bill}\n")

    # ================= UTIL =================
    def clear_data(self):
        for v in [self.sanitizer, self.mask, self.hand_gloves, self.dettol,
                  self.newsprin, self.thermal_gun, self.rice, self.food_oil,
                  self.wheat, self.daal, self.flour, self.maggi,
                  self.sprite, self.limka, self.mazza, self.coke,
                  self.fanta, self.mountain_duo]:
            v.set(0)

        self.c_name.set("")
        self.c_phone.set("")
        self.welcome_bill()

    def exit_app(self):
        self.root.destroy()

    def find_bill(self):
        messagebox.showinfo("Info", "Search feature optional")

root = Tk()
obj = Bill_App(root)
root.mainloop()
