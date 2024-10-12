import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Function to open a file
def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"RK Text Editor - {filepath}")

# Function to save a file
def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"RK Text Editor - {filepath}")

# Function to change button color on hover
def on_hover(button, color):
    def inner(event):
        button['bg'] = color
    return inner

# Function to reset button color when hover ends
def off_hover(button, color):
    def inner(event):
        button['bg'] = color
    return inner

# Main window
window = tk.Tk()
window.title("RK Text Editor")
window.geometry("900x600")  # Set a fixed window size
window.rowconfigure(0, minsize=600, weight=1)
window.columnconfigure(1, minsize=700, weight=1)

# Text editing area
txt_edit = tk.Text(window, wrap="word", font=("Arial", 14), undo=True)
txt_edit.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

# Button frame
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2, bg="gray20")
fr_buttons.grid(row=0, column=0, sticky="ns")

# Open button with color transitions
btn_open = tk.Button(fr_buttons, text="Open", command=open_file, bg="RoyalBlue1", fg="white", font=("Arial", 12, "bold"), width=12)
btn_open.grid(row=0, column=0, padx=5, pady=10, sticky="ew")

# Save As button with color transitions
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file, bg="SpringGreen3", fg="white", font=("Arial", 12, "bold"), width=12)
btn_save.grid(row=1, column=0, padx=5, pady=10, sticky="ew")

# Add hover effects
btn_open.bind("<Enter>", on_hover(btn_open, "SteelBlue3"))
btn_open.bind("<Leave>", off_hover(btn_open, "RoyalBlue1"))

btn_save.bind("<Enter>", on_hover(btn_save, "SeaGreen3"))
btn_save.bind("<Leave>", off_hover(btn_save, "SpringGreen3"))

# Run the Tkinter loop
window.mainloop()