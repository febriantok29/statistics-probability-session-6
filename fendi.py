import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load initial data from Excel
try:
    data_laptop = pd.read_excel("./data.xlsx")
    data_laptop = data_laptop[
        [
            "Company",
            "Product",
            "CPU Company",
            "RAM (GB)",
            "Primary Storage (GB)",
            "Price (IDR)",
        ]
    ]
    data_laptop.columns = ["Company", "Product", "CPU", "RAM", "Storage", "Price"]
except FileNotFoundError:
    messagebox.showerror(
        "Error",
        "File Excel tidak ditemukan. Pastikan file berada di direktori yang benar.",
    )
    data_laptop = pd.DataFrame(
        columns=["Company", "Product", "CPU", "RAM", "Storage", "Price"]
    )


def add_data():
    global data_laptop
    company = company_var.get()
    product = product_entry.get()
    cpu = cpu_var.get()
    ram = ram_entry.get()
    storage = storage_entry.get()
    price = price_entry.get()

    if (
        not product
        or not ram.isnumeric()
        or not storage.isnumeric()
        or not price.isnumeric()
    ):
        messagebox.showerror(
            "Gagal Input", "Mohon isi semua kolom dengan benar sesuai format."
        )
        return

    new_data = pd.DataFrame(
        {
            "Company": [company],
            "Product": [product],
            "CPU": [cpu],
            "RAM": [int(ram)],
            "Storage": [int(storage)],
            "Price": [int(price)],
        }
    )

    data_laptop = pd.concat([data_laptop, new_data], ignore_index=True)
    update_table()
    clear_inputs()


def edit_data():
    try:
        selected_item = tree.selection()[0]
        index = tree.index(selected_item)

        data_laptop.loc[index, "Company"] = company_var.get()
        data_laptop.loc[index, "Product"] = product_entry.get()
        data_laptop.loc[index, "CPU"] = cpu_var.get()
        data_laptop.loc[index, "RAM"] = int(ram_entry.get())
        data_laptop.loc[index, "Storage"] = int(storage_entry.get())
        data_laptop.loc[index, "Price"] = int(price_entry.get())

        update_table()
        clear_inputs()
    except IndexError:
        messagebox.showerror("Gagal Edit", "Mohon pilih data yang ingin diubah.")


def delete_data():
    try:
        selected_item = tree.selection()[0]
        index = tree.index(selected_item)

        if messagebox.askyesno(
            "Konfirmasi Hapus", "Apakah Anda yakin ingin menghapus data ini?"
        ):
            data_laptop.drop(index, inplace=True)
            data_laptop.reset_index(drop=True, inplace=True)
            update_table()
            clear_inputs()
    except IndexError:
        messagebox.showerror("Gagal Hapus", "Mohon pilih data yang ingin dihapus.")


def update_table():
    for row in tree.get_children():
        tree.delete(row)
    for index, row in data_laptop.iterrows():
        tree.insert("", "end", values=list(row))


def clear_inputs():
    product_entry.delete(0, tk.END)
    ram_entry.delete(0, tk.END)
    storage_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)


def calculate_probability():
    try:
        x = prob_price_entry.get()
        ram_val = ram_cdf_entry.get()

        if not x or not ram_val:
            messagebox.showerror(
                "Gagal Input", "Mohon masukkan nilai untuk Harga dan RAM."
            )
            return

        x = float(x)
        ram_val = int(ram_val)

        prob_greater = (data_laptop["Price"] > x).mean()

        ram_cdf = stats.rv_discrete(
            values=(
                data_laptop["RAM"].unique(),
                [(data_laptop["RAM"] == r).mean() for r in data_laptop["RAM"].unique()],
            )
        )

        prob_ram_cdf = ram_cdf.cdf(ram_val)

        messagebox.showinfo(
            "Hasil Perhitungan Probabilitas",
            f"Probabilitas Harga > {x}: {prob_greater:.2f}\n"
            f"Nilai Fungsi Distribusi Kumulatif RAM: {prob_ram_cdf:.2f}",
        )
    except ValueError:
        messagebox.showerror(
            "Gagal Input", "Mohon masukkan nilai numerik untuk Harga dan RAM."
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))


def hypothesis_testing():
    # try:
    #     x = float(hypothesis_price_entry.get())
    #     t_stat, p_value = stats.ttest_1samp(data_laptop["Price"], x)

    #     result_label.config(text=f"T-test: t_stat={t_stat:.2f}, p_value={p_value:.2f}")
    # except Exception as e:
    #     messagebox.showerror("Gagal Uji Hipotesis", str(e))

    try:
        # Mengkonversi kolom Harga menjadi numerik
        data_laptop["Price"] = pd.to_numeric(data_laptop["Price"], errors="coerce")
        data_laptop.dropna(subset=["Price"], inplace=True)

        # Mendapatkan nilai dari entry
        test_value = float(hypothesis_price_entry.get())

        # Menghitung rata-rata, deviasi standar, dan ukuran sampel
        mean_price = data_laptop["Price"].mean()
        std_dev_price = data_laptop["Price"].std()
        sample_size = data_laptop["Price"].count()

        # Menghitung statistik uji t
        t_stat = (mean_price - test_value) / (std_dev_price / (sample_size**0.5))

        # Menghitung p-value
        p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=sample_size - 1))

        # Menampilkan hasil dalam popup
        result_message = (
            f"Hasil Uji Hipotesis:\n"
            f"Rata-rata Sampel: {mean_price:.2f}\n"
            f"Statistik t: {t_stat:.2f}\n"
            f"Nilai p: {p_value:.2f}\n"
        )

        # Menentukan apakah menolak H0
        alpha = 0.05
        if p_value < alpha:
            result_message += "Kesimpulan: Tolak H0 (ada bukti yang cukup untuk menyatakan bahwa rata-rata harga berbeda dari nilai hipotesis)."
        else:
            result_message += "Kesimpulan: Gagal menolak H0 (tidak ada bukti yang cukup untuk menyatakan bahwa rata-rata harga berbeda dari nilai hipotesis)."

        messagebox.showinfo("Hasil Uji Hipotesis", result_message)

    except ValueError:
        messagebox.showerror(
            "Kesalahan Input", "Silakan masukkan nilai yang valid untuk Harga."
        )
    except Exception as e:
        messagebox.showerror("Kesalahan", str(e))


def visualize_data():
    plt.figure(figsize=(14, 6))

    plt.subplot(1, 2, 1)
    plt.hist(data_laptop["Price"], bins=20, color="skyblue", edgecolor="black")
    plt.title("Distribusi Harga Laptop")
    plt.xlabel("Harga (IDR)")
    plt.ylabel("Jumlah Laptop")
    plt.grid(axis="y")
    plt.gca().get_xaxis().get_major_formatter().set_scientific(
        False
    )  # Disable scientific notation

    plt.subplot(1, 2, 2)
    plt.scatter(data_laptop["RAM"], data_laptop["Price"], alpha=0.6, color="green")
    plt.title("Hubungan RAM dengan Harga Laptop")
    plt.xlabel("RAM")
    plt.ylabel("Harga (IDR)")
    plt.gca().get_yaxis().get_major_formatter().set_scientific(
        False
    )  # Disable scientific notation

    plt.tight_layout()
    plt.show()


# Tkinter GUI setup
app = tk.Tk()
app.title("Laptop Data Analysis")

company_var = tk.StringVar()
cpu_var = tk.StringVar()

company_label = tk.Label(app, text="Perusahaan:", anchor="w")
company_label.grid(row=0, column=0, sticky="ew", padx=(5, 0))
company_menu = ttk.Combobox(
    app,
    textvariable=company_var,
    values=["Acer", "Asus", "Dell", "HP", "Lenovo", "MSI"],
)
company_menu.grid(row=0, column=1, sticky="ew")

product_label = tk.Label(app, text="Produk:", anchor="w")
product_label.grid(row=1, column=0, sticky="ew", padx=(5, 0))
product_entry = tk.Entry(app, justify="left")
product_entry.grid(row=1, column=1, sticky="ew")

cpu_label = tk.Label(app, text="CPU:", anchor="w")
cpu_label.grid(row=2, column=0, sticky="ew", padx=(5, 0))
cpu_menu = ttk.Combobox(app, textvariable=cpu_var, values=["Intel", "AMD"])
cpu_menu.grid(row=2, column=1, sticky="ew")

ram_label = tk.Label(app, text="RAM (GB):", anchor="w")
ram_label.grid(row=3, column=0, sticky="ew", padx=(5, 0))
ram_entry = tk.Entry(app, justify="left")
ram_entry.grid(row=3, column=1, sticky="ew")

storage_label = tk.Label(app, text="Penyimpanan (GB):", anchor="w")
storage_label.grid(row=4, column=0, sticky="ew", padx=(5, 0))
storage_entry = tk.Entry(app, justify="left")
storage_entry.grid(row=4, column=1, sticky="ew")

price_label = tk.Label(app, text="Harga (IDR):", anchor="w")
price_label.grid(row=5, column=0, sticky="ew", padx=(5, 0))
price_entry = tk.Entry(app, justify="left")
price_entry.grid(row=5, column=1, sticky="ew")

add_button = tk.Button(app, text="Tambah Data", command=add_data)
add_button.grid(row=6, column=0, padx=5, pady=5)

edit_button = tk.Button(app, text="Perbarui Data", command=edit_data)
edit_button.grid(row=6, column=1, padx=5, pady=5)

delete_button = tk.Button(app, text="Hapus Data", command=delete_data)
delete_button.grid(row=6, column=2, padx=5, pady=5)

columns = ("Company", "Product", "CPU", "RAM", "Storage", "Price")
tree = ttk.Treeview(app, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=100)

tree.grid(row=7, columnspan=3)

menu_frame = tk.Frame(app)
menu_frame.grid(row=8, columnspan=3, pady=(10, 10))

probability_button = tk.Button(
    menu_frame, text="Hitung Probabilitas", command=lambda: show_menu("probability")
)
probability_button.pack(side=tk.LEFT, padx=10)

hypothesis_button = tk.Button(
    menu_frame, text="Uji Hipotesis", command=lambda: show_menu("hypothesis")
)
hypothesis_button.pack(side=tk.LEFT, padx=10)

visualize_button = tk.Button(
    menu_frame, text="Visualisasi Data", command=visualize_data
)
visualize_button.pack(side=tk.LEFT, padx=10)

input_frame = tk.Frame(app)
input_frame.grid(row=9, columnspan=3)

prob_label = tk.Label(
    input_frame, text="Harga untuk Menghitung Probabilitas:", anchor="w"
)
prob_price_entry = tk.Entry(input_frame, justify="left")

ram_cdf_label = tk.Label(
    input_frame, text="RAM untuk Fungsi Distribusi Kumulatif:", anchor="w"
)
ram_cdf_entry = tk.Entry(input_frame, justify="left")

prob_button = tk.Button(
    input_frame, text="Hitung Probabilitas", command=calculate_probability
)

hypothesis_label = tk.Label(
    input_frame, text="Masukan Harga untuk Uji Hipotesis:", anchor="w"
)
hypothesis_price_entry = tk.Entry(input_frame, justify="left")
hypothesis_button = tk.Button(
    input_frame, text="Hasil Uji Hipotesis", command=hypothesis_testing
)
result_label = tk.Label(input_frame, text="", anchor="center")


def show_menu(menu):
    for widget in input_frame.winfo_children():
        widget.grid_forget()

    if menu == "probability":
        prob_label.grid(row=0, column=0)
        prob_price_entry.grid(row=0, column=1)

        ram_cdf_label.grid(row=1, column=0)
        ram_cdf_entry.grid(row=1, column=1)

        prob_button.grid(row=2, columnspan=2)

    elif menu == "hypothesis":
        hypothesis_label.grid(row=0, column=0)
        hypothesis_price_entry.grid(row=0, column=1)
        hypothesis_button.grid(row=1, columnspan=2)
        result_label.grid(row=2, columnspan=2)


# Pastikan tabel diperbarui setelah semua widget diatur
update_table()

app.mainloop()
