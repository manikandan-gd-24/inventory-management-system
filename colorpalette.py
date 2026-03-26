import customtkinter as ctk

# Initialize main window
root = ctk.CTk()
root.title("Professional Color Picker")
root.geometry("450x700")

# Scrollable frame for color list
scroll_frame = ctk.CTkScrollableFrame(root, width=430, height=400)
scroll_frame.pack(pady=10, padx=10, fill="both", expand=False)

# Preview frame
preview_frame = ctk.CTkFrame(root, width=430, height=150, corner_radius=10)
preview_frame.pack(pady=10, padx=10, fill="both", expand=False)

# Label to show current color name
preview_label = ctk.CTkLabel(preview_frame, text="Select a color", font=("Arial", 16))
preview_label.pack(pady=(10, 5))

# Big square showing current color
color_square = ctk.CTkLabel(preview_frame, text="", width=200, height=60, corner_radius=10)
color_square.pack(pady=5)

# Entry to show hex code
hex_entry = ctk.CTkEntry(preview_frame, width=200, font=("Arial", 14))
hex_entry.pack(pady=(5, 10))

# List of colors (name, hex)
colors = [
    ("Black", "#000000"), ("White", "#FFFFFF"), ("Red", "#FF0000"), ("Green", "#008000"),
    ("Blue", "#0000FF"), ("Yellow", "#FFFF00"), ("Cyan", "#00FFFF"), ("Magenta", "#FF00FF"),
    ("Orange", "#FFA500"), ("Pink", "#FFC0CB"), ("Purple", "#800080"), ("Gray", "#808080"),
    ("Light Gray", "#D3D3D3"), ("Dark Gray", "#A9A9A9"), ("Brown", "#A52A2A"),
    ("Sky Blue", "#87CEEB"), ("Deep Blue", "#00008B"), ("Lime Green", "#32CD32"),
    ("Tomato Red", "#FF6347"), ("Gold", "#FFD700"), ("Coral", "#FF7F50"),
    ("Accent Blue", "#1f6aa5"), ("Light Pink", "#FFB6C1"), ("Olive", "#808000"),
    ("Teal", "#008080"), ("Navy", "#000080"), ("Maroon", "#800000"), ("Silver", "#C0C0C0"),
    ("Chocolate", "#D2691E"), ("Indigo", "#4B0082"), ("Turquoise", "#40E0D0"), ("Violet", "#EE82EE")
]


# Function to determine readable text color
def get_text_color(hex_code):
    r = int(hex_code[1:3], 16)
    g = int(hex_code[3:5], 16)
    b = int(hex_code[5:7], 16)
    luminance = (0.299 * r + 0.587 * g + 0.114 * b)
    return "black" if luminance > 186 else "white"


# Update preview when a color is selected
def select_color(name, hex_code):
    # Update preview
    preview_label.configure(text=f"{name}: {hex_code}")
    color_square.configure(fg_color=hex_code)
    hex_entry.delete(0, "end")
    hex_entry.insert(0, hex_code)

    # Copy to clipboard
    root.clipboard_clear()
    root.clipboard_append(hex_code)
    root.update()
    print(f"Copied {hex_code} to clipboard")


# Add color labels to scrollable frame
for name, hex_code in colors:
    label = ctk.CTkLabel(
        scroll_frame,
        text=f"{name}: {hex_code}",
        fg_color=hex_code,
        text_color=get_text_color(hex_code),
        height=40
    )
    label.pack(pady=3, fill="x")
    label.bind("<Button-1>", lambda e, n=name, h=hex_code: select_color(n, h))

root.mainloop()