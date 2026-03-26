import customtkinter as ctk

class ReusableFrame(ctk.CTkFrame):
    def __init__(self, master, title="Card", fg_color="#1E90FF", layout='pack', **kwargs):
        super().__init__(
            master,
            fg_color=fg_color,
            **kwargs
        )

        # Title label
        self.title_label = ctk.CTkLabel(
            self,
            text=title,
            font=("Roboto", 20, "bold"),
            text_color="white"
        )

        if layout == "grid":
            self.title_label.grid(row=0, column=0, padx=15, pady=15)
        else:
            self.title_label.pack(padx=15, pady=15)