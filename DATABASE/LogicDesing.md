# Base de Datos

¿Qué es una Base de Datos?

- Una base de datos es una conjunto organizado de informacion almacenada de forma estructurada en un sistema, para que pueda ser facilmente consultada, modificada y gestianada.
- Componentes claves:
    - Tablas: donde se guadan los datos(filas y columnas)
    - Registros: cada fila de la tabla (un dato especifico)
    - Campos: cada columna (un atributo del dato)
- Tipo más comunes:
    - Relacionales (SQL): Usan tablas vinculadas entre si. EJ: MySQL, PostgreSQL
    - No relacionales (NOSQL): Datos mas flexibles, sin estructura fija. EJ: MongoDB

En el ejemplo visto en clases, ¿Por qué es mejor usar FLOAT a cambio de INT en el ingreso del campo edad?,¿por qué ingresar edad en un sistema de base de datos no es recomendable y cual seria una mejor opcion en este caso justifique.

- Cuando se quieren registrar bebés o mascotas es mejor usar float ya que se contabiliza los meses, sim embargo es poco preciso y dificil de interpretar. La mejor forma es guadar fechas de nacimientos y calcular la edad exacta cuando se necesite. Asi obtenemos años, meses, y dias con precisión

El "Dato" vs. "Realidad": En la pizarra se propuso usar `FLOAT` con el valor `0.5` para representar a un cachorro de 6 meses. Si el sistema debe enviar un saludo automático de "Feliz Cumpleaños" cada año, ¿qué problema técnico enfrentaríamos si solo guardamos `0.5` y no la fecha de nacimiento (`DATE`)?

- 0,5 representa la mitad de un entero sin embargo un año tiene 12 meses por lo que a la hora de enviar el mensaje de feliz cumpleaños lo haria cada 5 meses . 

## Tabla ejemplo

![tabla](https://github.com/TamaMart/Recursos/blob/main/Imagenes/Martinez_tabla.jpeg?raw=true)

## MER ejemplo

![Flowchart](https://github.com/TamaMart/Recursos/blob/main/Imagenes/Martinez_mer.jpeg?raw=true)


1. Detección de Error:  Según lo aprendido en el video de cardinalidad

¿para qué tipo de relación se utiliza realmente una tabla intermedia como la que creamos en clase MASCOTA_TUTOR? justifique (máx. 10 líneas)


2. Contexto de Negocio: El autor del video menciona que las reglas varían según la organización.

Caso A:  Clínica Veterinaria Hogar: Una mascota solo puede tener un dueño responsable. (Defina la cardinalidad).

- Cardinalidad notación clasica: 1:1, como se indica **una** sola mascota puede tener **un solo  dueño**.
  
Caso B: Hotel de Mascotas Premium: Una mascota puede ser retirada por el padre, la madre o un tutor legal (Varios tutores) y un tutor puede tener varias mascotas. (Defina la cardinalidad).

- En este caso la cardinalidad es en notacion de minimos y maximos donde 1..N 


