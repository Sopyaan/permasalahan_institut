# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut adalah sebuah institusi pendidikan tinggi berbasis teknologi (Edutech) yang bertujuan untuk menyediakan layanan pendidikan berkualitas dengan dukungan sistem informasi yang modern. Namun, seperti banyak institusi pendidikan lainnya, Jaya Jaya Institut menghadapi tantangan besar terkait tingkat siswa yang mengalami dropout (putus studi). Tingginya angka dropout ini berpotensi merugikan secara reputasi, keuangan, dan efektivitas operasional lembaga.

### Permasalahan Bisnis
Permasalahan utama yang dihadapi oleh Jaya Jaya Institut:
- Tingginya tingkat siswa yang dropout dalam dua semester pertama.
- Tidak adanya sistem prediksi untuk mengidentifikasi siswa yang berisiko tinggi dropout sejak awal.
- Kurangnya dashboard analitik yang mampu memberikan wawasan cepat kepada manajemen terkait performa akademik dan risiko dropout.

### Cakupan Proyek
Proyek ini bertujuan untuk menyelesaikan permasalahan di atas dengan cakupan sebagai berikut:
- Membuat business dashboard interaktif untuk memantau performa siswa dan tren dropout.
- Membangun sistem machine learning berbasis data historis untuk memprediksi kemungkinan siswa mengalami dropout.
- Mengembangkan prototype berbasis Streamlit sebagai antarmuka prediksi yang dapat digunakan oleh staf akademik.
- Memberikan rekomendasi berbasis data untuk menurunkan tingkat dropout.

### Persiapan

Sumber data: Dataset yang digunakan berasal dari dicoding untuk latihan menyelesaikan permsalahan data science.
[dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

Setup environment:
```
# Setup virtual environment
python -m venv venv
source venv/bin/activate  # Jika menggunakan Unix/Mac
venv\Scripts\activate     # Jika menggunakan Windows


# Install dependencies
pip install -r requirements.txt

```

## Business Dashboard
Dashboard ini dibuat menggunakan Looker Studio untuk memvisualisasikan data dropout mahasiswa berdasarkan gender, status pernikahan, penerima beasiswa, dan nilai akademik.

Fitur dashboard:
- Total mahasiswa
- Rata-rata usia, nilai semester 1 dan 2
- Distribusi status (graduate, dropout, enrolled)
- Visualisasi hubungan status dengan gender, status pernikahan, dan beasiswa

[Link akses dashboard](https://lookerstudio.google.com/reporting/ad66a601-2b53-4fe9-b1f8-ab6207bcdb7d)

## Menjalankan Sistem Machine Learning
Prototype sistem prediksi dropout mahasiswa dikembangkan menggunakan model Gradient Boosting Classifier, yang terbukti efektif dalam menangani masalah klasifikasi kompleks. Sistem ini kemudian diimplementasikan dalam antarmuka interaktif berbasis Streamlit, sehingga mudah digunakan oleh staf akademik.

Fitur utama pada dashboard untuk melakukan prediksi yaitu:
- Gender
- Age at Enrollment
- Debtor
- Tuition Fees Up to Date
- Scholarship Holder
- Displaced
- Informasi akademi semester 1 dan 2

Setelah data dimasukkan, sistem akan memberikan prediksi apakah mahasiswa tersebut berpotensi untuk melakukan dropout atau tidak, lengkap dengan indikator visual yang mudah dipahami.

```
# Cara Menjalankan Aplikasi
streamlit run app.py
```
[Link prototype Streamlit]()

## Conclusion
Dari proyek ini ditemukan bahwa:
- Sekitar 32% mahasiswa mengalami dropout.
- Faktor-faktor seperti umur, marital status, nilai akademik, jumlah mata kuliah yang diambil dan diselesaikan, serta status beasiswa berperan penting dalam memengaruhi status kelulusan mahasiswa.
- Model Gradient Boosting memberikan hasil prediksi yang baik untuk memetakan potensi dropout mahasiswa dengan tingkat akurasi mencapai 0.87.


### Rekomendasi Action Items
- Pemantauan Dini: Gunakan dashboard dan sistem prediksi untuk mengidentifikasi siswa berisiko dropout sejak dini.
- Intervensi Akademik: Berikan bantuan belajar atau bimbingan akademik kepada siswa dengan performa semester yang rendah karena ini menjadi salah satu hal yang berpengaruh terhadap angka dropout yang terjadi.
-  Evaluasi Program Beasiswa: Tinjau kembali kriteria dan distribusi beasiswa agar dapat membantu siswa yang benar-benar membutuhkan.
