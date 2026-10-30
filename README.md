# Prediksi Risiko Diabetes Menggunakan Multilayer Perceptron (MLP)

Proyek mata kuliah **Pembelajaran Mendalam (Deep Learning)**, Semester Ganjil TA 2026/2027.
Repository ini dipakai untuk **Tugas 1** dan **UTS**. Kedua tugas memakai dataset, pipeline, dan model final yang sama. UTS menambahkan aplikasi yang di-deploy dan video demo.

> **Disclaimer:** Aplikasi dan model di repository ini adalah alat demonstrasi akademik untuk memperkirakan *risiko* berdasarkan indikator kesehatan hasil survei. Hasilnya **bukan diagnosis medis** dan tidak menggantikan pemeriksaan oleh tenaga kesehatan.

## Tautan

| Artefak | Link |
|---|---|
| Aplikasi (UTS) | _menyusul_ |
| Video demo & deployment (UTS) | _menyusul_ |
| Laporan Tugas 1 | `reports/tugas1/` (rilis `tugas1-final`) |
| Laporan UTS | `reports/uts/` (rilis `uts-final`) |

## Anggota Kelompok

| NIM | Nama | Peran utama |
|---|---|---|
| 231111970 | Felix Malvin | Koordinator teknis & repo, preprocessing, eksperimen arsitektur |
| 231110702 | Afriyoga Haganta Tarigan | EDA, eksperimen regularisasi, editor laporan |
| 231110595 | Wilbert Edric Tanjiro | Pelatihan, eksperimen optimizer, evaluasi final |
| 231110730 | Johannes Hartanto | Fitur unik 1: penanganan imbalance & threshold |
| 231110980 | Erik Hamli | Fitur unik 2: explainability, aplikasi & deployment |

## Dataset

[Diabetes Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset) (Kaggle, Alex Teboul), file `diabetes_binary_health_indicators_BRFSS2015.csv`. Detail fitur ada di [`data/README.md`](data/README.md). File CSV **tidak** disimpan di repository. Notebook akan mengunduhnya otomatis.

## Struktur Repository

```
├── data/          # dokumentasi dataset, indeks split (CSV mentah tidak di-commit)
├── notebooks/     # notebook Colab berurutan 00, 01, 02, ...
├── src/           # kode bersama: konfigurasi, pemuatan data, model, evaluasi
├── models/        # artefak model final (model, scaler, konfigurasi threshold)
├── results/       # grafik, log eksperimen, metrik final
├── app/           # aplikasi Streamlit (UTS)
├── docs/          # catatan keputusan & screenshot deployment
└── reports/       # laporan PDF Tugas 1 dan UTS
```

## Cara Menjalankan di Google Colab

1. Buka notebook dari GitHub di Colab (*File → Open notebook → GitHub*).
2. Jalankan sel pertama. Sel tersebut meng-clone repository ini ke `/content/diabetes-risk-mlp` sehingga modul `src/` bisa di-import.
3. Jalankan notebook **berurutan**: `00_setup` → `01_eda` → `02_preprocessing` → dan seterusnya.

## Reproducibility

- Seed global `42` diatur di `src/config.py` dan dipanggil lewat `src.utils.set_seed()`.
- Urutan fitur, rentang nilai valid, dan nama target hanya didefinisikan di `src/config.py`.
- Versi library dicatat otomatis oleh `00_setup.ipynb` ke `results/environment.json`.

## Kontribusi

Lihat [`CONTRIBUTING.md`](CONTRIBUTING.md) untuk aturan branch, commit, dan pull request.
