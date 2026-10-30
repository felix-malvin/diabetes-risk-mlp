# Catatan Keputusan Proyek

Setiap keputusan penting dicatat di sini, lengkap dengan alasannya. Bagian ini menjadi bahan langsung untuk laporan dan menjaga konsistensi antaranggota.

| ID | Tanggal | Keputusan | Alasan | Status |
|---|---|---|---|---|
| D-01 | 30 Okt 2026 | Satu repository untuk Tugas 1 dan UTS, dibedakan dengan tag rilis `tugas1-final` dan `uts-final` | Dataset, pipeline, dan model sama. Dua repo berisiko menghasilkan dua versi kode yang berbeda | Disepakati |
| D-02 | 30 Okt 2026 | Tugas 1 dan UTS memakai model, preprocessing, dan angka evaluasi yang sama | Sudah dikonfirmasi boleh oleh dosen. UTS hanya menambah aplikasi, deployment, dan video | Disepakati |
| D-03 | 30 Okt 2026 | Fitur unik 1: cost-sensitive learning (class weight / focal loss) dan threshold yang dioptimasi pada data validation | Menjawab ketidakseimbangan kelas dan mahalnya false negative pada konteks risiko diabetes | Disepakati |
| D-04 | 30 Okt 2026 | Fitur unik 2: penjelasan faktor risiko per prediksi dengan Integrated Gradients | Padanan Grad-CAM untuk data tabular, bisa ditampilkan di aplikasi, tanpa ketergantungan library tambahan | Disepakati |
| D-05 | 30 Okt 2026 | Butir laporan A.1.c ("pengembangan dari Tugas Proyek 2") tidak diisi pengembangan | Tidak ada Tugas Proyek 2 sebelumnya | Disepakati |
| D-06 | 30 Okt 2026 | Platform deployment: Streamlit Community Cloud | Gratis untuk aplikasi publik dan terhubung langsung ke GitHub | Disepakati |
| D-07 | _menunggu EDA_ | Penanganan baris duplikat dan baris dengan fitur identik tetapi label berbeda | Ditentukan setelah melihat hasil `01_eda.ipynb` | Terbuka |
| D-08 | _menunggu EDA_ | Proporsi split dan strategi pencegahan kebocoran | Ditentukan di `02_preprocessing.ipynb` | Terbuka |
| D-09 | 5 Nov 2026 | **Model freeze** (konfigurasi final) | Setelah tanggal ini tidak ada pelatihan ulang | Terjadwal |
