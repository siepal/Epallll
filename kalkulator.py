import tkinter as tk

def klik(tombol):
    if tombol == "=":
        try:
            ekspresi = entry.get()
            if '+' in ekspresi:
                entry.delete(0, tk.END)
                entry.insert(tk.END, "i love you")
            else:
                hasil = str(eval(ekspresi))
                entry.delete(0, tk.END)
                entry.insert(tk.END, hasil)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif tombol == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, tombol)

# Jendela utama
root = tk.Tk()
root.title("Mini Kalkulator")

# Ukuran jendela (lebar x tinggi)
window_width = 250
window_height = 300

# Dapatkan ukuran layar
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Hitung posisi tengah
x_pos = (screen_width // 2) - (window_width // 2)
y_pos = (screen_height // 2) - (window_height // 2)

# Set posisi jendela ke tengah
root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")
root.resizable(False, False)  # Nonaktifkan resize

# Entry (layar kalkulator)
entry = tk.Entry(root, width=18, font=('Arial', 14), bd=5, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Tombol-tombol
tombol_list = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0
for tombol in tombol_list:
    cmd = lambda x=tombol: klik(x)
    tk.Button(
        root,
        text=tombol,
        width=4,
        height=1,
        font=('Arial', 14),
        command=cmd
    ).grid(row=row_val, column=col_val, padx=3, pady=3)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Jalankan
root.mainloop()
