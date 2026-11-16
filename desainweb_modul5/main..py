import numpy as np
import pandas as pd

# 1. Baca File CSV Kotor
df = pd.read_csv("dirty_cafe_sales.csv")
jumlah_baris_awal = len(df)

# Rapikan spasi berlebih pada teks di seluruh kolom
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].astype(str).str.strip()

# 2. DAFTAR ANOMALI TEKS: Daftar kata sampah yang akan di-flag
daftar_anomali = [
    "ERROR",
    "error",
    "Error",
    "Unknown",
    "unknown",
    "UNKNOWN",
    "N/A",
    "n/a",
    "-",
    "nan",
    "NaN",
    "null",
    "NULL",
    "",
]

# Ubah semua teks anomali di SELURUH KOLOM menjadi NaN (kosong)
df_clean = df.replace(daftar_anomali, np.nan)

# 3. VALIDASI TANGGAL: Jika format tanggal anomali/salah -> ubah jadi NaT (kosong)
df_clean["Transaction Date"] = pd.to_datetime(
    df_clean["Transaction Date"], errors="coerce"
)

# 4. VALIDASI ANGKA: Jika kolom harga/quantity berisi teks anomali -> ubah jadi NaN (kosong)
kolom_numerik = [
    col
    for col in ["Quantity", "Price Per Unit", "Total Spent"]
    if col in df_clean.columns
]
for col in kolom_numerik:
    df_clean[col] = pd.to_numeric(df_clean[col], errors="coerce")

# 5. HAPUS FULL BARIS (HORIZONTAL / AXIS = 0)
# how='any' artinya jika ADA SATU SAJA kolom yang berisi anomali/NaN, HAPUS 1 BARIS UTUH.
df_clean = df_clean.dropna(how="any", axis=0).copy()

# 6. EKSPOR FILE HASIL CLEANING (Excel & CSV)
df_export = df_clean.copy()
df_export["Transaction Date"] = df_export["Transaction Date"].dt.strftime(
    "%Y-%m-%d"
)

df_export.to_excel("clean_cafe_sales.xlsx", index=False)
df_export.to_csv("clean_cafe_sales.csv", index=False)

jumlah_baris_bersih = len(df_clean)
baris_terbuang = jumlah_baris_awal - jumlah_baris_bersih

# 7. OLAH DATA UNTUK MANAJER
df_clean["Bulan"] = df_clean["Transaction Date"].dt.strftime("%Y-%m (%B)")
df_clean["Hari"] = df_clean["Transaction Date"].dt.day_name()

print("=" * 65)
print("PEMBERSIHAN TOTAL (ROW DROPPED HORIZONTALLY) BERHASIL!")
print("=" * 65)
print(f"✔ Total data awal               : {jumlah_baris_awal} baris")
print(
    f"✖ Total baris anomali dibuang   : {baris_terbuang} baris (Full 1 row terhapus)"
)
print(f"✔ Total data bersih tersisa     : {jumlah_baris_bersih} baris")
print("-" * 65)
print("📁 File Excel bersih tersimpan  : 'clean_cafe_sales.xlsx'")
print("📁 File CSV bersih tersimpan    : 'clean_cafe_sales.csv'")
print("=" * 65)

# ---------------------------------------------------------
# HASIL RINGKASAN MANAJER
# ---------------------------------------------------------
rekap_menu = (
    df_clean.groupby("Item")
    .agg(Total_Omzet=("Total Spent", "sum"), Porsi_Terjual=("Quantity", "sum"))
    .reset_index()
)
top_omzet = rekap_menu.sort_values(by="Total_Omzet", ascending=False).iloc[0]
top_porsi = rekap_menu.sort_values(by="Porsi_Terjual", ascending=False).iloc[0]

rekap_bulan = (
    df_clean.groupby("Bulan")
    .agg(Jumlah_Transaksi=("Transaction ID", "count"))
    .sort_values(by="Jumlah_Transaksi", ascending=False)
)
rekap_hari = (
    df_clean.groupby("Hari")
    .agg(Jumlah_Transaksi=("Transaction ID", "count"))
    .sort_values(by="Jumlah_Transaksi", ascending=False)
)

top_payment = df_clean["Payment Method"].value_counts().idxmax()
top_payment_count = df_clean["Payment Method"].value_counts().max()
top_location = df_clean["Location"].value_counts().idxmax()
top_location_count = df_clean["Location"].value_counts().max()

print("\n[ RINGKASAN JAWABAN MANAJER ]")
print(
    f"1. Menu Omzet Terbesar  : {top_omzet['Item']} (${top_omzet['Total_Omzet']:,.2f})"
)
print(
    f"   Menu Porsi Terbanyak : {top_porsi['Item']} ({int(top_porsi['Porsi_Terjual'])} porsi)"
)
print(
    f"2. Bulan Paling Ramai   : {rekap_bulan.index[0]} ({rekap_bulan.iloc[0]['Jumlah_Transaksi']} transaksi)"
)
print(
    f"   Hari Paling Ramai    : {rekap_hari.index[0]} ({rekap_hari.iloc[0]['Jumlah_Transaksi']} transaksi)"
)
print(
    f"3. Metode Bayar Favorit : {top_payment} ({top_payment_count} transaksi)"
)
print(
    f"   Lokasi Favorit       : {top_location} ({top_location_count} transaksi)"
)
print("=" * 65)