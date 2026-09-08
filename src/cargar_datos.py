from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import os

rutaCSV = Path(__file__).resolve().parent.parent/ "data" / "dolar_observado_sii_2022_2025.csv"

datos = np.genfromtxt(rutaCSV, delimiter=",", names=True, dtype=["U20","U20","i4","f8"], encoding="utf-8")