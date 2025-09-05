import pandas as pd
import os
from tkinter import Tk, filedialog
import shutil
import matplotlib.pyplot as plt
import textwrap

def seleccionar_archivo():
    Tk().withdraw()  # Oculta la ventana principal de Tkinter
    archivo = filedialog.askopenfilename(
        title="Selecciona un archivo de datos",
        filetypes=[
            ("Archivos CSV", "*.csv"),
            ("Archivos Excel", "*.xlsx;*.xls"),
            ("Archivos de texto", "*.txt"),
            ("Todos los archivos", "*.*")
        ]
    )
    return archivo

def cargar_archivo(ruta_archivo):
    if not os.path.isfile(ruta_archivo):
        raise FileNotFoundError(f"El archivo '{ruta_archivo}' no existe.")
    try:
        if ruta_archivo.endswith('.csv'):
            df = pd.read_csv(ruta_archivo)
        elif ruta_archivo.endswith('.xlsx') or ruta_archivo.endswith('.xls'):
            df = pd.read_excel(ruta_archivo)
        elif ruta_archivo.endswith('.txt'):
            df = pd.read_csv(ruta_archivo, delimiter='\t')
        else:
            raise ValueError("Formato de archivo no soportado. Usa .csv, .xlsx, .xls o .txt")
        print(f"Archivo cargado correctamente: {ruta_archivo}")
        return df
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None

def descargar_archivo(origen):
    Tk().withdraw()
    destino = filedialog.asksaveasfilename(
        title="Guardar archivo como",
        initialfile=os.path.basename(origen),
        defaultextension=os.path.splitext(origen)[1],
        filetypes=[("Todos los archivos", "*.*")]
    )
    if destino:
        shutil.copy(origen, destino)
        print(f"Archivo guardado en: {destino}")
    else:
        print("No se seleccionó destino.")

def dataframe_a_pdf(df, ruta_pdf, max_filas=20, max_columnas=10, ancho_max=20):
    df_mostrar = df.copy()
    if len(df_mostrar) > max_filas:
        df_mostrar = df_mostrar.head(max_filas)
        nota = f"Mostrando solo las primeras {max_filas} filas de {len(df)}"
    else:
        nota = None
    if len(df_mostrar.columns) > max_columnas:
        df_mostrar = df_mostrar.iloc[:, :max_columnas]
        nota = (nota or "") + f" | Mostrando solo las primeras {max_columnas} columnas de {len(df.columns)}"

    # Aplica saltos de línea a celdas largas
    def wrap_cell(cell):
        if isinstance(cell, str):
            return '\n'.join(textwrap.wrap(cell, ancho_max))
        return cell

    cell_text = [[wrap_cell(cell) for cell in row] for row in df_mostrar.values]

    fig_width = min(0.8 * len(df_mostrar.columns), 16)
    fig_height = min(0.6 * len(df_mostrar), 12)
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    ax.axis('tight')
    ax.axis('off')
    tabla = ax.table(cellText=cell_text, colLabels=df_mostrar.columns, loc='center')
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(7)
    tabla.scale(1.3, 1.3)

    # Ajusta el ancho de columnas
    for i, key in enumerate(tabla._cells):
        cell = tabla._cells[key]
        cell.set_width(1.0 / len(df_mostrar.columns))

    if nota:
        plt.figtext(0.5, 0.02, nota, ha="center", fontsize=9, color="red")

    plt.tight_layout()
    plt.savefig(ruta_pdf, bbox_inches='tight')
    plt.close()
    print(f"DataFrame guardado como PDF en: {ruta_pdf}")

def graficar_df(df):
    # Selecciona las dos primeras columnas numéricas
    columnas_numericas = df.select_dtypes(include='number').columns
    if len(columnas_numericas) >= 2:
        x = columnas_numericas[0]
        y = columnas_numericas[1]
        plt.figure(figsize=(8, 5))
        plt.plot(df[x], df[y], marker='o')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(f'Gráfica de {x} vs {y}')
        plt.grid(True)
        plt.show()
    else:
        print("No hay suficientes columnas numéricas para graficar.")

if __name__ == "__main__":
    archivo = seleccionar_archivo()
    if archivo:
        df = cargar_archivo(archivo)
        if df is not None:
            print("DataFrame creado correctamente:")
            print(df.head())
            ruta_pdf = filedialog.asksaveasfilename(
                title="Guardar DataFrame como PDF",
                defaultextension=".pdf",
                filetypes=[("Archivo PDF", "*.pdf")]
            )
            if ruta_pdf:
                dataframe_a_pdf(df, ruta_pdf)
            graficar_df(df)



