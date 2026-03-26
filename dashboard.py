import tkinter as tk
import customtkinter as ctk
from PIL import Image


class ReusableFrame(ctk.CTkFrame):
    def __init__(self, master, title="Default Title", width=300, height=150, fg_color="#1E90FF", **kwargs):
        super().__init__(master, width=width, height=height, fg_color=fg_color, corner_radius=15, **kwargs)

        # Make the frame scalable inside its parent
        self.grid_propagate(False)  # keeps the size fixed unless you want it to stretch

        # Add a label
        self.label = ctk.CTkLabel(self, text=title, font=("Roboto", 20, "bold"), text_color="white")
        self.label.pack(padx=10, pady=10)

        # Add more widgets if needed, e.g., buttons
        self.button = ctk.CTkButton(self, text="Click Me")
        self.button.pack(pady=10)

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("themes/breeze.json")

dashboard_window = ctk.CTk()
dashboard_window.title("Dashboard")

# maximize window
dashboard_window.after(0, lambda: dashboard_window.state("zoomed"))

# ---------- HEADER FRAME ----------
header = ctk.CTkFrame(
    dashboard_window,
    fg_color="#03396C",
    height=100,
    corner_radius=0
)
header.pack(fill="x")

# allow resizing layout
header.grid_columnconfigure(0, weight=1)
header.grid_columnconfigure(1, weight=10)
header.grid_columnconfigure(2, weight=1)

# ---------- IMAGE ----------
imagePath = "Images/storage.png"
inventory_logo = ctk.CTkImage(Image.open(imagePath), size=(64, 64))

# ---------- TITLE ----------
title_label = ctk.CTkLabel(
    header,
    text="INVENTORY MANAGEMENT SYSTEM",
    padx=25,
    image=inventory_logo,
    compound="left",
    font=("roboto condensed", 50, "bold"),
    text_color="white"
)

title_label.grid(row=0, column=0, sticky="w", padx=20, pady=10)

# ---------- LOGOUT BUTTON ----------
logout_button = ctk.CTkButton(
    header,
    text="LOGOUT",
    font=("roboto condensed", 20, "bold"),
    width=150,
    height=50,
    corner_radius=25
)

logout_button.grid(row=0, column=2, sticky="e", padx=20)

dashboard_window.mainloop()