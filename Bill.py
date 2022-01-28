from tkinter import *
import math
import random
import os
from tkinter import messagebox
import tkinter
try:
    os.makedirs("C:\\Bills")
except:
    pass


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x720+0+0")
        self.root.title("Billing Software")

        bg_title = "#01aed4"
        bg_customer = "#DC143C"
        title = Label(self.root, text="Billing Software", fg="black", bd=12, relief=GROOVE,
                      bg=bg_title, font=("times new roman", 30, "bold"), pady=(2)).pack(fill=X)

        # Variable Declaration
        # Cosmetics Variables
        self.soap = IntVar()
        self.fc = IntVar()
        self.lotion = IntVar()
        self.powder = IntVar()
        self.shampoo = IntVar()
        self.hair = IntVar()
        self.spray = IntVar()
        # grocery Variables
        self.chilli = DoubleVar()
        self.urad = DoubleVar()
        self.toor = DoubleVar()
        self.chana = DoubleVar()
        self.instnood = IntVar()
        self.rice = DoubleVar()
        self.red = DoubleVar()
        # Beverage Variables
        self.sprite = DoubleVar()
        self.coca = DoubleVar()
        self.maaza = DoubleVar()
        self.pepsi = DoubleVar()
        self.frooti = DoubleVar()
        self.slice = DoubleVar()
        self.pulp = DoubleVar()
        # total Product Price and Tax Variables
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.beverage_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.beverage_tax = StringVar()
        # Customer Variables
        self.cust_name = StringVar()
        self.mob = StringVar()
        self.bill = StringVar()
        self.search = StringVar()
        x = random.randint(1, 9999)
        self.bill.set(str(x))

        # Customer Details Frame
        F1 = LabelFrame(self.root, bd=7, relief=GROOVE, text="Customer Details",
                        fg="black", font=("times new roman", 15, "bold"), bg=bg_title)
        F1.place(x=0, y=80, relwidth=1)
        # Customer Details
        cust_lbl = Label(F1, text="Customer Name", font=("times new roman", 15, "bold"),
                         fg="white", bg=bg_title).grid(row=0, column=0, padx=10, pady=3)
        cust_ent = Entry(F1, width=30, bd=4, textvariable=self.cust_name,
                         relief=RIDGE, font="arial 10").grid(row=0, column=1, pady=5, padx=10)
        mob_lbl = Label(F1, text="Mobile Number", font=("times new roman", 15, "bold"),
                        fg="white", bg=bg_title).grid(row=0, column=2, padx=10, pady=3)
        mob_ent = Entry(F1, width=30, bd=4, textvariable=self.mob, relief=RIDGE,
                        font="arial 10").grid(row=0, column=3, padx=10, pady=5)
        bll_lbl = Label(F1, text="Bill Number", font=("times new roman", 15, "bold"),
                        fg="white", bg=bg_title).grid(row=0, column=4, padx=10, pady=3)
        bll_ent = Entry(F1, width=30, bd=4, relief=RIDGE, textvariable=self.search,
                        font="arial 10").grid(row=0, column=5, padx=10, pady=5)
        bll_bttn = Button(F1, text="Search", command=self.search_bill, font=(
            "Arial", 15), width=8, bd=4).grid(row=0, column=6)

        # Cosmetics Frame
        F2 = LabelFrame(self.root, bd=7, relief=GROOVE, text="Cosmetics",
                        fg="black", font=("times new roman", 15, "bold"), bg=bg_title)
        F2.place(x=5, y=160, width=325, height=350)
        # Cosmetics Details
        bath_lbl = Label(F2, text="Bath Soap", font=("times new roman", 12, "bold"),
                         bg=bg_title, fg="White").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        bath_ent = Entry(F2, width=5, textvariable=self.soap, font=(
            "arial"), bd=2, relief=RIDGE).grid(row=0, column=1, padx=5, pady=5)
        cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 12, "bold"),
                          bg=bg_title, fg="White").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        cream_ent = Entry(F2, width=5, textvariable=self.fc, font=(
            "arial"), bd=2, relief=RIDGE).grid(row=1, column=1, padx=5, pady=5)
        lotion_lbl = Label(F2, text="Body Lotion", font=("times new roman", 12, "bold"),
                           bg=bg_title, fg="White").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        lotion_ent = Entry(F2, width=5, font=("arial"), textvariable=self.lotion,
                           bd=2, relief=RIDGE).grid(row=2, column=1, padx=5, pady=5)
        powder_lbl = Label(F2, text="Powder", font=("times new roman", 12, "bold"),
                           bg=bg_title, fg="White").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        powder_ent = Entry(F2, width=5, font=("arial"), textvariable=self.powder,
                           bd=2, relief=RIDGE).grid(row=3, column=1, padx=5, pady=5)
        shampoo_lbl = Label(F2, text="Shampoo", font=("times new roman", 12, "bold"),
                            bg=bg_title, fg="White").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        shampoo_ent = Entry(F2, width=5, textvariable=self.shampoo, font=(
            "arial"), bd=2, relief=RIDGE).grid(row=4, column=1, padx=5, pady=5)
        hair_lbl = Label(F2, text="Hair Dye", font=("times new roman", 12, "bold"),
                         bg=bg_title, fg="White").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        hair_ent = Entry(F2, width=5, font=("arial"), textvariable=self.hair,
                         bd=2, relief=RIDGE).grid(row=5, column=1, padx=5, pady=5)
        spray_lbl = Label(F2, text="Body Spray", font=("times new roman", 12, "bold"),
                          bg=bg_title, fg="White").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        spray_ent = Entry(F2, width=5, font=("arial"), textvariable=self.spray,
                          bd=2, relief=RIDGE).grid(row=6, column=1, padx=5, pady=5)
        # Grocery Frame
        F3 = LabelFrame(self.root, bd=7, relief=GROOVE, text="Grocery", fg="black", font=(
            "times new roman", 15, "bold"), bg=bg_title)
        F3.place(x=330, y=160, width=325, height=350)
        # Grocery Details
        chilli_lbl = Label(F3, text="Chilli Powder", font=("times new roman", 12, "bold"),
                           bg=bg_title, fg="White").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        chilli_ent = Entry(F3, width=5, font=("arial"), textvariable=self.chilli,
                           bd=2, relief=RIDGE).grid(row=0, column=1, padx=5, pady=5)
        urad_lbl = Label(F3, text="Urad Dal", font=("times new roman", 12, "bold"),
                         bg=bg_title, fg="White").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        urad_ent = Entry(F3, width=5, font=("arial"), textvariable=self.urad,
                         bd=2, relief=RIDGE).grid(row=1, column=1, padx=5, pady=5)
        toor_lbl = Label(F3, text="Toor Dal", font=("times new roman", 12, "bold"),
                         bg=bg_title, fg="White").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        toor_ent = Entry(F3, width=5, font=("arial"), textvariable=self.toor,
                         bd=2, relief=RIDGE).grid(row=2, column=1, padx=5, pady=5)
        chana_lbl = Label(F3, text="Chana Dal", font=("times new roman", 12, "bold"),
                          bg=bg_title, fg="White").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        chana_ent = Entry(F3, width=5, font=("arial"), textvariable=self.chana,
                          bd=2, relief=RIDGE).grid(row=3, column=1, padx=5, pady=5)
        inst_nood_lbl = Label(F3, text="Instant Noodles", font=("times new roman", 12, "bold"),
                              bg=bg_title, fg="White").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        inst_nood_ent = Entry(F3, width=5, font=("arial"), textvariable=self.instnood,
                              bd=2, relief=RIDGE).grid(row=4, column=1, padx=5, pady=5)
        rice_lbl = Label(F3, text="Rice", font=("times new roman", 12, "bold"),
                         bg=bg_title, fg="White").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        rice_ent = Entry(F3, width=5, font=("arial"), textvariable=self.rice,
                         bd=2, relief=RIDGE).grid(row=5, column=1, padx=5, pady=5)
        red_lbl = Label(F3, text="Red Gram", font=("times new roman", 12, "bold"),
                        bg=bg_title, fg="White").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        red_ent = Entry(F3, width=5, font=("arial"), textvariable=self.red,
                        bd=2, relief=RIDGE).grid(row=6, column=1, padx=5, pady=5)
        # Beverages Frame
        F4 = LabelFrame(self.root, bd=7, relief=GROOVE, text="Beverages",
                        fg="black", font=("times new roman", 15, "bold"), bg=bg_title)
        F4.place(x=655, y=160, width=325, height=350)
        # Beverages Details
        sprite_lbl = Label(F4, text="Sprite", font=("times new roman", 12, "bold"),
                           bg=bg_title, fg="White").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        sprite_ent = Entry(F4, width=5, font=("arial"), textvariable=self.sprite,
                           bd=2, relief=RIDGE).grid(row=0, column=1, padx=5, pady=5)
        cocacola_lbl = Label(F4, text="Coca Cola", font=("times new roman", 12, "bold"),
                             bg=bg_title, fg="White").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        cocacola_ent = Entry(F4, width=5, font=("arial"), textvariable=self.coca,
                             bd=2, relief=RIDGE).grid(row=1, column=1, padx=5, pady=5)
        maaza_lbl = Label(F4, text="Maaza", font=("times new roman", 12, "bold"),
                          bg=bg_title, fg="White").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        maaza_ent = Entry(F4, width=5, font=("arial"), textvariable=self.maaza,
                          bd=2, relief=RIDGE).grid(row=2, column=1, padx=5, pady=5)
        pepsi_lbl = Label(F4, text="Pepsi", font=("times new roman", 12, "bold"),
                          bg=bg_title, fg="White").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        pepsi_ent = Entry(F4, width=5, font=("arial"), textvariable=self.pepsi,
                          bd=2, relief=RIDGE).grid(row=3, column=1, padx=5, pady=5)
        frooti_lbl = Label(F4, text="Frooti", font=("times new roman", 12, "bold"),
                           bg=bg_title, fg="White").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        frooti_ent = Entry(F4, width=5, font=("arial"), textvariable=self.frooti,
                           bd=2, relief=RIDGE).grid(row=4, column=1, padx=5, pady=5)
        slice_lbl = Label(F4, text="Slice", font=("times new roman", 12, "bold"),
                          bg=bg_title, fg="White").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        slice_ent = Entry(F4, width=5, font=("arial"), textvariable=self.slice,
                          bd=2, relief=RIDGE).grid(row=5, column=1, padx=5, pady=5)
        pulp_lbl = Label(F4, text="Pulp", font=("times new roman", 12, "bold"),
                         bg=bg_title, fg="White").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        pulp_ent = Entry(F4, width=5, font=("arial"), textvariable=self.pulp,
                         bd=2, relief=RIDGE).grid(row=6, column=1, padx=5, pady=5)
        # Toys Frame
        F5 = LabelFrame(self.root, bd=7, relief=GROOVE, text="Toys", fg="gold", font=(
            "times new roman", 15, "bold"), bg=bg_title)
        F5.place(x=980, y=160, width=325, height=350)
        # Toys Details
        rubiks_lbl = Label(F5, text="Rubiks Cube", font=("times new roman", 12, "bold"),
                           bg=bg_title, fg="White").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        rubiks_ent = Entry(F5, width=5, font=("arial"), bd=2, relief=RIDGE).grid(
            row=0, column=1, padx=5, pady=5)
        lego_lbl = Label(F5, text="Lego", font=("times new roman", 12, "bold"),
                         bg=bg_title, fg="White").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        lego_ent = Entry(F5, width=5, font=("arial"), bd=2, relief=RIDGE).grid(
            row=1, column=1, padx=5, pady=5)
        ball_lbl = Label(F5, text="Ball", font=("times new roman", 12, "bold"),
                         bg=bg_title, fg="White").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        ball_ent = Entry(F5, width=5, font=("arial"), bd=2, relief=RIDGE).grid(
            row=2, column=1, padx=5, pady=5)
        car_lbl = Label(F5, text="RC Car", font=("times new roman", 12, "bold"),
                        bg=bg_title, fg="White").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        car_ent = Entry(F5, width=5, font=("arial"), bd=2, relief=RIDGE).grid(
            row=3, column=1, padx=5, pady=5)
        train_lbl = Label(F5, text="RC train", font=("times new roman", 12, "bold"),
                          bg=bg_title, fg="White").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        train_ent = Entry(F5, width=5, font=("arial"), bd=2, relief=RIDGE).grid(
            row=4, column=1, padx=5, pady=5)
        truck_lbl = Label(F5, text="RC Truck", font=("times new roman", 12, "bold"),
                          bg=bg_title, fg="White").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        truck_ent = Entry(F5, width=5, font=("arial"), bd=2, relief=RIDGE).grid(
            row=5, column=1, padx=5, pady=5)
        jcb_lbl = Label(F5, text="JCB", font=("times new roman", 12, "bold"),
                        bg=bg_title, fg="White").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        jcb_ent = Entry(F5, width=5, font=("arial"), bd=2, relief=RIDGE).grid(
            row=6, column=1, padx=5, pady=5)

        # Bill Frame
        F5 = Label(self.root, bd=7, relief=GROOVE)
        F5.place(x=1000, y=160, width=400, height=350)
        bill_title = Label(F5, text="BILL AREA", font=(
            "Arial", 15, "bold"), fg="Black", bd=4, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=2)

        # Button Frame
        F6 = LabelFrame(self.root, bd=7, relief=GROOVE, text="Bill Menu",
                        fg="black", font=("times new roman", 15, "bold"), bg=bg_title)
        F6.place(x=0, y=510, relwidth=1, height=140)
        m1 = Label(F6, text="Total Cosmetic Price", font=("times new roman", 12, "bold"),
                   bg=bg_title, fg="white").grid(row=0, column=0, padx=10, pady=1, sticky="w")
        m1_ent = Entry(F6, width=10, textvariable=self.cosmetic_price, bd=4,
                       relief=RIDGE, font="arial").grid(row=0, column=1, pady=1, padx=10)
        m1_east = Label(F6, text="Cosmetic Tax Price", font=("times new roman", 12, "bold"),
                        bg=bg_title, fg="white").grid(row=0, column=2, padx=10, pady=1, sticky="e")
        m1_east_ent = Entry(F6, width=10, bd=4, textvariable=self.cosmetic_tax,
                            relief=RIDGE, font="arial").grid(row=0, column=3, pady=1, padx=10)
        m2 = Label(F6, text="Total Grocery Price", font=("times new roman", 12, "bold"),
                   bg=bg_title, fg="white").grid(row=1, column=0, padx=10, pady=1, sticky="w")
        m2_ent = Entry(F6, width=10, bd=4, textvariable=self.grocery_price,
                       relief=RIDGE, font="arial").grid(row=1, column=1, pady=1, padx=10)
        m2_east = Label(F6, text="Grocery Tax Price", font=("times new roman", 12, "bold"),
                        bg=bg_title, fg="white").grid(row=1, column=2, padx=10, pady=1, sticky="e")
        m2_east_ent = Entry(F6, width=10, textvariable=self.grocery_tax, bd=4,
                            relief=RIDGE, font="arial").grid(row=1, column=3, pady=1, padx=10)
        m3 = Label(F6, text="Total Beverage Price", font=("times new roman", 12, "bold"),
                   bg=bg_title, fg="white").grid(row=2, column=0, padx=10, pady=1, sticky="w")
        m3_ent = Entry(F6, width=10, bd=4, textvariable=self.beverage_price,
                       relief=RIDGE, font="arial").grid(row=2, column=1, pady=1, padx=10)
        m3_east = Label(F6, text="Beverage Tax Price", font=("times new roman", 12, "bold"),
                        bg=bg_title, fg="white").grid(row=2, column=2, padx=10, pady=1, sticky="e")
        m3_east_ent = Entry(F6, width=10, textvariable=self.beverage_tax, bd=4,
                            relief=RIDGE, font="arial").grid(row=2, column=3, pady=1, padx=10)

        btn_f = Frame(F6, bd=7, relief=GROOVE, bg="white")
        btn_f.place(x=750, width=710, height=105)
        bg_btn = "Dark Blue"

        total_btn = Button(btn_f, text="Total", command=self.total, font=(
            "Arial", 15), bd=3, bg=bg_btn, fg="white", pady=15, padx=3, width=10).grid(row=0, column=0, padx=5, pady=5)
        gbill_btn = Button(btn_f, text="Generate\nBill", command=self.bill_area, font=(
            "Arial", 15), bd=3, bg=bg_btn, fg="white", pady=5, padx=3, width=10).grid(row=0, column=1, padx=5, pady=5)
        clear_btn = Button(btn_f, text="Clear", command=self.clear, font=(
            "Arial", 15), bd=3, bg=bg_btn, fg="white", pady=15, padx=3, width=10).grid(row=0, column=3, padx=5, pady=5)
        exit_btn = Button(btn_f, text="Exit", font=("Arial", 15), command=self.exit_app, bd=3,
                          bg=bg_btn, fg="white", pady=15, padx=3, width=10).grid(row=0, column=4, padx=5, pady=5)
        enxit_btn = Button(btn_f, text="Save", font=("Arial", 15), command=self.save_file, bd=3,
                           bg=bg_btn, fg="white", pady=15, padx=3, width=10).grid(row=0, column=2, padx=5, pady=5)
        self.welcome_bill()

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome, Shanmukh Retail.\n")
        self.txtarea.insert(END, f"\n Bill Number : {self.bill.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.cust_name.get()}")
        self.txtarea.insert(END, f"\n Mobile Number : {self.mob.get()}")
        self.txtarea.insert(
            END, "\n=============================================")
        self.txtarea.insert(END, "\nProducts\t\tQTY\tPrice\tTax")
        self.txtarea.insert(
            END, "\n=============================================")

    def total(self):
        # Cosmetics Price Variable Storing
        self.c_s_p = (self.soap.get()*20)
        self.c_f_p = (self.fc.get()*75)
        self.c_l_p = (self.lotion.get()*120)
        self.c_p_p = (self.powder.get()*100)
        self.c_sh_p = (self.shampoo.get()*260)
        self.c_h_p = (self.hair.get()*50)
        self.c_t_p = (self.spray.get()*80)
        # Cosmetics Tax Variable Storing
        self.c_s_t = round(self.c_s_p*(18/100), 2)
        self.c_f_t = round(self.c_f_p*(18/100), 2)
        self.c_l_t = round(self.c_l_p*(18/100), 2)
        self.c_p_t = round(self.c_p_p*(18/100), 2)
        self.c_sh_t = round(self.c_sh_p*(18/100), 2)
        self.c_h_t = round(self.c_h_p*(18/100), 2)
        self.c_t_t = round(self.c_t_p*(18/100), 2)
        self.total_cosmetic_price = float(
            self.c_s_p +
            self.c_f_p +
            self.c_l_p +
            self.c_p_p +
            self.c_sh_p +
            self.c_h_p +
            self.c_t_p)
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax = round(self.total_cosmetic_price*(18/100), 2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))
        # grocery price Variable Storing
        self.g_ci_p = round((self.chilli.get()*150), 2)
        self.g_u_p = round((self.urad.get()*120), 2)
        self.g_t_p = round((self.toor.get()*110), 2)
        self.g_c_p = round((self.chana.get()*120), 2)
        self.g_i_p = round((self.instnood.get()*60), 2)
        self.g_r_p = round((self.rice.get()*40), 2)
        self.g_re_p = round((self.red.get()*90), 2)
        # grocery tax variable storing
        self.g_ci_t = round((self.chilli.get()*150)*(5/100), 2)
        self.g_u_t = round((self.urad.get()*120)*(5/100), 2)
        self.g_t_t = round((self.toor.get()*110)*(5/100), 2)
        self.g_c_t = round((self.chana.get()*120)*(5/100), 2)
        self.g_i_t = round((self.instnood.get()*60)*(5/100), 2)
        self.g_r_t = round((self.rice.get()*40)*(5/100), 2)
        self.g_re_t = round((self.red.get()*90)*(5/100), 2)

        self.total_grocery_price = float(
            self.g_ci_p +
            self.g_u_p +
            self.g_t_p +
            self.g_c_p +
            self.g_i_p +
            self.g_r_p +
            self.g_re_p)
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax = round(self.total_grocery_price*(5/100), 2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))
        # beverage price variable storing
        self.b_s_p = round((self.sprite.get()*80), 2)
        self.b_c_p = round((self.coca.get()*70), 2)
        self.b_m_p = round((self.maaza.get()*90), 2)
        self.b_p_p = round((self.pepsi.get()*90), 2)
        self.b_f_p = round((self.frooti.get()*60), 2)
        self.b_sl_p = round((self.slice.get()*75), 2)
        self.b_pl_p = round((self.pulp.get()*65), 2)
        # beverage tax variable storing
        self.b_s_t = self.b_s_p*(18/100)
        self.b_c_t = self.b_c_p*(18/100)
        self.b_m_t = self.b_m_p*(18/100)
        self.b_p_t = self.b_p_p*(18/100)
        self.b_f_t = self.b_f_p*(18/100)
        self.b_s_t = self.b_sl_p*(18/100)
        self.b_pl_t = self.b_pl_p*(18/100)
        self.total_beverage_price = float(
            self.b_s_p +
            self.b_c_p +
            self.b_m_p +
            self.b_p_p +
            self.b_f_p +
            self.b_sl_p +
            self.b_pl_p)
        self.beverage_price.set("Rs. "+str(self.total_beverage_price))
        self.b_tax = round(self.total_beverage_price*(18/100), 2)
        self.beverage_tax.set("Rs. "+str(self.b_tax))

        self.total_price = self.total_beverage_price + \
            self.total_cosmetic_price+self.total_grocery_price
        round(self.total_price, 2)
        self.total_tax = round(self.total_beverage_price*(18/100), 2)+round(
            self.total_grocery_price*(5/100), 2)+round(self.total_cosmetic_price*(18/100), 2)
        round(self.total_tax, 2)

        self.total_bill = self.total_price+self.total_tax
        round(self.total_bill, 2)

    def bill_area(self):
        if self.cust_name.get() == "" or self.mob.get() == "":
            messagebox.showerror("Error", "Customer Details are Important")
        elif self.cosmetic_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.beverage_price.get() == "Rs. 0.0":
            messagebox.showerror("Error", "Shopping cart is empty.")

        else:
            self.welcome_bill()
            # cosmetics
            if self.soap.get() != 0:
                self.txtarea.insert(
                    END, f"\n Bath Soap\t\t{self.soap.get()}U\tRs.{self.c_s_p}\tRs.{self.c_s_t}")
            if self.fc.get() != 0:
                self.txtarea.insert(
                    END, f"\n Face cream\t\t{self.fc.get()}U\tRs.{self.c_f_p}\tRs.{self.c_f_t}")
            if self.lotion.get() != 0:
                self.txtarea.insert(
                    END, f"\n Body Lotion\t\t{self.lotion.get()}U\tRs.{self.c_l_p}\tRs.{self.c_l_t}")
            if self.powder.get() != 0:
                self.txtarea.insert(
                    END, f"\n Powder\t\t{self.powder.get()}U\tRs.{self.c_p_p}\tRs.{self.c_p_t}")
            if self.shampoo.get() != 0:
                self.txtarea.insert(
                    END, f"\n Shampoo\t\t{self.shampoo.get()}U\tRs.{self.c_sh_p}\tRs.{self.c_sh_t}")
            if self.hair.get() != 0:
                self.txtarea.insert(
                    END, f"\n Hair Dye\t\t{self.hair.get()}U\tRs.{self.c_h_p}\tRs.{self.c_h_t}")
            if self.spray.get() != 0:
                self.txtarea.insert(
                    END, f"\n Body Spray\t\t{self.spray.get()}U\tRs.{self.c_t_p}\tRs.{self.c_t_t}")
            if self.cosmetic_tax.get() != "Rs. 0.0":
                self.txtarea.insert(
                    END, "\n---------------------------------------------")
                self.txtarea.insert(
                    END, f"\n Cosmetic Tax\t\t\t\t{self.cosmetic_tax.get()}")
                self.txtarea.insert(
                    END, "\n---------------------------------------------")
            # Grocery
            if self.chilli.get() != 0:
                self.txtarea.insert(
                    END, f"\n Chilli\nPowder\t\t{self.chilli.get()}Kgs\tRs.{self.g_ci_p}\tRs.{self.g_ci_t}")
            if self.urad.get() != 0:
                self.txtarea.insert(
                    END, f"\n Urad Dal\t\t{self.urad.get()}Kgs\tRs.{self.g_u_p}\tRs.{self.g_u_t}")
            if self.toor.get() != 0:
                self.txtarea.insert(
                    END, f"\n Toor Dal\t\t{self.toor.get()}Kgs\tRs.{self.g_t_p}\tRs.{self.g_t_t}")
            if self.chana.get() != 0:
                self.txtarea.insert(
                    END, f"\n Chana Dal\t\t{self.chana.get()}Kgs\tRs.{self.g_c_p}\tRs.{self.g_c_t}")
            if self.instnood.get() != 0:
                self.txtarea.insert(
                    END, f"\n Instant\nNoodles\t\t{self.instnood.get()}U\tRs.{self.g_i_p}\tRs.{self.g_i_t}")
            if self.rice.get() != 0:
                self.txtarea.insert(
                    END, f"\n Rice\t\t{self.rice.get()}Kgs\tRs.{self.g_r_p}\tRs.{self.g_r_t}")
            if self.red.get() != 0:
                self.txtarea.insert(
                    END, f"\n Red Gram\t\t{self.red.get()}Kgs\tRs.{self.g_re_p}\tRs.{self.g_re_t}")
            if self.grocery_tax.get() != "Rs. 0.0":
                self.txtarea.insert(
                    END, "\n---------------------------------------------")
                self.txtarea.insert(
                    END, f"\n Grocery Tax\t\t\t\t{self.grocery_tax.get()}")
                self.txtarea.insert(
                    END, "\n---------------------------------------------")
            # Beverages
            if self.sprite.get() != 0:
                self.txtarea.insert(
                    END, f"\n Sprite\t\t{self.rice.get()}L\tRs.{self.b_s_p}\tRs.{self.b_s_t}")
            if self.coca.get() != 0:
                self.txtarea.insert(
                    END, f"\n Coca Cola\t\t{self.rice.get()}L\tRs.{self.b_c_p}\tRs.{self.b_c_t}")
            if self.maaza.get() != 0:
                self.txtarea.insert(
                    END, f"\n Maaza\t\t{self.rice.get()}L\tRs.{self.b_m_p}\tRs.{self.b_m_t}")
            if self.pepsi.get() != 0:
                self.txtarea.insert(
                    END, f"\n Pepsi\t\t{self.rice.get()}L\tRs.{self.b_p_p}\tRs.{self.b_p_t}")
            if self.frooti.get() != 0:
                self.txtarea.insert(
                    END, f"\n Frooti\t\t{self.rice.get()}L\tRs.{self.b_f_p}\tRs.{self.b_f_t}")
            if self.slice.get() != 0:
                self.txtarea.insert(
                    END, f"\n Mango Slice\t\t{self.rice.get()}L\tRs.{self.b_sl_p}\tRs.{self.b_sl_t}")
            if self.pulp.get() != 0:
                self.txtarea.insert(
                    END, f"\n Orange Pulp\t\t{self.rice.get()}L\tRs.{self.b_pl_p}\tRs.{self.b_pl_t}")
            if self.beverage_tax.get() != "Rs. 0.0":
                self.txtarea.insert(
                    END, "\n---------------------------------------------")
                self.txtarea.insert(
                    END, f"\n Beverages Tax\t\t\t\t{self.beverage_tax.get()}")
                self.txtarea.insert(
                    END, "\n---------------------------------------------")

            self.txtarea.insert(
                END, "\n---------------------------------------------")
            self.txtarea.insert(
                END, f"\nTotal \t\t\tRs.{self.total_price}\tRs.{self.total_tax}")
            self.txtarea.insert(
                END, "\n---------------------------------------------\n")
            self.txtarea.insert(
                END, "\n*********************************************")
            self.txtarea.insert(END, f"\nGrand Total \t\t\t{self.total_bill}")

    def save_file(self):
        op = messagebox.askyesno(
            "Save File", "Do you want to save this Bill ?")
        if op > 0:
            self.billdata = self.txtarea.get('0.0', END)
            f = open(f"C:\\Bills\\{self.bill.get()}.bill", "w")
            f.write(self.billdata)
            f.close()
            messagebox.showinfo(
                "Save File", f"Your Bill {self.bill} has been saved successfully.")
        else:
            return

    def search_bill(self):
        present = "no"
        for i in os.listdir("C:\\Bills\\"):
            if i.split('.')[0] == self.search.get():
                f = open(f"C:\\Bills\\{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f:
                    self.txtarea.insert(END, d)
                f.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill Number.")

    def clear(self):
        op = messagebox.askyesno(
            "Clear", "Do you want to clear the current bill ?")
        if op > 0:
            # Variable Declaration
            # Cosmetics Variables
            self.soap.set(0)
            self.fc.set(0)
            self.lotion.set(0)
            self.powder.set(0)
            self.shampoo.set(0)
            self.hair.set(0)
            self.spray.set(0)
            # grocery Variables
            self.chilli.set(0.0)
            self.urad.set(0.0)
            self.toor.set(0.0)
            self.chana.set(0.0)
            self.instnood.set(0)
            self.rice.set(0.0)
            self.red.set(0.0)
            # Beverage Variables
            self.sprite.set(0.0)
            self.coca.set(0.0)
            self.maaza.set(0.0)
            self.pepsi.set(0.0)
            self.frooti.set(0.0)
            self.slice.set(0.0)
            self.pulp.set(0.0)
            # total Product Price and Tax Variables
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.beverage_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.beverage_tax.set("")
            # Customer Variables
            self.cust_name.set("")
            self.mob.set("")
            self.bill.set("")
            self.search.set("")
            self.txtarea.delete('1.0', END)
            x = random.randint(1, 9999)
            self.bill.set(str(x))
            self.welcome_bill()

        else:
            return

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you want to Exit the App ?")
        if op > 0:
            self.root.destroy()
        else:
            return


root = tkinter.Tk()
obj = Bill_App(root)
root.wm_iconbitmap(
    r"C:\Users\shanm\OneDrive\Desktop\My projects\Billing Software\icon.ico")

root.mainloop()
