"""
Konfigurasi terpusat proyek Prediksi Risiko Diabetes (MLP).

Semua notebook dan aplikasi WAJIB mengambil nama kolom, urutan fitur,
seed, dan path dari file ini supaya konsisten di seluruh artefak
(notebook, model, aplikasi, laporan).
"""
from pathlib import Path

# ---------------------------------------------------------------------------
# Path proyek (dihitung dari lokasi file ini, aman dipakai dari folder mana pun)
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
SPLIT_DIR = DATA_DIR / "splits"
MODEL_DIR = ROOT / "models"
RESULTS_DIR = ROOT / "results"
FIG_DIR = RESULTS_DIR / "figures"

# ---------------------------------------------------------------------------
# Reproducibility
# ---------------------------------------------------------------------------
SEED = 42

# ---------------------------------------------------------------------------
# Dataset
# ---------------------------------------------------------------------------
KAGGLE_DATASET = "alexteboul/diabetes-health-indicators-dataset"
CSV_NAME = "diabetes_binary_health_indicators_BRFSS2015.csv"
EXPECTED_SHAPE = (253_680, 22)

# Diisi setelah 00_setup.ipynb dijalankan pertama kali (lihat results/environment.json).
# Jika sudah diisi, loader akan memastikan semua anggota memakai file yang identik.
DATA_MD5 = None

TARGET = "Diabetes_binary"  # 0 = tidak diabetes, 1 = prediabetes ATAU diabetes

# Pengelompokan fitur berdasarkan codebook BRFSS2015 (Kaggle/UCI)
BINARY_FEATURES = [
    "HighBP", "HighChol", "CholCheck", "Smoker", "Stroke",
    "HeartDiseaseorAttack", "PhysActivity", "Fruits", "Veggies",
    "HvyAlcoholConsump", "AnyHealthcare", "NoDocbcCost", "DiffWalk", "Sex",
]
ORDINAL_FEATURES = ["GenHlth", "Age", "Education", "Income"]
NUMERIC_FEATURES = ["BMI", "MentHlth", "PhysHlth"]

# Urutan fitur resmi. Urutan ini dipakai saat training DAN inference di aplikasi.
FEATURES = [
    "HighBP", "HighChol", "CholCheck", "BMI", "Smoker", "Stroke",
    "HeartDiseaseorAttack", "PhysActivity", "Fruits", "Veggies",
    "HvyAlcoholConsump", "AnyHealthcare", "NoDocbcCost", "GenHlth",
    "MentHlth", "PhysHlth", "DiffWalk", "Sex", "Age", "Education", "Income",
]

# Rentang nilai valid menurut codebook (dipakai untuk validasi data dan input aplikasi)
VALID_RANGES = {
    **{f: (0, 1) for f in BINARY_FEATURES},
    "GenHlth": (1, 5),      # 1 = sangat baik ... 5 = buruk
    "Age": (1, 13),         # kategori usia 5 tahunan, 1 = 18-24 ... 13 = 80+
    "Education": (1, 6),    # 1 = tidak sekolah/TK ... 6 = lulus perguruan tinggi
    "Income": (1, 8),       # 1 = < $10.000 ... 8 = >= $75.000
    "BMI": (12, 98),        # rentang yang teramati di dataset
    "MentHlth": (0, 30),    # jumlah hari kesehatan mental buruk dalam 30 hari
    "PhysHlth": (0, 30),    # jumlah hari kesehatan fisik buruk dalam 30 hari
}

FEATURE_DESCRIPTIONS = {
    "HighBP": "Pernah didiagnosis tekanan darah tinggi",
    "HighChol": "Pernah didiagnosis kolesterol tinggi",
    "CholCheck": "Cek kolesterol dalam 5 tahun terakhir",
    "BMI": "Body Mass Index",
    "Smoker": "Pernah merokok minimal 100 batang seumur hidup",
    "Stroke": "Pernah didiagnosis stroke",
    "HeartDiseaseorAttack": "Penyakit jantung koroner atau serangan jantung",
    "PhysActivity": "Aktivitas fisik di luar pekerjaan dalam 30 hari terakhir",
    "Fruits": "Konsumsi buah minimal 1x per hari",
    "Veggies": "Konsumsi sayur minimal 1x per hari",
    "HvyAlcoholConsump": "Konsumsi alkohol berat (pria >= 14, wanita >= 7 gelas/minggu)",
    "AnyHealthcare": "Memiliki jaminan/asuransi kesehatan",
    "NoDocbcCost": "Tidak bisa ke dokter karena biaya (12 bulan terakhir)",
    "GenHlth": "Penilaian diri atas kesehatan umum (1 sangat baik - 5 buruk)",
    "MentHlth": "Hari dengan kesehatan mental buruk (30 hari terakhir)",
    "PhysHlth": "Hari dengan kesehatan fisik buruk (30 hari terakhir)",
    "DiffWalk": "Kesulitan serius berjalan atau naik tangga",
    "Sex": "Jenis kelamin (0 perempuan, 1 laki-laki)",
    "Age": "Kategori usia 13 tingkat (1 = 18-24, 13 = 80+)",
    "Education": "Tingkat pendidikan (1-6)",
    "Income": "Kategori pendapatan (1-8)",
}

assert len(FEATURES) == 21
assert set(FEATURES) == set(BINARY_FEATURES + ORDINAL_FEATURES + NUMERIC_FEATURES)
