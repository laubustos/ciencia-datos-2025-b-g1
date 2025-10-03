# Parcial Parte 1 – Planificación y Valoración de la Nota Definitiva

## Parte 1: Planteamiento de la solución (nota definitiva)
Realice la **planificación para calcular y mostrar la nota definitiva de cualquier materia**, considerando que todas comparten la siguiente distribución de calificaciones:

### Corte 1 y 2
- Parcial: **70%**  
- Actividades (Taller + Foro + Quiz): **15%**  
- Certificación: **10%**  
- Autoevaluación : **2%**  
- Coevaluación : **3%**

### Corte 3
- Parcial: **50%**  
- Proyecto: **50%**  
- Actividades (Taller + Foro + Quiz): **15%**  
- Certificación: **10%**  
- Autoevaluación : **2%**  
- Coevaluación : **3%**

La planificación debe dejar explícito cómo se integran estos componentes en un modelo que permita obtener la nota definitiva de cada materia, estudiante y corte académico.

---

## Parte 2: Caso para generar valor a la data
Además de calcular la nota, plantee un **caso de análisis que aporte valor agregado** a los datos académicos. Este caso debe ir acompañado de la **gráfica más adecuada** para evidenciarlo.  

Ejemplo orientador (no se puede reutilizar el mismo):  
> Obtener la línea de tendencia de las notas de los estudiantes en una materia, mostrando cómo evolucionan desde el inicio hasta el final de cada corte. Esto permite identificar el comportamiento global del grupo y no solo los resultados individuales.

> **Datos de entrada esperados:**
> - Identificador de la materia.
> - Listado de estudiantes.
> - Notas de cada componente (parcial, actividades, certificación, autoevaluaciones, proyecto).
> - Corte académico al que corresponde la nota.

> **Planificación paso a paso:**
> 1. Recolectar las calificaciones de todos los estudiantes para cada corte.
> 2. Calcular la nota definitiva por estudiante en cada corte usando la ponderación definida.
> 3. Obtener el promedio grupal de notas en cada corte.
> 4. Construir una serie temporal con los promedios (corte 1, corte 2, corte 3).
> 5. Representar los resultados en un gráfico de línea que muestre la tendencia global.
> 6. Interpretar el comportamiento: mejora, estabilidad o descenso en el rendimiento del grupo.

### Requisitos del caso propuesto
- Puede considerar **n materias, n grupos, n semestres o n programas académicos**.  
- Lo importante es que la redacción del caso muestre **cómo se genera valor real** a partir del planteamiento.  
- Indique qué **visualización** es más adecuada (ejemplo: gráfico de barras comparativas, boxplot de dispersión, mapa de calor, etc.) y justifique su elección.  

---

## Parte 3: Implementación y entrega
1. **Datos sintéticos**: genere un archivo `.csv` con información realista que respalde el caso planteado.  
2. **Demostración práctica**: grabe un video en el que se muestre:  
   - El estudiante en cámara.  
   - El código en vivo dentro de un notebook.  
   - La explicación paso a paso del proceso (step by step).  
3. **Publicación**:  
   - Suba el notebook a su repositorio (fork correspondiente).  
   - Adjunte en Moodle el archivo `.ipynb` y el enlace público al video.  

---

En esta redacción queda claro:  
- El **alcance técnico** (cálculo de nota definitiva).  
- El **valor analítico** (caso y gráfica).  
- La **ejecución práctica** (datos, notebook, video y entrega).  
