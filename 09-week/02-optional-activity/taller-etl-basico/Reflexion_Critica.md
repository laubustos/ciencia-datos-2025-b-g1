# Proyecto ETL - "EduSmart"

**Autor:** Laura Valentina Bustos Lupaco 
**Materia:** Ciencia de Datos  

---

## Conclusiones

- El uso de un archivo JSON permitió organizar los datos de estudiantes, cursos y matrículas de forma centralizada.  
- La fase de transformación fue clave para garantizar la calidad de los datos, eliminando duplicados y unificando formatos de fechas.  
- La métrica `costo_total` ofreció un valor agregado, facilitando el análisis de ingresos potenciales por estudiante.  
- El modelo de datos destino aseguró consistencia al integrar múltiples entidades en una sola tabla.  

---

## Reflexión Crítica

El principal reto fue la estandarización de fechas, que llegaron en diferentes formatos (YYYY-MM-DD, YYYY/MM/DD y DD-MM-YYYY).  
También hubo dificultades con valores nulos y duplicados en la tabla de estudiantes. Integrar cursos y matrículas requirió definir reglas claras de validación para evitar inconsistencias.  
El ejercicio mostró que, incluso en un escenario académico, un flujo ETL bien diseñado es esencial para generar información confiable para la toma de decisiones.
