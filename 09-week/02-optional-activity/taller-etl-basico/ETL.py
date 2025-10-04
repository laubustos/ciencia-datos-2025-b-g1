import pandas as pd
import sqlite3
import json

# 1. Extracción
with open("dataset-EduSmart/edusmart.json", "r") as f:
    data = json.load(f)

estudiantes = pd.DataFrame(data["estudiantes"])
cursos = pd.DataFrame(data["cursos"])
matriculas = pd.DataFrame(data["matriculas"])

# 2. Transformación
# Limpieza de estudiantes
estudiantes = estudiantes.dropna().drop_duplicates()
estudiantes["nombre"] = estudiantes["nombre"].str.upper()

# Normalización de fechas
matriculas["fecha"] = pd.to_datetime(matriculas["fecha"], errors="coerce")

# Integración
df = matriculas.merge(estudiantes, on="id_estudiante", how="inner")
df = df.merge(cursos, on="id_curso", how="inner")

# Cálculo del costo total (ejemplo de métrica)
df["costo_total"] = df["costo"] * df["duracion_semanas"]

# 3. Carga
conn = sqlite3.connect("edusmart.db")
df.to_sql("matriculas_limpias", conn, if_exists="replace", index=False)
conn.close()

print("Proceso ETL completado. Datos cargados en 'matriculas_limpias'")
