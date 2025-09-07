# Documento Comparativo – Arquitecturas Big Data

## 1. Escenario  
El caso de análisis será **Banca**, un sector que procesa:  
- Millones de transacciones electrónicas en tiempo real (transferencias, pagos, retiros).  
- Datos históricos de clientes (créditos, inversiones, cuentas de ahorro).  
- Información de seguridad y fraudes (patrones de comportamiento sospechoso).  
- Datos no estructurados provenientes de interacciones en canales digitales (chatbots, correo electrónico, redes sociales).  

El reto principal es manejar grandes volúmenes de información financiera con **seguridad, rapidez en el análisis y escalabilidad**, para mejorar la experiencia del cliente, prevenir fraudes y cumplir normativas del sector.  



## 2. Introducción  

### Propósito  
Comparar tres arquitecturas Big Data (Hadoop, Spark y Nube) evaluando sus componentes, ventajas, limitaciones y aplicaciones en el sector bancario, con el fin de determinar la más adecuada para este escenario.  

### Alcance  
El análisis se centrará en:  
- **Hadoop:** modelo clásico basado en HDFS, YARN y MapReduce.  
- **Apache Spark:** plataforma de procesamiento en memoria con soporte batch y streaming.  
- **Arquitecturas en la nube (ej. AWS, GCP, Azure):** servicios gestionados con escalabilidad y seguridad integrada.  

### Glosario  
- **HDFS:** sistema distribuido para almacenar grandes volúmenes de datos financieros.  
- **YARN:** gestor de recursos en Hadoop.  
- **MapReduce:** modelo de programación batch.  
- **RDD:** dataset distribuido tolerante a fallos en Spark.  
- **ETL:** proceso de extracción, transformación y carga de datos.  
- **Escalabilidad automática:** capacidad de la nube para ajustar recursos según la demanda.  

---

## 3. Descripción de arquitecturas  

### a) Hadoop  
- **Componentes:** HDFS, YARN, MapReduce, Hive, HBase.  
- **Ventaja:** almacenamiento económico y confiable de historiales de transacciones y auditorías.  
- **Limitación:** latencia alta, no apto para monitoreo en tiempo real de fraudes.  

### b) Apache Spark  
- **Componentes:** Spark Core, RDD, Spark SQL, MLlib, Streaming.  
- **Ventaja:** análisis en tiempo real de transacciones y detección de fraudes con baja latencia.  
- **Limitación:** requiere clústeres potentes con mayor capacidad de memoria.  

### c) Arquitecturas en la nube  
- **Componentes:** servicios gestionados (AWS EMR, BigQuery, Azure Synapse), auto-escalado, data lakes.  
- **Ventaja:** escalabilidad inmediata, integración con IoT financiero y seguridad avanzada.  
- **Limitación:** dependencia del proveedor y costos variables.