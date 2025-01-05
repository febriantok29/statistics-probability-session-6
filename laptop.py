import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from tkinter import messagebox, ttk, Tk, Frame, Label, Entry, Button, END


# Load data from Excel
def load_data():
    try:
        df = pd.read_excel("data.xlsx")
        return df
    except FileNotFoundError:
        messagebox.showerror(
            "Error",
            "File Excel tidak ditemukan. Pastikan file berada di direktori yang benar.",
        )
        return pd.DataFrame()


laptop_df = load_data()
laptop_data = laptop_df.to_dict("records")

# Extract unique values for dropdowns
company_options = laptop_df["Company"].dropna().unique().tolist()
type_options = laptop_df["Type"].dropna().unique().tolist()
os_options = laptop_df["OS"].dropna().unique().tolist()
touchscreen_options = laptop_df["Touchscreen"].dropna().unique().tolist()
ips_panel_options = laptop_df["IPS Panel"].dropna().unique().tolist()
retina_display_options = laptop_df["Retina Display"].dropna().unique().tolist()
cpu_company_options = laptop_df["CPU Company"].dropna().unique().tolist()
primary_storage_type_options = (
    laptop_df["Primary Storage Type"].dropna().unique().tolist()
)
secondary_storage_type_options = (
    laptop_df["Secondary Storage Type"].dropna().unique().tolist()
)
gpu_company_options = laptop_df["GPU Company"].dropna().unique().tolist()


# Utility functions
def clear_input_fields():
    """Clear all input fields."""
    entry_company.delete(0, END)
    entry_product.delete(0, END)
    entry_type.delete(0, END)
    entry_screen_size.delete(0, END)
    entry_ram.delete(0, END)
    entry_os.delete(0, END)
    entry_weight.delete(0, END)
    entry_price_euros.delete(0, END)
    entry_price_idr.delete(0, END)
    entry_screen.delete(0, END)
    entry_screen_width.delete(0, END)
    entry_screen_height.delete(0, END)
    entry_touchscreen.delete(0, END)
    entry_ips_panel.delete(0, END)
    entry_retina_display.delete(0, END)
    entry_cpu_company.delete(0, END)
    entry_cpu_frequency.delete(0, END)
    entry_cpu_model.delete(0, END)
    entry_primary_storage.delete(0, END)
    entry_secondary_storage.delete(0, END)
    entry_primary_storage_type.delete(0, END)
    entry_secondary_storage_type.delete(0, END)
    entry_gpu_company.delete(0, END)
    entry_gpu_model.delete(0, END)


def save_to_excel():
    """Save the in-memory data to the Excel file."""
    df = pd.DataFrame(laptop_data)
    df.to_excel("data.xlsx", index=False)


# Data operations
def add_laptop():
    """Add laptop data to the in-memory list and save to Excel."""
    new_laptop = {
        "Company": entry_company.get(),
        "Product": entry_product.get(),
        "Type": entry_type.get(),
        "Screen Size (Inches)": entry_screen_size.get(),
        "RAM (GB)": entry_ram.get(),
        "OS": entry_os.get(),
        "Weight (KG)": entry_weight.get(),
        "Price (Euros)": entry_price_euros.get(),
        "Price (IDR)": entry_price_idr.get(),
        "Screen": entry_screen.get(),
        "Screen Width (Pixels)": entry_screen_width.get(),
        "Screen Height (Pixels)": entry_screen_height.get(),
        "Touchscreen": entry_touchscreen.get(),
        "IPS Panel": entry_ips_panel.get(),
        "Retina Display": entry_retina_display.get(),
        "CPU Company": entry_cpu_company.get(),
        "CPU Frequency": entry_cpu_frequency.get(),
        "CPU Model": entry_cpu_model.get(),
        "Primary Storage (GB)": entry_primary_storage.get(),
        "Secondary Storage (GB)": entry_secondary_storage.get(),
        "Primary Storage Type": entry_primary_storage_type.get(),
        "Secondary Storage Type": entry_secondary_storage_type.get(),
        "GPU Company": entry_gpu_company.get(),
        "GPU Model": entry_gpu_model.get(),
    }

    if not all(new_laptop.values()):
        messagebox.showerror("Input Error", "Semua kolom harus diisi!")
        return

    laptop_data.append(new_laptop)
    clear_input_fields()
    messagebox.showinfo(
        "Data Ditambahkan", f"Laptop '{new_laptop['Product']}' berhasil ditambahkan!"
    )
    display_laptop_data()
    save_to_excel()


def display_laptop_data():
    """Display laptop data in the table."""
    tree.delete(*tree.get_children())
    for record in laptop_data:
        tree.insert(
            "",
            "end",
            values=(
                record["Company"],
                record["Product"],
                record["Type"],
                record["Screen Size (Inches)"],
                record["RAM (GB)"],
                record["OS"],
                record["Weight (KG)"],
                record["Price (Euros)"],
                record["Price (IDR)"],
                record["Screen"],
                record["Screen Width (Pixels)"],
                record["Screen Height (Pixels)"],
                record["Touchscreen"],
                record["IPS Panel"],
                record["Retina Display"],
                record["CPU Company"],
                record["CPU Frequency"],
                record["CPU Model"],
                record["Primary Storage (GB)"],
                record["Secondary Storage (GB)"],
                record["Primary Storage Type"],
                record["Secondary Storage Type"],
                record["GPU Company"],
                record["GPU Model"],
            ),
        )


def update_laptop():
    """Update selected laptop data and save to Excel."""
    selected_item = tree.selection()

    if not selected_item:
        messagebox.showerror("Update Error", "Pilih laptop yang ingin diperbarui!")
        return

    item = tree.item(selected_item)
    selected_product = item["values"][1]

    entry_company.delete(0, END)
    entry_company.insert(0, item["values"][0])
    entry_product.delete(0, END)
    entry_product.insert(0, selected_product)
    entry_type.delete(0, END)
    entry_type.insert(0, item["values"][2])
    entry_screen_size.delete(0, END)
    entry_screen_size.insert(0, item["values"][3])
    entry_ram.delete(0, END)
    entry_ram.insert(0, item["values"][4])
    entry_os.delete(0, END)
    entry_os.insert(0, item["values"][5])
    entry_weight.delete(0, END)
    entry_weight.insert(0, item["values"][6])
    entry_price_euros.delete(0, END)
    entry_price_euros.insert(0, item["values"][7])
    entry_price_idr.delete(0, END)
    entry_price_idr.insert(0, item["values"][8])
    entry_screen.delete(0, END)
    entry_screen.insert(0, item["values"][9])
    entry_screen_width.delete(0, END)
    entry_screen_width.insert(0, item["values"][10])
    entry_screen_height.delete(0, END)
    entry_screen_height.insert(0, item["values"][11])
    entry_touchscreen.delete(0, END)
    entry_touchscreen.insert(0, item["values"][12])
    entry_ips_panel.delete(0, END)
    entry_ips_panel.insert(0, item["values"][13])
    entry_retina_display.delete(0, END)
    entry_retina_display.insert(0, item["values"][14])
    entry_cpu_company.delete(0, END)
    entry_cpu_company.insert(0, item["values"][15])
    entry_cpu_frequency.delete(0, END)
    entry_cpu_frequency.insert(0, item["values"][16])
    entry_cpu_model.delete(0, END)
    entry_cpu_model.insert(0, item["values"][17])
    entry_primary_storage.delete(0, END)
    entry_primary_storage.insert(0, item["values"][18])
    entry_secondary_storage.delete(0, END)
    entry_secondary_storage.insert(0, item["values"][19])
    entry_primary_storage_type.delete(0, END)
    entry_primary_storage_type.insert(0, item["values"][20])
    entry_secondary_storage_type.delete(0, END)
    entry_secondary_storage_type.insert(0, item["values"][21])
    entry_gpu_company.delete(0, END)
    entry_gpu_company.insert(0, item["values"][22])
    entry_gpu_model.delete(0, END)
    entry_gpu_model.insert(0, item["values"][23])

    global laptop_data
    laptop_data = [
        record for record in laptop_data if record["Product"] != selected_product
    ]
    save_to_excel()


def delete_laptop():
    """Delete selected laptop data and save to Excel."""
    selected_item = tree.selection()

    if not selected_item:
        messagebox.showerror("Delete Error", "Pilih laptop yang ingin dihapus!")
        return

    item = tree.item(selected_item)
    selected_product = item["values"][1]

    global laptop_data
    laptop_data = [
        record for record in laptop_data if record["Product"] != selected_product
    ]
    messagebox.showinfo(
        "Delete Success", f"Laptop '{selected_product}' berhasil dihapus!"
    )
    display_laptop_data()
    save_to_excel()


def search_laptop():
    """Search and display laptop data based on the search query."""
    query = entry_search.get().lower()
    filtered_data = [
        record
        for record in laptop_data
        if any(query in str(value).lower() for value in record.values())
    ]
    
    tree.delete(*tree.get_children())
    for record in filtered_data:
        tree.insert(
            "",
            "end",
            values=tuple(record[col] for col in tree["columns"]),
        )


def perform_analysis():
    """Perform descriptive and ANOVA analysis on laptop data."""
    if not laptop_data:
        messagebox.showerror("Data Error", "Tidak ada data untuk analisis!")
        return

    df = pd.DataFrame(laptop_data)
    avg_price_by_company = df.groupby("Company")["Price (IDR)"].mean()

    grouped_data = [
        df[df["Company"] == company]["Price (IDR)"]
        for company in df["Company"].unique()
    ]

    if len(grouped_data) < 2:
        messagebox.showerror(
            "Analysis Error",
            "ANOVA membutuhkan setidaknya dua grup data. Tambahkan lebih banyak data dengan perusahaan yang berbeda!",
        )
        return

    f_stat, p_value = stats.f_oneway(*grouped_data)

    analysis_result = (
        "Perbedaan signifikan dalam harga berdasarkan perusahaan."
        if p_value < 0.05
        else "Tidak ada perbedaan signifikan dalam harga berdasarkan perusahaan."
    )

    avg_price_by_company_formatted = avg_price_by_company.apply(
        lambda x: f"Rp {x:,.2f}"
    )

    messagebox.showinfo(
        "Hasil Analisis",
        f"Rata-rata Harga berdasarkan Perusahaan:\n{avg_price_by_company_formatted}\n\n"
        f"Hasil ANOVA:\nF-statistik: {f_stat:.2f}, p-value: {p_value:.4f}\n\n{analysis_result}",
    )

    _, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

    avg_price_by_company.plot(kind="bar", color="skyblue", ax=axes[0])
    axes[0].set_title("Rata-rata Harga berdasarkan Perusahaan")
    axes[0].set_xlabel("Perusahaan")
    axes[0].set_ylabel("Rata-rata Harga (IDR)")
    axes[0].tick_params(axis="x", rotation=45)
    axes[0].grid(axis="y")
    axes[0].get_yaxis().get_major_formatter().set_scientific(False)
    axes[0].get_yaxis().set_major_formatter(
        plt.FuncFormatter(lambda x, _: f"Rp {x:,.0f}")
    )

    axes[1].scatter(df["RAM (GB)"], df["Price (IDR)"], alpha=0.6, color="green")
    axes[1].set_title("Hubungan antara RAM dan Harga")
    axes[1].set_xlabel("RAM (GB)")
    axes[1].set_ylabel("Harga (IDR)")
    axes[1].grid(True)
    axes[1].get_yaxis().get_major_formatter().set_scientific(False)
    axes[1].get_yaxis().set_major_formatter(
        plt.FuncFormatter(lambda x, _: f"Rp {x:,.0f}")
    )

    plt.tight_layout()
    plt.show()


def sort_column(tree, col, reverse):
    """Sort the table by the given column."""
    data = [(tree.set(child, col), child) for child in tree.get_children("")]

    # Try to convert data to float for numeric sorting
    try:
        data.sort(
            key=lambda t: float(t[0].replace("Rp ", "").replace(",", "")),
            reverse=reverse,
        )
    except ValueError:
        data.sort(reverse=reverse)

    for index, (_, child) in enumerate(data):
        tree.move(child, "", index)

    tree.heading(col, command=lambda: sort_column(tree, col, not reverse))


# GUI setup
root = Tk()
root.title("Manajemen Katalog Laptop")

frame_input = Frame(root)
frame_input.pack(pady=20)

Label(frame_input, text="Perusahaan:").grid(row=0, column=0, padx=10, pady=5)
entry_company = ttk.Combobox(frame_input, values=company_options)
entry_company.grid(row=0, column=1, padx=10, pady=5)

Label(frame_input, text="Produk:").grid(row=0, column=2, padx=10, pady=5)
entry_product = Entry(frame_input)
entry_product.grid(row=0, column=3, padx=10, pady=5)

Label(frame_input, text="Tipe:").grid(row=0, column=4, padx=10, pady=5)
entry_type = ttk.Combobox(frame_input, values=type_options)
entry_type.grid(row=0, column=5, padx=10, pady=5)

Label(frame_input, text="Ukuran Layar (Inci):").grid(row=1, column=0, padx=10, pady=5)
entry_screen_size = Entry(frame_input)
entry_screen_size.grid(row=1, column=1, padx=10, pady=5)

Label(frame_input, text="RAM (GB):").grid(row=1, column=2, padx=10, pady=5)
entry_ram = Entry(frame_input)
entry_ram.grid(row=1, column=3, padx=10, pady=5)

Label(frame_input, text="OS:").grid(row=1, column=4, padx=10, pady=5)
entry_os = ttk.Combobox(frame_input, values=os_options)
entry_os.grid(row=1, column=5, padx=10, pady=5)

Label(frame_input, text="Berat (KG):").grid(row=2, column=0, padx=10, pady=5)
entry_weight = Entry(frame_input)
entry_weight.grid(row=2, column=1, padx=10, pady=5)

Label(frame_input, text="Harga (Euro):").grid(row=2, column=2, padx=10, pady=5)
entry_price_euros = Entry(frame_input)
entry_price_euros.grid(row=2, column=3, padx=10, pady=5)

Label(frame_input, text="Harga (IDR):").grid(row=2, column=4, padx=10, pady=5)
entry_price_idr = Entry(frame_input)
entry_price_idr.grid(row=2, column=5, padx=10, pady=5)

Label(frame_input, text="Layar:").grid(row=3, column=0, padx=10, pady=5)
entry_screen = Entry(frame_input)
entry_screen.grid(row=3, column=1, padx=10, pady=5)

Label(frame_input, text="Lebar Layar (Piksel):").grid(row=3, column=2, padx=10, pady=5)
entry_screen_width = Entry(frame_input)
entry_screen_width.grid(row=3, column=3, padx=10, pady=5)

Label(frame_input, text="Tinggi Layar (Piksel):").grid(row=3, column=4, padx=10, pady=5)
entry_screen_height = Entry(frame_input)
entry_screen_height.grid(row=3, column=5, padx=10, pady=5)

Label(frame_input, text="Layar Sentuh:").grid(row=4, column=0, padx=10, pady=5)
entry_touchscreen = ttk.Combobox(frame_input, values=touchscreen_options)
entry_touchscreen.grid(row=4, column=1, padx=10, pady=5)

Label(frame_input, text="Panel IPS:").grid(row=4, column=2, padx=10, pady=5)
entry_ips_panel = ttk.Combobox(frame_input, values=ips_panel_options)
entry_ips_panel.grid(row=4, column=3, padx=10, pady=5)

Label(frame_input, text="Layar Retina:").grid(row=4, column=4, padx=10, pady=5)
entry_retina_display = ttk.Combobox(frame_input, values=retina_display_options)
entry_retina_display.grid(row=4, column=5, padx=10, pady=5)

Label(frame_input, text="Perusahaan CPU:").grid(row=5, column=0, padx=10, pady=5)
entry_cpu_company = ttk.Combobox(frame_input, values=cpu_company_options)
entry_cpu_company.grid(row=5, column=1, padx=10, pady=5)

Label(frame_input, text="Frekuensi CPU:").grid(row=5, column=2, padx=10, pady=5)
entry_cpu_frequency = Entry(frame_input)
entry_cpu_frequency.grid(row=5, column=3, padx=10, pady=5)

Label(frame_input, text="Model CPU:").grid(row=5, column=4, padx=10, pady=5)
entry_cpu_model = Entry(frame_input)
entry_cpu_model.grid(row=5, column=5, padx=10, pady=5)

Label(frame_input, text="Penyimpanan Utama (GB):").grid(
    row=6, column=0, padx=10, pady=5
)
entry_primary_storage = Entry(frame_input)
entry_primary_storage.grid(row=6, column=1, padx=10, pady=5)

Label(frame_input, text="Penyimpanan Sekunder (GB):").grid(
    row=6, column=2, padx=10, pady=5
)
entry_secondary_storage = Entry(frame_input)
entry_secondary_storage.grid(row=6, column=3, padx=10, pady=5)

Label(frame_input, text="Tipe Penyimpanan Utama:").grid(
    row=6, column=4, padx=10, pady=5
)
entry_primary_storage_type = ttk.Combobox(
    frame_input, values=primary_storage_type_options
)
entry_primary_storage_type.grid(row=6, column=5, padx=10, pady=5)

Label(frame_input, text="Tipe Penyimpanan Sekunder:").grid(
    row=7, column=0, padx=10, pady=5
)
entry_secondary_storage_type = ttk.Combobox(
    frame_input, values=secondary_storage_type_options
)
entry_secondary_storage_type.grid(row=7, column=1, padx=10, pady=5)

Label(frame_input, text="Perusahaan GPU:").grid(row=7, column=2, padx=10, pady=5)
entry_gpu_company = ttk.Combobox(frame_input, values=gpu_company_options)
entry_gpu_company.grid(row=7, column=3, padx=10, pady=5)

Label(frame_input, text="Model GPU:").grid(row=7, column=4, padx=10, pady=5)
entry_gpu_model = Entry(frame_input)
entry_gpu_model.grid(row=7, column=5, padx=10, pady=5)

# Search field
frame_search = Frame(root)
frame_search.pack(pady=10)

Label(frame_search, text="Cari:").pack(side="left", padx=10)
entry_search = Entry(frame_search)
entry_search.pack(side="left", padx=10)
Button(frame_search, text="Cari", command=search_laptop).pack(side="left", padx=10)

# Buttons in a horizontal layout
frame_buttons = Frame(root)
frame_buttons.pack(pady=10)

Button(frame_buttons, text="Tambah Laptop", command=add_laptop).pack(
    side="left", padx=5
)
Button(frame_buttons, text="Perbarui Laptop", command=update_laptop).pack(
    side="left", padx=5
)
Button(frame_buttons, text="Hapus Laptop", command=delete_laptop).pack(
    side="left", padx=5
)
Button(frame_buttons, text="Analisis Data", command=perform_analysis).pack(
    side="left", padx=5
)

# Data table with scrollbars
frame_table = Frame(root)
frame_table.pack(pady=20)

# Create a Treeview with scrollbars
columns = (
    "Company",
    "Product",
    "Type",
    "Screen Size (Inches)",
    "RAM (GB)",
    "OS",
    "Weight (KG)",
    "Price (Euros)",
    "Price (IDR)",
    "Screen",
    "Screen Width (Pixels)",
    "Screen Height (Pixels)",
    "Touchscreen",
    "IPS Panel",
    "Retina Display",
    "CPU Company",
    "CPU Frequency",
    "CPU Model",
    "Primary Storage (GB)",
    "Secondary Storage (GB)",
    "Primary Storage Type",
    "Secondary Storage Type",
    "GPU Company",
    "GPU Model",
)

tree = ttk.Treeview(frame_table, columns=columns, show="headings")

# Add horizontal scrollbar
h_scroll = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)
h_scroll.pack(side="bottom", fill="x")
tree.configure(xscrollcommand=h_scroll.set)

# Add vertical scrollbar
v_scroll = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
v_scroll.pack(side="right", fill="y")
tree.configure(yscrollcommand=v_scroll.set)

# Configure treeview columns
for col in columns:
    tree.heading(col, text=col, command=lambda _col=col: sort_column(tree, _col, False))
    tree.column(col, anchor="center", width=120)  # Set a default width for each column

tree.pack()

# Display initial data
display_laptop_data()

# Run the application
root.mainloop()
