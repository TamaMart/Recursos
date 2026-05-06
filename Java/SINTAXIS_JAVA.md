# Sintaxis Java


## Texto:

```java
public class Main { // Creamos una clase Main
    public static void main(String[] args) { // Declaramos variables de tipo String
        String libro = "El Quijote";  // Declaramos una variable de tipo String para el título del libro
        String autor = "Miguel de Cervantes";  // Declaramos una variable de tipo String para el nombre del autor
        
    }
}
```

## Numeros:

```java
class Main { 
    public static void main(String[] args) { // Declaramos variables de tipo entero y decimal
        int entero = 100;  // Declaramos una variable de tipo entero para almacenar un número entero
        double decimal = 3.14; // Declaramos una variable de tipo decimal para almacenar un número decimal
    }
}
```

## Booleans:

```java
class Main {
    public static void main(String[] args) { // Declaramos variables de tipo booleano
        boolean autorizado = true;  // Declaramos una variable de tipo booleano para indicar si el usuario está autorizado
        boolean seleccionado = false; // Declaramos una variable de tipo booleano para indicar si un elemento está seleccionado
    }
}
```

## Lista:

```java
class Main {  
    public static void main(String[] args) { // Creamos un ArrayList de tipo Integer
       ArrayList<Integer> numeros = new ArrayList<Integer>(); // Agregamos elementos al ArrayList
       numeros.add(23);   // Agregamos elementos al ArrayList
       numeros.add(45);        
       numeros.add(16);
       numeros.add(37);
       System.out.println(numeros.get(0));// Imprimimos el primer elemento del ArrayList
    }
}   
```
## Objeto:
```java
import java.util.HashMap; // importamos la clase HashMap para poder utilizarla en nuestro programa

public class Main {
    public static void main(String[] args) { // método principal donde se ejecuta el programa
        HashMap<Integer, String> jugadores = new HashMap<Integer, String>();    // creamos un objeto HashMap llamado jugadores que almacena claves de tipo Integer y valores de tipo String
        jugadores.put(10, "Lionel Messi"); // agregamos un par clave-valor al HashMap, donde la clave es 10 y el valor es "Lionel Messi"    
        jugadores.put(7, "Cristiano Ronaldo");
        System.out.println(jugadores.get (7))   ;// imprimimos el valor asociado a la clave 7, que es "Cristiano Ronaldo"

```

# Hashmap

¿Qué es un HashMap?

Un HashMap es una estructura de datos que almacena información en pares clave → valor, como un diccionario. Permite buscar, agregar y eliminar datos de forma muy rápida.

¿Para qué se utiliza?

- Guardar datos asociados, por ejemplo: nombre del estudiante → nota
- Buscar información rápidamente sin recorrer toda una lista
- Contar ocurrencias de elementos

cómo se importa? 

 Utilizamos: 
 ```java
 import java.util.HashMap; // importamos la clase HashMap para poder utilizarla en nuestro programa
```

Ejemplo de codigo:

```java

import java.util.HashMap;

public class Main {
    public static void main(String[] args) {

        HashMap<String, Integer> notas = new HashMap<>();

        // Agregar datos
        notas.put("Tamara", 95);
        notas.put("Carlos", 80);
        notas.put("María", 70);

        // Obtener un valor
        System.out.println(notas.get("Tamara")); // → 95

        // Recorrer el HashMap
        for (String nombre : notas.keySet()) {
            System.out.println(nombre + ": " + notas.get(nombre));
        }
    }
}

```




