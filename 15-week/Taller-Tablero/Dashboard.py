# dashboard.py
# TABLERO INTERACTIVO DE VENTAS


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Leer dataset
df = pd.read_csv(r"C:\Users\Laura Valentina\OneDrive\Escritorio\ciencia-datos-2025-b-g1\15-week\Taller-Tablero\dataset_ventas_colombia.csv", encoding="utf-8")
df["Fecha"] = pd.to_datetime(df["Fecha"])
df["Mes"] = df["Fecha"].dt.to_period("M").astype(str)

# 1 CÁLCULO DE KPIs
ventas_totales = df["Venta_Total"].sum()
promedio_mensual = df.groupby("Mes")["Venta_Total"].sum().mean()
clientes_unicos = df["Cliente"].nunique()
productos_unicos = df["Producto"].nunique()

# KPIs visuales (estilo Power BI)
fig_kpi = go.Figure()

fig_kpi.add_trace(go.Indicator(
    mode="number",
    value=ventas_totales,
    title={"text": "Ventas Totales"},
    number={"prefix": "$", "valueformat": ",.0f"},
    domain={'row': 0, 'column': 0}
))

fig_kpi.add_trace(go.Indicator(
    mode="number",
    value=promedio_mensual,
    title={"text": "Promedio Mensual"},
    number={"prefix": "$", "valueformat": ",.0f"},
    domain={'row': 0, 'column': 1}
))

fig_kpi.add_trace(go.Indicator(
    mode="number",
    value=clientes_unicos,
    title={"text": "Clientes Únicos"},
    number={"valueformat": ",.0f"},
    domain={'row': 0, 'column': 2}
))

fig_kpi.add_trace(go.Indicator(
    mode="number",
    value=productos_unicos,
    title={"text": "Productos"},
    number={"valueformat": ",.0f"},
    domain={'row': 0, 'column': 3}
))

fig_kpi.update_layout(
    grid={'rows': 1, 'columns': 4, 'pattern': "independent"},
    title="KPIs Principales del Negocio",
    template="plotly_dark"
)
fig_kpi.show()

# 2 TOP 5 PRODUCTOS MÁS VENDIDOS
top_productos = (
    df.groupby("Producto")["Venta_Total"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

fig1 = px.bar(
    top_productos,
    x="Producto",
    y="Venta_Total",
    text="Venta_Total",
    color="Producto",
    title="Top 5 Productos más Vendidos"
)
fig1.show()

# 3 EVOLUCIÓN DE VENTAS MENSUAL
ventas_mes = df.groupby("Mes")["Venta_Total"].sum().reset_index()
fig2 = px.line(
    ventas_mes,
    x="Mes",
    y="Venta_Total",
    markers=True,
    title="Evolución de Ventas por Mes"
)
fig2.show()

# 4 VENTAS POR REGIÓN
ventas_region = (
    df.groupby("Región")["Venta_Total"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
fig3 = px.bar(
    ventas_region,
    x="Región",
    y="Venta_Total",
    color="Región",
    text="Venta_Total",
    title="Ventas Totales por Región"
)
fig3.show()

# 5 CLIENTES MÁS FRECUENTES
clientes_frecuentes = (
    df["Cliente"]
    .value_counts()
    .head(5)
    .reset_index()
    .rename(columns={"index": "Cliente", "Cliente": "Frecuencia"})
)
fig4 = px.bar(
    clientes_frecuentes,
    x="Cliente",
    y="Frecuencia",
    color="Cliente",
    text="Frecuencia",
    title="Top 5 Clientes más Frecuentes"
)
fig4.show()

# 6 HEATMAP DE CORRELACIÓN
plt.figure(figsize=(6, 4))
sns.heatmap(
    df[["Cantidad", "Precio_Unitario", "Venta_Total"]].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlación entre Variables Numéricas")
plt.tight_layout()
plt.show()

print("\n Tablero completo generado correctamente con KPIs y visualizaciones interactivas.")