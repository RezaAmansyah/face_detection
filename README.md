# Real time face and smille detection 


Proyek ini menampilkan aplikasi deteksi wajah dan senyum secara real-time yang dibangun menggunakan OpenCV dan Streamlit. Aplikasi ini menggunakan Haar Cascade untuk mendeteksi profil wajah dan senyuman dalam umpan video langsung dari webcam, memberikan cara sederhana untuk menunjukkan teknik deteksi objek dengan Python.

## Deskripsi Proyek

Dalam proyek ini, antarmuka sederhana dibuat menggunakan Streamlit untuk memungkinkan deteksi senyum secara real-time pada wajah dalam umpan webcam. Aplikasi ini memanfaatkan dua model Haar Cascade yang sudah dilatih sebelumnya:
- `haarcascade_profileface.xml` untuk mendeteksi profil wajah.
- `haarcascade_smile.xml` untuk mendeteksi senyuman.

## Fitur

- **Deteksi Real-time:** Mendeteksi wajah dan senyuman secara langsung, menandainya dengan persegi panjang berwarna hijau.
- **Antarmuka Berbasis Web:** Dibangun menggunakan Streamlit, memungkinkan pengoperasian cepat dan interaksi langsung melalui browser.
- **Kontrol Sederhana:** Pengguna dapat memulai dan menghentikan umpan webcam dengan sekali klik.

## Penjelasan Kode

1. **Memuat Model Cascade:** Aplikasi memuat dua model Haar Cascade yang sudah dilatih sebelumnya untuk deteksi senyuman dan profil wajah.
2. **Fungsi Deteksi:** Fungsi `detect_smile` memproses setiap frame video dengan mengonversinya ke grayscale dan menerapkan model cascade untuk mendeteksi senyum. Senyuman yang terdeteksi ditandai dengan persegi panjang hijau.
3. **Kontrol Webcam:**
   - Umpan webcam dimulai dengan tombol "Start Webcam," yang menginisialisasi sesi dan menampilkan frame dengan deteksi senyuman secara kontinu.
   - Tombol "Stop Webcam" menghentikan sesi webcam dengan baik.

## Cara Penggunaan

1. Jalankan aplikasi dengan Streamlit:
   ```
   streamlit run app.py
   ```
2. Klik **Start Webcam** untuk memulai deteksi senyuman secara real-time.
3. Klik **Stop Webcam** untuk mengakhiri deteksi dan menutup umpan webcam.

## Persyaratan

- Python 3.7+
- OpenCV
- Streamlit

## Contoh Penggunaan

Proyek ini bermanfaat bagi siapa saja yang ingin mempelajari visi komputer dan mengeksplorasi teknik deteksi wajah. Proyek ini juga dapat menjadi dasar untuk membangun aplikasi real-time yang lebih canggih, seperti deteksi emosi atau analisis ekspresi.

---

ReadMe ini memberikan gambaran umum tentang fungsi aplikasi, menjelaskan bagaimana setiap bagian kode bekerja, sehingga memudahkan orang lain untuk mereplikasi atau mengembangkan proyek ini lebih lanjut.
