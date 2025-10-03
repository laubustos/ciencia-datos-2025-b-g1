**Resumen Estructurado – Análisis y Solución con IA**

**Corte 1: Análisis y Solución con IA**

**Corte 2: Análisis, Codificación Propia y Apropiación de Modelos con IA**

---

**1. Análisis de Datos**

**Datos de Entrada:**

- **Programa**
  - Atributos: `codigo`, `nombre`

- **Materia**
  - Atributos: `codigo`, `nombre`, `semestre`, `codigo_programa`

- **Estudiante**
  - Atributos: `codigo`, `nombre`, `semestre`, `[codigo_materia]`, `nota`

**Estructura de Notas por Corte:**

- **Cortes 1 y 2**
  - Parcial: 70% (`0.7`)
  - Actividades: 15% (`0.15`)  
    - Compuesta por: `(taller + foro + quiz) / 3`
  - Certificación: 10% (`0.1`)
  - Autoevaluación: 2% (`0.02`)
  - Coevaluación: 3% (`0.03`)

- **Corte 3**
  - Parcial: 50% (`0.5`)
  - Actividades: 15% (`0.15`)
  - Certificación: 10% (`0.1`)
  - Autoevaluación: 2% (`0.02`)
  - Coevaluación: 3% (`0.03`)
  - Proyecto: 20% (`0.2`)

---

**2. Proceso de Cálculo de Nota Final (NDf)**

- **Corte 1 y 2**
  - **NDf =** Parcial + Actividades + Certificación + Autoevaluación + Coevaluación

- **Corte 3**
  - **NDf =** Parcial + Actividades + Certificación + Autoevaluación + Coevaluación + Proyecto

---

**3. Análisis de Impacto**

**Objetivo:**  
Observar el **nivel de impacto** de las notas asociadas a las actividades frente a la nota del parcial.

**Escenarios de Evaluación:**

- **Caso por Estudiante:**
  - Evaluación de **5 escenarios distintos** para observar cómo varían las notas finales según cambios en actividades y parciales.

- **Caso por Grupo:**
  - Evaluación de **2 escenarios generales** para analizar el impacto en conjunto.

**Datos de Entrada por Caso:**

- **Caso 1:**  
  - Datos requeridos: Nota y Materia

- **Caso 2:**  
  - Datos requeridos: Nota, Materia y Grupo

---

Este esquema permite realizar análisis comparativos y simular escenarios para evaluar la **incidencia de las actividades** (taller, foro, quiz) en la **nota final** en relación con el peso del **parcial**, particularmente útil para **tomar decisiones pedagógicas o estratégicas** en el proceso de evaluación y enseñanza.
