# Actividad 2: Diseño de Base de datos

## Creación de base de datos de una libreria

Trabajo realizado por Alvaro Neira y Tamara Martinez

## Imagen del ejercicio como boceto

NORMALIZACIÓN 3FN Y RELACIONES
![normalizacion](https://github.com/TamaMart/Recursos/blob/main/Imagenes/normalizacion%203fn.jpg?raw=true)

TABLAS

![TABLA1](https://github.com/TamaMart/Recursos/blob/main/Imagenes/tabla%201%203fn.jpg?raw=true)
![TABLA2](https://github.com/TamaMart/Recursos/blob/main/Imagenes/tabla%202%203fn.jpg?raw=true)






## Preguntas :

- ¿Que formas normales uso y por que?


  R: 0 FN: Comenzamos con todos los datos mezclados en una sola tabla sin organizar.
  
   1 FN: Eliminamos grupos repetitivos, separamos cada libro en su propia fila, de modo que cada celda tuviera un solo valor.
  
   2 FN: Eliminamos dependecias parciales, separamos CLIENTES en su propia tabla. EL nombre del cliente dependia solo del ID_CLIENTE, no de toda la PK compuesta.
  
   3 FN: Eliminamos dependencia transitiva, separamos categorias y tipo_pago en su propia tabla. Categoria dependia de libro, no directamente de la PK.
  

- ¿Cual fue la parte más compleja de resolver y por qué?
  

R: Normalizar la tabla a 3FN, ya que primero teniamos que normalizarla a 2FN y ademas teniamos que evitar que los atributos no principales dependan transitivamente del atributo clave.
Tambien identificar las relaciones entre los atributos.


- ¿Que tablas aún le faltaría a su sistema para producción y por qué?
  

R: Nos faltaria la tabla AUTORES, ya que al buscar un libro solo lo categorizamos por genero.


  
