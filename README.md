### 🎨 Kumpulan Karya Desain Web

Repository berisi kumpulan karya mata kuliah Desain Web dan dibuat untuk praktikum Modul 10.

### 👩🏻 Identitas

| | |
| :--- | :--- |
| **Nama** | Calista Trisna Putri|
| **NIM** | K3525089 |
| **Program Studi** | Pendidikan Teknik Informatika dan Komputer |
| **Universitas** | Universitas Sebelas Maret |
| **Mata Kuliah** | Desain Web |
| **Dosen Pengampu** | Vearen Dika Sofirudin, S.pd., M.ed. |



### 🎯 Tujuan Praktikum

1. Mahasiswa mengenal teknik versioning dengan Git  
2. Mahasiswa mampu berkolaborasi dalam tim dengan Git  
3. Mahasiswa mampu mengembangkan aplikasi perangkat lunak dengan Git  



### 📔 Ringkasan Materi

Git merupakan sistem kontrol versi terdistribusi (*Distributed Version Control System*) yang digunakan untuk mencatat, melacak, dan mengelola setiap perubahan pada kode sumber (*source code*) selama proses pengembangan perangkat lunak. Dengan menggunakan Git, pengembang dapat menyimpan riwayat perubahan melalui mekanisme *commit*, bekerja secara paralel pada cabang (*branch*) yang berbeda tanpa mengganggu kode utama, serta menggabungkan hasil pekerjaan dari berbagai anggota tim secara terstruktur. Untuk mendukung kolaborasi secara daring, Git sering dipadukan dengan layanan *hosting* repositori berbasis cloud seperti GitHub, sehingga proyek dapat disimpan secara aman, diakses dari mana saja, dan didokumentasikan dengan rapi.



### 💻 Langkah Kerja

### 1. Membuat Repository di GitHub

Membuat repository baru di GitHub sebagai tempat penyimpanan remote.

### 2. Masuk ke Direktori Project

```bash
D:
cd "semester3\Desain Web\kumpulan_karya_calista"
```

### 3. Membuat Repository Lokal

```bash
git init
```

### 4. Menambahkan File ke Staging Area

```bash
git add *
```

### 5. Menyimpan Perubahan dengan Commit

```bash
git commit -m "Upload Desain Web"
```

### 6. Mengubah Nama Branch ke Main

```bash
git branch -M main
```

### 7. Menghubungkan ke Repository GitHub

```bash
git remote add origin https://github.com/calistata12/kumpulan_karya_calista_desainweb_modul10.git
```

### 8. Mengunggah (Push) ke GitHub

```bash
git push -u origin main
```



### 📋 Kesimpulan

Melalui praktikum ini, pengelolaan versi proyek menggunakan Git dan GitHub dapat diterapkan secara langsung melalui antarmuka baris perintah (*Command Line Interface*). Seluruh tahapan mulai dari inisialisasi repositori lokal, penambahan berkas ke *staging area*, pencatatan riwayat perubahan melalui *commit*, hingga pengunggahan (*push*) ke repositori *remote* berjalan dengan baik. Penerapan alur kerja Git ini mempermudah pengarsipan kumpulan karya praktikum Desain Web secara terstruktur serta menjadi fondasi penting dalam kolaborasi pengembangan perangkat lunak.
