# TIPOS DE DATOS EN DATABASE 

1. Sobre el tipo CHAR:

¿Cuál es la característica principal del tipo de dato CHAR en cuanto a su almacenamiento y qué sucede si el contenido ingresado es menor a la longitud definida? (2:06 - 2:50)

CHAR siempre ocupa el número de bytes definidos en su declaración, sin importar la cantidad real de caracteres almacenados. Si el contenido es menor a la longitud definida, los bytes restantes se llenarán con espacios. Por ejemplo, si declaramos un CHAR de longitud 20 y guardamos "Hola", solo se ocuparán 4 bytes y los otros 16 se llenarán con espacios.


2. Sobre el tipo VARCHAR:

¿En qué se diferencia principalmente VARCHAR de CHAR y por qué se considera más eficiente para almacenar datos como nombres o direcciones? (3:03 - 3:40)

A diferencia de CHAR, VARCHAR(n) es de longitud variable. Es especialmente útil para guardar cadenas de caracteres de longitud muy variable como domicilios, nombres de empresas o personas. Tiene peor rendimiento que CHAR porque necesita almacenar información adicional sobre la longitud de cada registro, pero tiene la ventaja de guardar solo los caracteres presentes en lugar de rellenar con espacios.

3. Sobre el tipo TEXT:

¿Para qué tipo de escenarios está diseñado el tipo de dato TEXT y cuál es su ventaja respecto a la limitación de caracteres en comparación con los otros tipos vistos? (3:45 - 4:24)

TEXT está diseñado para texto que ocupa varias líneas, como artículos, descripciones largas o código. Su ventaja es que no tiene un límite de caracteres fijo como CHAR o VARCHAR, lo que lo hace ideal para contenido extenso e impredecible en longitud.

4. Análisis de caso práctico:

Si tuvieras que diseñar una base de datos para almacenar matrículas vehiculares que siempre tienen un formato estándar de 7 caracteres, ¿qué tipo de dato elegirías y por qué? (2:51 - 3:00)

Elegiría CHAR(7) porque se recomienda usar CHAR cuando la longitud del dato es fija y conocida de antemano. Una matrícula siempre tiene exactamente 7 caracteres, por lo que no hay desperdicio de espacio y además CHAR es más rápido que VARCHAR en cuanto a rendimiento, ya que se sabe de antemano cuál es la longitud de los datos.

5. Gestión de almacenamiento:

El video menciona que el rendimiento y la optimización son clave. ¿Qué riesgo existe al definir una longitud de caracteres excesivamente grande en un campo VARCHAR si los datos reales son pequeños? (4:44 - 4:55)

Usar VARCHAR(MAX) innecesariamente aumenta el tamaño de la tabla. Esto significa que la base de datos reserva más recursos de los necesarios, lo que puede afectar el rendimiento de las consultas y el uso de memoria, especialmente cuando hay millones de registros.
