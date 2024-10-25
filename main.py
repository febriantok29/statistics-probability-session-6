import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import chi2_contingency

plt.tight_layout()

# Uji `T` Satu Sampel
print("Uji T Satu Sampel")
data = [45, 47, 49, 52, 50, 48, 47, 51]

t_statistic, p_value = stats.ttest_1samp(data, 50)

print(f"Nilai statistik t: {t_statistic}")
print(f"Nilai p-value: {p_value}")

alpha = 0.05
if p_value < alpha:
    print("H0 ditolak, Rata-rata berbeda secara signifikan dari 50")
else:
    print("H0 diterima, Rata-rata sama dengan 50")

# Buat Diagram Garis Dari Uji T Satu Sampel
x_single_sample = np.arange(1, len(data) + 1)
plt.plot(
    x_single_sample,
    data,
    marker="o",
    linestyle="-",
    color="b",
    label="Data Satu Sampel",
)
plt.axhline(y=50, color="r", linestyle="--", label="Rata-rata 50")
plt.title("Uji T Satu Sampel")
plt.xlabel("Pengamatan")
plt.ylabel("Nilai")
plt.grid(True)
plt.legend()
plt.show()
print("--- End of Uji T Satu Sampel ---")

# Uji `T` Dua Sampel
print("Uji T Dua Sampel")
first_data = [50, 52, 54, 48, 49, 51]
second_data = [45, 47, 46, 44, 48, 47]

t_statistic, p_value = stats.ttest_ind(first_data, second_data)

print(f"Nilai statistik t: {t_statistic}")
print(f"Nilai p-value: {p_value}")

if p_value < alpha:
    print("H0 ditolak, Rata-rata dua kelompok berbeda secara signifikan")
else:
    print("H0 diterima, Rata-rata dua kelompok sama")

# Buat Diagram Garis Dari Uji T Dua Sampel
x_two_sample = np.arange(1, len(first_data) + 1)
plt.plot(
    x_two_sample, first_data, marker="o", linestyle="-", color="g", label="Kelompok 1"
)
plt.plot(
    x_two_sample, second_data, marker="o", linestyle="-", color="m", label="Kelompok 2"
)
plt.axhline(y=50, color="r", linestyle="--", label="Rata-rata 50")
plt.title("Uji T Dua Sampel")
plt.xlabel("Pengamatan")
plt.ylabel("Nilai")
plt.grid(True)
plt.legend()
plt.show()
print("-- End of Uji T Dua Sampel --")

# Uji Chi-Square
print("Uji Chi-Square")
first_data = [10, 10, 20]
second_data = [20, 20, 30]

observed = np.array([first_data, second_data])

chi2, p, _, __ = chi2_contingency(observed)

print(f"Nilai Chi-Square: {chi2}")
print(f"Nilai p-value: {p}")

if p < alpha:
    print("H0 ditolak, Ada hubungan signifikan antara variabel")
else:
    print("H0 diterima, Tidak ada hubungan antara variabel")

# Buat Diagram Garis Dari Uji Chi-Square
categories = ["Kategori 1", "Kategori 2", "Kategori 3"]
x_categories = np.arange(1, len(categories) + 1)

plt.plot(
    x_categories, observed[0], marker="o", linestyle="-", color="c", label="Kelompok 1"
)
plt.plot(
    x_categories, observed[1], marker="o", linestyle="-", color="y", label="Kelompok 2"
)

plt.xlabel("Kategori")
plt.ylabel("Frekuensi")
plt.title("Uji Chi-Square")
plt.grid(True)
plt.xticks(x_categories, categories)
plt.legend()
plt.show()

print("-- End of Uji Chi-Square --")
