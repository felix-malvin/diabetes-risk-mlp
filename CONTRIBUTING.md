# Panduan Kontribusi

## 1. Branch

- `main` diproteksi. Tidak ada yang boleh push langsung ke `main`.
- Setiap pekerjaan dibuat di branch dengan pola `nama/topik`, contoh:
  - `afriyoga/eda`
  - `felix/preprocessing`
  - `wilbert/exp-optimizer`
  - `johannes/feature-imbalance`
  - `erik/app-streamlit`
- Satu branch untuk satu topik. Setelah di-merge, branch boleh dihapus.

## 2. Pesan Commit

Format: `<jenis>: <ringkasan singkat>`

| Jenis | Dipakai untuk |
|---|---|
| `feat` | kode atau notebook baru |
| `exp` | menambah atau mengubah eksperimen |
| `fix` | memperbaiki bug |
| `docs` | README, laporan, catatan keputusan |
| `refactor` | merapikan kode tanpa mengubah hasil |
| `chore` | konfigurasi, `.gitignore`, requirements |

Contoh: `exp: tambah varian dropout 0.3 dan 0.5 pada MLP 3 layer`

Tulis commit yang bermakna. Hindari pesan seperti `update` atau `fix` tanpa keterangan.

## 3. Pull Request

1. Push branch, lalu buka Pull Request ke `main`.
2. Minimal **1 reviewer** dari anggota lain (bergiliran, jangan selalu orang yang sama).
3. Reviewer menjalankan ulang notebook atau kode yang diubah bila memungkinkan.
4. Merge setelah disetujui. Gunakan *Squash and merge* hanya bila commit di branch sangat berantakan.

## 4. Aturan Notebook (penting untuk mencegah konflik)

- **Satu notebook dipegang satu orang.** File `.ipynb` hampir mustahil di-merge jika diedit dua orang bersamaan.
- Logika yang dipakai bersama (urutan fitur, loader, pembangun model) ditaruh di `src/` dan diubah lewat PR kecil.
- Jangan mengubah `src/config.py` tanpa memberi tahu grup, karena semua notebook bergantung padanya.
- Jalankan notebook dari atas sampai bawah (*Runtime → Restart and run all*) sebelum commit, supaya output yang tersimpan konsisten.

## 5. Menyimpan dari Colab ke GitHub

1. Di Colab: *File → Save a copy in GitHub*.
2. Pilih repository ini dan **branch milikmu** (bukan `main`).
3. Tulis pesan commit sesuai format di atas.
4. Grafik di `results/figures/` diunduh lewat sel terakhir notebook (file zip), lalu diunggah ke branch yang sama lewat GitHub (*Add file → Upload files*) atau lewat git lokal.

## 6. Memastikan Kontribusi Tercatat

- Commit dari Colab otomatis tercatat atas akun GitHub yang dihubungkan.
- Jika memakai git lokal, pastikan `git config user.email` **sama** dengan email akun GitHub. Jika berbeda, commit tidak muncul di grafik kontribusi.
- Untuk pekerjaan berpasangan, tambahkan baris berikut di akhir pesan commit:
  ```
  Co-authored-by: Nama Anggota <email-github@contoh.com>
  ```

## 7. Yang Tidak Boleh Di-commit

- File CSV mentah (`data/raw/`), kredensial Kaggle (`kaggle.json`), token apa pun.
- Checkpoint model eksperimen. Hanya model **final** yang masuk ke `models/`.
- File video. Cukup tautannya di README.
