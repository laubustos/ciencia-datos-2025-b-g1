# Documento Explicativo del Tablero de Ventas

## 1. Descripción del Proyecto
El presente tablero fue desarrollado en Python con el propósito de analizar el comportamiento de las ventas de una empresa ficticia colombiana. 
El objetivo principal fue aplicar los principios de visualización efectiva, empleando librerías como Plotly, Matplotlib y Seaborn, 
para obtener métricas clave y descubrir tendencias relevantes dentro de los datos.

## 2. Dataset Utilizado
Se utilizó un dataset simulado denominado **dataset_ventas_colombia.csv**, compuesto por 100 registros de ventas en las regiones de Neiva, Bogotá, Cali, Medellín y Barranquilla.  
Las columnas incluidas fueron:
- Fecha  
- Región  
- Cliente  
- Producto  
- Categoría  
- Cantidad  
- Precio Unitario  
- Venta Total  

Este conjunto de datos permitió analizar patrones mensuales, desempeño regional y comportamiento de los productos.

## 3. Métricas Principales
Se definieron las siguientes métricas (KPIs) para el tablero:
- **Ventas Totales:** Monto total vendido durante el periodo.  
- **Promedio Mensual:** Promedio de ventas mensuales.  
- **Clientes Únicos:** Número de clientes diferentes registrados.  
- **Productos:** Total de productos comercializados.  

Estas métricas resumen el estado general del negocio y permiten evaluar su rendimiento.

## 4. Visualizaciones Desarrolladas
El tablero incluye un conjunto de visualizaciones que cumplen con los requerimientos del taller:

1. **KPIs visuales:** Cuatro indicadores numéricos con Plotly (`go.Indicator`), mostrando las métricas clave del negocio.  
2. **Gráfico de barras comparativo:** Representa el Top 5 de productos más vendidos.  
3. **Serie temporal:** Muestra la evolución de las ventas a lo largo de los meses.  
4. **Gráfico por región:** Presenta la distribución total de ventas en cada ciudad.  
5. **Gráfico de clientes frecuentes:** Indica los clientes con mayor número de compras.  
6. **Mapa de calor de correlación:** Creado con Seaborn, muestra la relación entre cantidad, precio y venta total.

Cada visualización permite identificar información relevante y patrones de comportamiento en el negocio.

## 5. Justificación de Diseño
El diseño del tablero se basó en criterios de **claridad y simplicidad**:
- Se usó un esquema de colores contrastante y legible.  
- Las visualizaciones de Plotly permiten interactividad (zoom, hover, exportar, etc.).  
- Se eligió el formato horizontal de KPIs para emular el estilo de Power BI.  
- Las gráficas de barras y líneas fueron priorizadas por su fácil interpretación y comparación.  

Esta estructura facilita la toma de decisiones al permitir identificar los productos más rentables, los meses más activos y las regiones con mejor desempeño.

## 6. Conclusión
El tablero cumple con los objetivos planteados en el taller, ya que integra análisis descriptivo, métricas clave y visualizaciones efectivas.  
El uso de librerías de Python permitió obtener un producto interactivo, claro y visualmente atractivo, ideal para la comunicación de resultados y la toma de decisiones empresariales.