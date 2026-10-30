"""Utilitas umum: seed, penyimpanan grafik, dan pencatatan versi library."""
import os
import platform
import random
import importlib

import numpy as np

from src.config import FIG_DIR, SEED


def set_seed(seed: int = SEED, deterministic_tf: bool = False) -> None:
    """Mengunci sumber acak (Python, NumPy, TensorFlow) agar eksperimen bisa diulang.

    deterministic_tf=True membuat operasi TF deterministik penuh, tetapi
    pelatihan di GPU bisa sedikit lebih lambat.
    """
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    try:
        import tensorflow as tf
        tf.keras.utils.set_random_seed(seed)
        if deterministic_tf:
            tf.config.experimental.enable_op_determinism()
    except ImportError:
        pass  # TensorFlow belum dibutuhkan pada tahap EDA


def save_fig(fig, name: str, dpi: int = 150) -> str:
    """Menyimpan grafik ke results/figures dengan nama konsisten untuk laporan."""
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    path = FIG_DIR / f"{name}.png"
    fig.savefig(path, dpi=dpi, bbox_inches="tight")
    return str(path)


def get_versions() -> dict:
    """Mengembalikan versi Python dan library utama (untuk bab Teknologi di laporan)."""
    versions = {"python": platform.python_version()}
    for lib in ["numpy", "pandas", "sklearn", "scipy", "matplotlib",
                "seaborn", "tensorflow", "keras", "kagglehub"]:
        try:
            versions[lib] = importlib.import_module(lib).__version__
        except Exception:
            versions[lib] = "tidak terpasang"
    return versions
