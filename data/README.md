# Dokumentasi Dataset

## Sumber

- **Nama:** Diabetes Health Indicators Dataset
- **Penyusun:** Alex Teboul (Kaggle)
- **Tautan:** https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset
- **File yang dipakai:** `diabetes_binary_health_indicators_BRFSS2015.csv`
- **Asal data:** Behavioral Risk Factor Surveillance System (BRFSS) 2015, survei kesehatan telepon tahunan oleh CDC Amerika Serikat. Versi Kaggle ini sudah dibersihkan dan diringkas oleh penyusun dari data BRFSS 2015 asli.
- **Rujukan setara:** UCI Machine Learning Repository, *CDC Diabetes Health Indicators* (ID 891), https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators
- **Lisensi:** _cek dan tulis di sini sesuai halaman Kaggle sebelum laporan final._

## Karakteristik

| Properti | Nilai |
|---|---|
| Jumlah baris | 253.680 respons survei |
| Jumlah fitur | 21 |
| Target | `Diabetes_binary` |
| Format | CSV, seluruh nilai numerik |
| Jenis data | Real-world (survei), bukan sintetis |
| Missing value | Tidak ada menurut penyusun (diverifikasi ulang di `01_eda.ipynb`) |

**Arti label:** `0` = tidak diabetes, `1` = **prediabetes atau diabetes**. Label 1 menggabungkan dua kondisi, sehingga model memprediksi *risiko*, bukan diagnosis diabetes.

## Kamus Fitur

| Fitur | Tipe | Rentang | Keterangan |
|---|---|---|---|
| HighBP | Biner | 0–1 | Pernah didiagnosis tekanan darah tinggi |
| HighChol | Biner | 0–1 | Pernah didiagnosis kolesterol tinggi |
| CholCheck | Biner | 0–1 | Cek kolesterol dalam 5 tahun terakhir |
| BMI | Numerik | 12–98 | Body Mass Index |
| Smoker | Biner | 0–1 | Pernah merokok minimal 100 batang seumur hidup |
| Stroke | Biner | 0–1 | Pernah didiagnosis stroke |
| HeartDiseaseorAttack | Biner | 0–1 | Penyakit jantung koroner atau serangan jantung |
| PhysActivity | Biner | 0–1 | Aktivitas fisik di luar pekerjaan, 30 hari terakhir |
| Fruits | Biner | 0–1 | Konsumsi buah minimal 1x per hari |
| Veggies | Biner | 0–1 | Konsumsi sayur minimal 1x per hari |
| HvyAlcoholConsump | Biner | 0–1 | Konsumsi alkohol berat |
| AnyHealthcare | Biner | 0–1 | Memiliki jaminan/asuransi kesehatan |
| NoDocbcCost | Biner | 0–1 | Tidak bisa ke dokter karena biaya, 12 bulan terakhir |
| GenHlth | Ordinal | 1–5 | Penilaian diri kesehatan umum (1 sangat baik, 5 buruk) |
| MentHlth | Numerik (hitungan hari) | 0–30 | Hari kesehatan mental buruk, 30 hari terakhir |
| PhysHlth | Numerik (hitungan hari) | 0–30 | Hari kesehatan fisik buruk, 30 hari terakhir |
| DiffWalk | Biner | 0–1 | Kesulitan serius berjalan atau naik tangga |
| Sex | Biner | 0–1 | 0 perempuan, 1 laki-laki |
| Age | Ordinal | 1–13 | Kategori usia 5 tahunan (1 = 18–24, 13 = 80+) |
| Education | Ordinal | 1–6 | Tingkat pendidikan |
| Income | Ordinal | 1–8 | Kategori pendapatan |

Definisi yang sama (nama, urutan, rentang) tersimpan di `src/config.py`. Jika ada perbedaan, `src/config.py` yang dipakai kode.

## Cara Mendapatkan Data

Data diunduh otomatis oleh `src/data.py` melalui `kagglehub`. Jika gagal, unduh CSV secara manual dari Kaggle lalu letakkan di `data/raw/`.

## Folder `splits/`

Berisi indeks baris untuk data train, validation, dan test (dibuat di `02_preprocessing.ipynb`). Semua anggota **wajib** memakai indeks yang sama supaya hasil eksperimen bisa dibandingkan.
