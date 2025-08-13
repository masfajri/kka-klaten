# 1. fungsi tanpa parameter
def salam():
    """Mengembalikan sebuah pesan sapaan standar."""
    return  "Halo, selamat datang di fungsi!"
# 2. fungsi dengan parameter
def sapa(nama):
    """Mengembalikan pesan sapaan yang tercantum nama pengguna parameter: nama (str) : nama
    pengguna yang ingin di sapa"""
    return "Halo, " + nama + "!"
# 3. pemanggilan fungsi
print(salam())  # Memanggil fungsi tanpa parameter
hasil = (sapa("Data Scientist"))  # Memanggil fungsi dengan parameter
print(hasil)  # Menampilkan hasil dari pemanggilan fungsi dengan parameter