import pandas as pd

# Membaca file CSV
data = pd.read_csv('penjualan.csv')

# Menampilkan data
print('===== DATA PENJUALAN =====')
print(data)

# Membuat kolom total
# total = harga x jumlah
data['total'] = data['harga'] * data['jumlah']

# Menampilkan data setelah ditambah kolom total
print('\n===== DATA DENGAN TOTAL =====')
print(data)

# Menghitung total semua penjualan
total_penjualan = data['total'].sum()

print('\n===== TOTAL PENJUALAN =====')
print('Rp', total_penjualan)

# Menghitung jumlah produk terjual
produk_terjual = data.groupby('produk')['jumlah'].sum()

print('\n===== JUMLAH PRODUK TERJUAL =====')
print(produk_terjual)

# Menentukan produk terlaris
produk_terlaris = produk_terjual.idxmax()

print('\n===== PRODUK TERLARIS =====')
print(produk_terlaris)
