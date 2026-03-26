import tkinter as tk
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("themes/breeze.json")

dashboard_window = ctk.CTk()
dashboard_window.title("Dashboard")
dashboard_window.resizable(0,0)
dashboard_window.after(0, lambda: dashboard_window.state("zoomed"))

borderWidth = 1
leftFrameButtonAnchor = 'center'

# ---------- HEADER FRAME ----------
header = ctk.CTkFrame(dashboard_window, fg_color="#03396C", height=100, corner_radius=0)
header.pack(fill="x")
header.pack_propagate(False)  # keeps height fixed at 100

header.grid_columnconfigure(0, weight=1)
header.grid_columnconfigure(1, weight=10)
header.grid_columnconfigure(2, weight=1)

# ---------- HEADER IMAGE & TITLE ----------
imagePath = "Images/stock.png"
inventory_logo = ctk.CTkImage(Image.open(imagePath), size=(128, 128))

title_label = ctk.CTkLabel(
    header,
    text="INVENTORY MANAGEMENT SYSTEM",
    padx=25,
    image=inventory_logo,
    compound="left",
    font=("roboto condensed", 70, "bold"),
    text_color="white"
)
title_label.grid(row=0, column=0, sticky="w", padx=20, pady=10)

logout_button = ctk.CTkButton(
    header,
    text="LOGOUT",
    font=("roboto condensed", 20, "bold"),
    width=180,
    height=80,
    corner_radius=35, border_width=borderWidth, border_color="black"
)
logout_button.grid(row=0, column=2, sticky="e", padx=20)

# ---------- SUBTITLE ----------
subtitleLabel = ctk.CTkLabel(
    dashboard_window,
    fg_color='cyan',
    text='Welcome Admin\t\t Date: 26-03-2026\t\t Time: 12:36:17 pm',
    font=("roboto condensed", 25, "bold"),
    text_color="black"
)
subtitleLabel.pack(fill="x")  # naturally sits below header

# ---------- MAIN BODY FRAME ----------
bodyFrame = ctk.CTkFrame(dashboard_window, corner_radius=0, fg_color="transparent")
bodyFrame.pack(fill="both", expand=True)  # fills remaining space

# ---------- LEFT FRAME ----------
leftFrame = ctk.CTkFrame(bodyFrame, corner_radius=0, width=400)
leftFrame.pack(side="left", fill="y")
leftFrame.pack_propagate(False)  # keeps width fixed
leftFrame.grid_columnconfigure(0, weight=1)

leftFrameLogo = "Images/warehouse-management-system.png"
warehouse_logo = ctk.CTkImage(Image.open(leftFrameLogo), size=(200, 200))

imagelabel = ctk.CTkLabel(leftFrame, image=warehouse_logo, text='')
imagelabel.grid(row=0, column=0, padx=20, pady=(70, 10))

menuLabel = ctk.CTkLabel(
    leftFrame,
    text="MENU",
    padx=25,
    font=("roboto condensed", 40, "bold"),
    fg_color='#009688',  # use fg_color instead of bg_color
    text_color="white",
    width=400, height=70
)
menuLabel.grid(row=1, column=0)

# ---------- Employer Button ----------
employee_Icon_path = "Images/staff.png"
employee_logo = ctk.CTkImage(Image.open(employee_Icon_path), size=(64, 64))
employee_Button = ctk.CTkButton(
    leftFrame,
    text=" EMPLOYEE",image=employee_logo,compound="left",
    font=("roboto condensed", 40, "bold"),
    width=400,
    height=70,
    corner_radius=0, anchor=leftFrameButtonAnchor, border_width=borderWidth, border_color="black"
)
employee_Button.grid(row=2, column=0)

# ---------- Supplier Button ----------
supplier_Icon_path = "Images/supplier.png"
supplier_logo = ctk.CTkImage(Image.open(supplier_Icon_path), size=(64, 64))
supplier_Button = ctk.CTkButton(
    leftFrame,
    text=" SUPPLIER",image=supplier_logo,compound="left",
    font=("roboto condensed", 40, "bold"),
    width=400,
    height=70,
    corner_radius=0, anchor=leftFrameButtonAnchor, border_width=borderWidth, border_color="black"
)
supplier_Button.grid(row=3, column=0)

# ---------- Category Button ----------
category_Icon_path = "Images/category.png"
category_logo = ctk.CTkImage(Image.open(category_Icon_path), size=(64, 64))
category_Button = ctk.CTkButton(
    leftFrame,
    text=" CATEGORIES",image=category_logo,compound="left",
    font=("roboto condensed", 40, "bold"),
    width=400,
    height=70,
    corner_radius=0, anchor=leftFrameButtonAnchor, border_width=borderWidth, border_color="black"
)
category_Button.grid(row=4, column=0)

# ---------- Products Button ----------
products_Icon_path = "Images/products.png"
products_logo = ctk.CTkImage(Image.open(products_Icon_path), size=(64, 64))
products_Button = ctk.CTkButton(
    leftFrame,
    text=" PRODUCTS",image=products_logo,compound="left",
    font=("roboto condensed", 40, "bold"),
    width=400,
    height=70,
    corner_radius=0, anchor=leftFrameButtonAnchor, border_width=borderWidth, border_color="black"
)
products_Button.grid(row=5, column=0)

# ---------- Sales Button ----------
sales_Icon_path = "Images/sales.png"
sales_logo = ctk.CTkImage(Image.open(sales_Icon_path), size=(64, 64))
sales_Button = ctk.CTkButton(
    leftFrame,
    text=" SALES",image=sales_logo,compound="left",
    font=("roboto condensed", 40, "bold"),
    width=400,
    height=70,
    corner_radius=0, anchor=leftFrameButtonAnchor, border_width=borderWidth, border_color="black"
)
sales_Button.grid(row=6, column=0)

# ---------- Exit Button ----------
exit_Icon_path = "Images/exit.png"
exit_logo = ctk.CTkImage(Image.open(exit_Icon_path), size=(64, 64))
exit_Button = ctk.CTkButton(
    leftFrame,
    text=" EXIT",image=exit_logo,compound="left",
    font=("roboto condensed", 40, "bold"),
    width=400,
    height=70,
    corner_radius=0, anchor=leftFrameButtonAnchor, border_width=borderWidth, border_color="black"
)
exit_Button.grid(row=7, column=0)

# ---------- CONTENT FRAME (right side) ----------
contentFrame = ctk.CTkFrame(bodyFrame, corner_radius=0, fg_color='#1C2833')
contentFrame.pack(side="right", fill="both", expand=True)

# ---------- Employees Frame ----------
emp_Frame = ctk.CTkFrame(contentFrame, corner_radius=15, fg_color='#1A2E3B', width=400, height=300, border_width=1)
emp_Frame.place(x=70, y=70)

totalEmp_Icon_path = "Images/team.png"
totalEmp_logo = ctk.CTkImage(Image.open(totalEmp_Icon_path), size=(80, 80))

totalEmp_Label = ctk.CTkLabel(emp_Frame, text='', image=totalEmp_logo, width=400, height=80, anchor='n')
#totalEmp_Label.grid(row=0, column=0,pady=20)
totalEmp_Label.pack(pady=(30, 30))

totalEmp_Label_Text = ctk.CTkLabel(emp_Frame, text='TOTAL EMPLOYEES', font=("roboto condensed", 30, "bold"), text_color='white')
#totalEmp_Label_Text.grid(row=1, column=0,pady=1)
totalEmp_Label_Text.pack(pady=(5, 30))

totalEmp_count = ctk.CTkLabel(emp_Frame, text='120', font=("roboto condensed", 30, "bold"), text_color='cyan')
totalEmp_count.pack(pady=(5, 30))

# ---------- Supplier Frame ----------
supplier_Frame = ctk.CTkFrame(contentFrame, corner_radius=15, fg_color='#1A2E3B', width=400, height=300, border_width=1)
supplier_Frame.place(x=570, y=70)

supplier_Icon_path = "Images/suppliers.png"
supplier_logo = ctk.CTkImage(Image.open(supplier_Icon_path), size=(80, 80))

supplier_Label = ctk.CTkLabel(supplier_Frame, text='', image=supplier_logo, width=400, height=80, anchor='n')
#totalEmp_Label.grid(row=0, column=0,pady=20)
supplier_Label.pack(pady=(30, 30))

supplier_Label_Text = ctk.CTkLabel(supplier_Frame, text='TOTAL SUPPLIERS', font=("roboto condensed", 30, "bold"), text_color='white')
#totalEmp_Label_Text.grid(row=1, column=0,pady=1)
supplier_Label_Text.pack(pady=(5, 30))

supplier_count = ctk.CTkLabel(supplier_Frame, text='120', font=("roboto condensed", 30, "bold"), text_color='cyan')
supplier_count.pack(pady=(5, 30))

# ---------- Category Frame ----------
category_Frame = ctk.CTkFrame(contentFrame, corner_radius=15, fg_color='#1A2E3B', width=400, height=300, border_width=1)
category_Frame.place(x=1070, y=70)

category_Icon_path = "Images/segment.png"
category_logo = ctk.CTkImage(Image.open(category_Icon_path), size=(80, 80))

category_Label = ctk.CTkLabel(category_Frame, text='', image=category_logo, width=400, height=80, anchor='n')
#totalEmp_Label.grid(row=0, column=0,pady=20)
category_Label.pack(pady=(30, 30))

category_Label_Text = ctk.CTkLabel(category_Frame, text='TOTAL CATEGORIES', font=("roboto condensed", 30, "bold"), text_color='white')
#totalEmp_Label_Text.grid(row=1, column=0,pady=1)
category_Label_Text.pack(pady=(5, 30))

category_count = ctk.CTkLabel(category_Frame, text='120', font=("roboto condensed", 30, "bold"), text_color='cyan')
category_count.pack(pady=(5, 30))

# ---------- Products Frame ----------
Products_Frame = ctk.CTkFrame(contentFrame, corner_radius=15, fg_color='#1A2E3B', width=400, height=300, border_width=1)
Products_Frame.place(x=320, y=470)

Products_Icon_path = "Images/product.png"
Products_logo = ctk.CTkImage(Image.open(Products_Icon_path), size=(80, 80))

Products_Label = ctk.CTkLabel(Products_Frame, text='', image=Products_logo, width=400, height=80, anchor='n')
#totalEmp_Label.grid(row=0, column=0,pady=20)
Products_Label.pack(pady=(30, 30))

Products_Label_Text = ctk.CTkLabel(Products_Frame, text='TOTAL PRODUCTS', font=("roboto condensed", 30, "bold"), text_color='white')
#totalEmp_Label_Text.grid(row=1, column=0,pady=1)
Products_Label_Text.pack(pady=(5, 30))

Products_count = ctk.CTkLabel(Products_Frame, text='120', font=("roboto condensed", 30, "bold"), text_color='cyan')
Products_count.pack(pady=(5, 30))

# ---------- Sales Frame ----------
sales_Frame = ctk.CTkFrame(contentFrame, corner_radius=15, fg_color='#1A2E3B', width=400, height=300, border_width=1)
sales_Frame.place(x=820, y=470)

sales_Icon_path = "Images/salesgraph.png"
sales_logo = ctk.CTkImage(Image.open(sales_Icon_path), size=(80, 80))

sales_Label = ctk.CTkLabel(sales_Frame, text='', image=sales_logo, width=400, height=80, anchor='n')
#totalEmp_Label.grid(row=0, column=0,pady=20)
sales_Label.pack(pady=(30, 30))

sales_Label_Text = ctk.CTkLabel(sales_Frame, text='TOTAL SALES', font=("roboto condensed", 30, "bold"), text_color='white')
#totalEmp_Label_Text.grid(row=1, column=0,pady=1)
sales_Label_Text.pack(pady=(5, 30))

sales_count = ctk.CTkLabel(sales_Frame, text='120', font=("roboto condensed", 30, "bold"), text_color='cyan')
sales_count.pack(pady=(5, 30))

dashboard_window.mainloop()