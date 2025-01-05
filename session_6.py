import pandas as pd
import tkinter as tk
from tkinter import ttk


master = pd.read_excel("laptop_prices.xlsx")

master.info()

root = tk.Tk()
root.title("Analisa Gaji Karyawan")
root.geometry("800x400")

# Labels
tk.Label(root, text="Nama:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="Divisi:").grid(row=1, column=0, padx=5, pady=5)
tk.Label(root, text="Gaji (Juta):").grid(row=2, column=0, padx=5, pady=5)
tk.Label(root, text="Jabatan:").grid(row=3, column=0, padx=5, pady=5)
tk.Label(root, text="Lama Bekerja (tahun):").grid(row=4, column=0, padx=5, pady=5)
tk.Label(root, text="Jenis Kelamin (L/P):").grid(row=5, column=0, padx=5, pady=5)

# Entry Fields
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

division_combo = ttk.Combobox(root, values=["Finance", "HR", "IT", "Marketing"])
division_combo.grid(row=1, column=1, padx=5, pady=5)

salary_entry = tk.Entry(root)
salary_entry.grid(row=2, column=1, padx=5, pady=5)

position_combo = ttk.Combobox(root, values=["Staf", "Manager", "Supervisor"])
position_combo.grid(row=3, column=1, padx=5, pady=5)

work_years_entry = tk.Entry(root)
work_years_entry.grid(row=4, column=1, padx=5, pady=5)

gender_entry = tk.Entry(root)
gender_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Button(root, text="Tambah Data").grid(row=6, column=0, padx=5, pady=5)
tk.Button(root, text="Perbarui Data").grid(row=6, column=1, padx=5, pady=5)
tk.Button(root, text="Hapus Data").grid(row=6, column=2, padx=5, pady=5)

columns = ("Nama", "Divisi", "Gaji", "Jabatan", "Lama_Bekerja", "Jenis_Kelamin")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

tk.Button(root, text="Visualisasi Data").grid(row=8, column=0, padx=5, pady=5)
tk.Button(root, text="Hitung Probabilitas").grid(row=8, column=1, padx=5, pady=5)
tk.Button(root, text="Uji Hipotesis").grid(row=8, column=2, padx=5, pady=5)

root.mainloop()
