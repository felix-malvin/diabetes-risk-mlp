"""Pemuatan dan validasi dataset BRFSS2015 (Diabetes Health Indicators)."""
import hashlib
import shutil
from pathlib import Path

import pandas as pd

from src.config import (CSV_NAME, DATA_MD5, EXPECTED_SHAPE, FEATURES,
                        KAGGLE_DATASET, RAW_DIR, TARGET, VALID_RANGES)


def file_md5(path) -> str:
    """Checksum file untuk memastikan semua anggota memakai data yang sama."""
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def get_raw_path() -> Path:
    """Mencari CSV di data/raw. Jika belum ada, unduh lewat kagglehub lalu salin ke data/raw."""
    local = RAW_DIR / CSV_NAME
    if local.exists():
        return local
    try:
        import kagglehub
    except ImportError as e:
        raise ImportError("Pasang kagglehub dulu: %pip install kagglehub") from e

    try:
        folder = Path(kagglehub.dataset_download(KAGGLE_DATASET))
    except Exception as e:
        raise RuntimeError(
            "Gagal mengunduh dari Kaggle. Opsi: (1) isi KAGGLE_USERNAME dan "
            "KAGGLE_KEY di Colab Secrets, atau (2) unduh CSV secara manual "
            f"lalu letakkan di {local}"
        ) from e

    src_file = next(folder.rglob(CSV_NAME), None)
    if src_file is None:
        raise FileNotFoundError(f"{CSV_NAME} tidak ditemukan di {folder}")
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy(src_file, local)
    return local


def validate_schema(df: pd.DataFrame) -> None:
    """Memastikan kolom, ukuran, dan rentang nilai sesuai codebook. Gagal keras jika tidak."""
    expected_cols = [TARGET] + FEATURES
    missing = set(expected_cols) - set(df.columns)
    extra = set(df.columns) - set(expected_cols)
    if missing or extra:
        raise ValueError(f"Kolom tidak sesuai. Hilang: {missing}, berlebih: {extra}")
    if df.shape != EXPECTED_SHAPE:
        print(f"[PERINGATAN] Ukuran data {df.shape}, diharapkan {EXPECTED_SHAPE}")
    for col, (lo, hi) in {**VALID_RANGES, TARGET: (0, 1)}.items():
        bad = (~df[col].between(lo, hi)).sum()
        if bad:
            print(f"[PERINGATAN] {col}: {bad} nilai di luar rentang [{lo}, {hi}]")


def load_raw(verify_md5: bool = True) -> pd.DataFrame:
    """Memuat dataset mentah, memvalidasi skema, dan mengubah tipe ke integer.

    CSV dari Kaggle menyimpan semua nilai sebagai float (misalnya 1.0).
    Karena seluruh fitur pada dasarnya bilangan bulat, tipe diubah ke int
    setelah dipastikan tidak ada nilai pecahan.
    """
    path = get_raw_path()
    if verify_md5 and DATA_MD5 is not None:
        md5 = file_md5(path)
        if md5 != DATA_MD5:
            raise ValueError(f"MD5 file berbeda ({md5}). Pastikan memakai file yang sama.")

    df = pd.read_csv(path)
    validate_schema(df)

    non_integer = [c for c in df.columns if (df[c] % 1 != 0).any()]
    if non_integer:
        print(f"[PERINGATAN] Kolom berisi nilai pecahan, tidak diubah ke int: {non_integer}")
    int_cols = [c for c in df.columns if c not in non_integer]
    df[int_cols] = df[int_cols].astype("int64")
    return df[[TARGET] + FEATURES]
