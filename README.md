## Facebook Auto Post & Scheduler

Aplikasi web sederhana yang dibangun dengan Python dan Flask untuk memposting status ke Halaman (Fan Page) Facebook secara langsung atau menjadwalkannya untuk waktu yang akan datang. Aplikasi ini menyediakan antarmuka web yang mudah digunakan sehingga Anda tidak perlu menyentuh kode untuk membuat postingan.

 <!-- Ganti dengan URL screenshot aplikasi Anda jika ada -->

## ✨ Fitur Utama

-   **Antarmuka Web Sederhana**: Tidak perlu keahlian teknis, semua dikelola melalui browser.
-   **Posting Langsung**: Kirim pembaruan status ke Halaman Facebook Anda secara instan.
-   **Penjadwalan Postingan**: Atur tanggal dan waktu spesifik untuk mempublikasikan postingan Anda secara otomatis.
-   **Manajemen Jadwal**: Lihat daftar semua postingan yang telah dijadwalkan dan batalkan jika perlu.
-   **Persisten**: Jadwal postingan disimpan dalam database lokal (`SQLite`), sehingga tidak akan hilang meskipun aplikasi di-restart.

## 🛠️ Teknologi yang Digunakan

-   **Backend**: Python
-   **Web Framework**: Flask
-   **Penjadwalan**: Flask-APScheduler
-   **Integrasi Facebook**: Facebook SDK for Python (`facebook-sdk`)
-   **Frontend**: HTML & CSS (tanpa framework eksternal)

## ⚙️ Pengaturan dan Instalasi

Ikuti langkah-langkah berikut untuk menjalankan aplikasi ini di komputer lokal Anda.

### 1. Prasyarat

-   **Akun Facebook Developer**: Wajib punya. Daftar gratis di [developers.facebook.com](https://developers.facebook.com/).
-   **Halaman Facebook (Fan Page)**: Anda harus menjadi admin dari Halaman yang akan dituju.
-   **Python 3.8+** dan `pip`.

### 2. Dapatkan Kredensial Facebook

Sebelum menjalankan aplikasi, Anda memerlukan dua hal penting dari Facebook:
-   **Page ID**: ID unik dari Halaman Facebook Anda.
-   **Page Access Token**: Kunci rahasia untuk memberikan izin kepada aplikasi Anda untuk memposting.

Untuk mendapatkannya, ikuti panduan resmi di [**Facebook Graph API Explorer**](https://developers.facebook.com/docs/graph-api/overview/):
1.  Buka [Graph API Explorer](https://developers.facebook.com/tools/explorer/).
2.  Di kanan atas, pilih **Aplikasi Facebook** Anda.
3.  Pada dropdown "User or Page", pilih **"Get Page Access Token"**.
4.  Berikan izin `pages_manage_posts` dan `pages_read_engagement`.
5.  Pilih Halaman Anda. Token akan dibuat.
6.  **PENTING**: Token ini hanya berlaku sebentar (short-lived). Anda harus mengubahnya menjadi **long-lived token** (berlaku ~60 hari) agar tidak perlu sering-sering membuat token baru. Gunakan token yang baru saja Anda dapatkan untuk membuat permintaan ke endpoint berikut (ganti `{...}` dengan nilai Anda):
    ```
    https://graph.facebook.com/v19.0/oauth/access_token?grant_type=fb_exchange_token&client_id={app-id}&client_secret={app-secret}&fb_exchange_token={short-lived-token}
    ```
    Simpan token yang dihasilkan dari permintaan ini.

### 3. Instalasi Proyek

1.  **Clone repositori ini:**
    ```bash
    git clone https://github.com/NAMA_USER_ANDA/NAMA_REPO_ANDA.git
    cd NAMA_REPO_ANDA
    ```

2.  **Buat dan aktifkan virtual environment (sangat disarankan):**
    ```bash
    # Untuk Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Untuk macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instal semua dependensi yang diperlukan:**
    Buat file bernama `requirements.txt` dan isi dengan teks di bawah ini, lalu jalankan perintah instalasi.

    **`requirements.txt`:**
    ```
    Flask
    Flask-APScheduler
    facebook-sdk
    ```

    **Perintah instalasi:**
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Cara Menjalankan Aplikasi

1.  Pastikan Anda berada di direktori utama proyek dan virtual environment Anda aktif.
2.  Jalankan aplikasi Flask dengan perintah berikut:
    ```bash
    python app.py
    ```
3.  Terminal akan menampilkan alamat lokal tempat aplikasi berjalan, biasanya:
    ```
    * Running on http://127.0.0.1:5000
    ```
4.  Buka browser Anda dan kunjungi **`http://127.0.0.1:5000`**.

## 📖 Cara Penggunaan

1.  **Isi Formulir**:
    -   **Page ID**: Masukkan ID Halaman Facebook Anda.
    -   **Page Access Token**: Tempel *long-lived token* yang sudah Anda dapatkan.
    -   **Message**: Tulis konten status yang ingin Anda posting.
2.  **Pilih Aksi**:
    -   **Untuk Posting Sekarang**: Biarkan kolom **"Schedule Time"** kosong, lalu klik **"Submit Post"**.
    -   **Untuk Menjadwalkan**: Klik kolom **"Schedule Time"**, pilih tanggal dan waktu di masa depan, lalu klik **"Submit Post"**.
3.  **Lihat Jadwal**: Postingan yang dijadwalkan akan muncul di tabel "Scheduled Posts" di bagian bawah halaman. Anda bisa membatalkannya dengan mengklik **"Hapus"**.

## ⚠️ Peringatan Keamanan

-   **Jangan Pernah Mengekspos `Page Access Token` Anda!** Token ini sangat rahasia. Jangan membagikannya atau menyimpannya di repositori publik. Aplikasi ini dirancang untuk penggunaan pribadi di lingkungan lokal.
-   Aplikasi ini berjalan dalam **mode debug**, yang tidak aman untuk lingkungan produksi.

## 🔮 Rencana Pengembangan

Beberapa ide untuk pengembangan di masa depan:

-   [ ] **Postingan Gambar**: Menambahkan fitur untuk mengunggah dan memposting gambar.
-   [ ] **Jadwal Berulang**: Mengatur postingan untuk diulang setiap hari, minggu, atau bulan.
-   [ ] **Database Pengguna**: Mengelola beberapa akun atau Halaman Facebook.
-   [ ] **Autentikasi Pengguna**: Sistem login untuk melindungi akses ke aplikasi.
-   [ ] **Penyimpanan Token yang Aman**: Menggunakan *environment variables* atau *secrets management* untuk menyimpan token.

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).
