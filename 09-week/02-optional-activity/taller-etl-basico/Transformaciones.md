# Transformación - Proyecto EduSmart

## 1. Estudiantes
- **Eliminación de nulos:**  
  Se eliminaron los registros donde el campo `nombre` o `email` estuviera vacío, ya que son atributos esenciales para identificar al estudiante y mantener la calidad del dataset.  

- **Eliminación de duplicados:**  
  Algunos estudiantes aparecían más de una vez con el mismo `id_estudiante`. Se conservaron únicamente los registros únicos para evitar redundancia y conteos erróneos en los análisis.  

- **Nombres en mayúsculas:**  
  El campo `nombre` se normalizó a mayúsculas para estandarizar la representación de los datos y facilitar búsquedas o comparaciones posteriores.  

---

## 2. Cursos
- **Validación de precios positivos:**  
  Se revisó que el campo `costo` fuera mayor a cero. Cualquier valor negativo o nulo se consideró inconsistente y se corrigió/eliminó.  

- **Validación de duración positiva:**  
  El campo `duracion_semanas` se verificó para que tuviera valores mayores a cero, asegurando que los cursos reflejaran una duración académica real.  

---

## 3. Matrículas
- **Conversión de fechas a formato ISO:**  
  Las fechas venían en diferentes formatos (`YYYY-MM-DD`, `YYYY/MM/DD`, `DD-MM-YYYY`). Se unificaron todas al estándar ISO (`YYYY-MM-DD`) para mantener consistencia y permitir análisis temporales correctos.  

- **Validación de claves foráneas:**  
  Cada matrícula fue verificada para que el `id_estudiante` existiera en la tabla de estudiantes y el `id_curso` en la tabla de cursos, garantizando la integridad referencial de los datos.  

---

## 4. Integración
- **Unión de estudiantes, cursos y matrículas:**  
  Se integraron las tres entidades en una sola tabla destino (`matriculas_limpias`), combinando la información académica y de negocio en un único dataset unificado.  

- **Creación de campo `costo_total`:**  
  Se añadió una columna calculada `costo_total = costo * duracion_semanas`, lo que permite medir el ingreso potencial de cada matrícula según la duración del curso.  
