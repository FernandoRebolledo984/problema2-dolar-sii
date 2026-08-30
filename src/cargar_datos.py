from pathlib import Path
import numpy as np

rutaCSV = Path(__file__).resolve().parent.parent/ "data" / "dolar_observado_sii_2022_2025.csv"

datos = np.genfromtxt(rutaCSV, delimiter=",", names=True, dtype=None, encoding="utf-8")
