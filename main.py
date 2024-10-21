import pandas as pd
import matplotlib.pyplot as plt

# Inisialisasi list untuk menyimpan gaji karyawan
salaries = []


# Fungsi untuk menghitung probabilitas karyawan dengan gaji di atas nilai tertentu
def calculate_percentage_above_threshold(threshold):
    # Menangani kasus jika list gaji kosong
    if not salaries:
        return 0

    salaries_above_threshold = [salary for salary in salaries if salary >= threshold]
    result = len(salaries_above_threshold) / len(salaries)

    # Mengubah menjadi persen
    return result * 100


# Fungsi untuk menghitung probabilitas bersyarat
def calculate_conditional_percentage(threshold1, threshold2):
    salaries_above_threshold1 = [salary for salary in salaries if salary >= threshold1]

    # Jika tidak ada karyawan dengan gaji di atas threshold1
    if not salaries_above_threshold1:
        return 0

    salaries_above_threshold2 = [
        salary for salary in salaries_above_threshold1 if salary >= threshold2
    ]

    result = len(salaries_above_threshold2) / len(salaries_above_threshold1)

    # Mengubah menjadi persen
    return result * 100


# Fungsi untuk menghitung probabilitas karyawan dengan gaji dalam rentang tertentu
def calculate_percentage_in_range(min_salary, max_salary):
    if not salaries:  # Menangani kasus jika list gaji kosong
        return 0

    if min_salary > max_salary:
        print(
            "Batas bawah rentang gaji harus lebih kecil dari batas atas rentang gaji."
        )
        return

    salaries_in_range = [
        salary for salary in salaries if min_salary <= salary <= max_salary
    ]

    result = len(salaries_in_range) / len(salaries)

    # Mengubah menjadi persen
    return result * 100


# Fungsi untuk menerima input angka valid dari pengguna
def get_valid_integer_input(prompt):
    input_value = input(prompt)

    if input_value.isdecimal():
        return int(input_value)
    else:
        None


# Fungsi untuk mengelompokkan gaji karyawan berdasarkan kategori
def classify_salary(salary, low_limit, mid_limit):
    if salary <= low_limit:
        return "Rendah"
    elif salary <= mid_limit:
        return "Menengah"
    else:
        return "Tinggi"


# Fungsi untuk menghitung dan menampilkan berbagai probabilitas serta kategori gaji
def main():
    # Meminta input jumlah karyawan
    total_employees = get_valid_integer_input("Masukkan jumlah karyawan: ")

    if total_employees is None:
        print("Jumlah karyawan tidak valid.")
        return

    # Memasukkan gaji karyawan
    for i in range(total_employees):
        order = i + 1
        salary = get_valid_integer_input(
            f"Masukkan gaji karyawan ke-{order} (jutaan rupiah): "
        )

        if salary is not None:
            salaries.append(salary)

    print("\n=== Perhitungan Persentase ===\n")

    # 1. Hitung persentase karyawan dengan gaji di atas nilai tertentu
    threshold = get_valid_integer_input("Masukkan batas gaji (jutaan rupiah): ")
    if threshold is not None:
        percentage_above = calculate_percentage_above_threshold(threshold)
        print(
            f"Persentase karyawan dengan gaji di atas {threshold} juta: {percentage_above:.2f}%"
        )
    else:
        print("Batas gaji tidak valid.")

    print()

    # 2. Hitung persentase bersyarat
    lower_threshold = get_valid_integer_input(
        "Masukkan batas bawah gaji (jutaan rupiah): "
    )
    upper_threshold = get_valid_integer_input(
        "Masukkan batas atas gaji (jutaan rupiah): "
    )

    if lower_threshold is not None and upper_threshold is not None:
        conditional_percentage = calculate_conditional_percentage(
            lower_threshold, upper_threshold
        )
        print(
            f"Persentase karyawan dengan gaji di atas {upper_threshold} juta jika diketahui di atas {lower_threshold} juta: {conditional_percentage:.2f}%"
        )
    else:
        print("Batas gaji tidak valid.")

    print()

    # 3. Hitung persentase gaji dalam rentang tertentu
    min_salary = get_valid_integer_input(
        "Masukkan batas bawah rentang gaji (jutaan rupiah): "
    )
    max_salary = get_valid_integer_input(
        "Masukkan batas atas rentang gaji (jutaan rupiah): "
    )

    if min_salary is not None and max_salary is not None:
        joint_percentage = calculate_percentage_in_range(min_salary, max_salary)
        print(
            f"Persentase karyawan dengan gaji antara {min_salary} dan {max_salary} juta: {joint_percentage:.2f}%"
        )
    else:
        print("Batas rentang gaji tidak valid.")

    # Menunggu pengguna menekan Enter sebelum menampilkan chart dan kategori
    input("\nTekan Enter untuk melihat chart...")

    # 4. Menghitung batas kategori gaji berdasarkan input karyawan
    if not salaries:
        print("Tidak ada data gaji yang dimasukkan.")
        return

    min_salary = min(salaries)
    max_salary = max(salaries)
    low_limit = round(min_salary + (max_salary - min_salary) / 3)
    mid_limit = round(min_salary + 2 * (max_salary - min_salary) / 3)

    # Menampilkan rentang kategori gaji
    low_range_label = f"Rp {0:,} - Rp {low_limit:,} juta"
    mid_range_label = f"Rp {low_limit:,} juta - Rp {mid_limit:,} juta"
    high_range_label = f"Lebih dari Rp {mid_limit:,} juta"

    print("\n=== Kategori Gaji ===")
    print(f"Gaji Rendah: {low_range_label}")
    print(f"Gaji Menengah: {mid_range_label}")
    print(f"Gaji Tinggi: {high_range_label}\n")

    # Klasifikasi gaji karyawan
    salary_categories = [
        classify_salary(salary, low_limit, mid_limit) for salary in salaries
    ]

    # Membuat DataFrame untuk menyimpan data karyawan dan kategori gaji
    df = pd.DataFrame(
        {
            "Karyawan": [f"Karyawan {i+1}" for i in range(total_employees)],
            "Gaji (Juta)": salaries,
            "Kategori": salary_categories,
        }
    )

    print("\n=== Data Gaji Karyawan ===\n")
    print(df)

    # Hitung jumlah karyawan di setiap kategori
    category_counts = (
        df["Kategori"]
        .value_counts()
        .reindex(["Rendah", "Menengah", "Tinggi"], fill_value=0)
    )

    # Menampilkan Chart
    plt.figure(figsize=(10, 6))

    # Membuat label untuk kategori dengan rentang gaji
    category_labels = [
        f"Rendah ({low_range_label})",
        f"Menengah ({mid_range_label})",
        f"Tinggi ({high_range_label})",
    ]

    plt.plot(
        category_labels,
        category_counts.values,
        marker="o",
        linestyle="-",
        color="b",
    )

    # Menambahkan judul dan label
    plt.title("Jumlah Karyawan Berdasarkan Kategori Gaji", fontsize=14)
    plt.xlabel("Kategori Gaji", fontsize=12)
    plt.ylabel("Jumlah Karyawan", fontsize=12)

    # Mengubah sumbu Y agar hanya menunjukkan bilangan bulat
    plt.gca().yaxis.set_major_locator(plt.MaxNLocator(integer=True))

    # Menampilkan grid
    plt.grid(True)

    # Menampilkan chart
    plt.show()


# Menjalankan program utama
if __name__ == "__main__":
    main()
