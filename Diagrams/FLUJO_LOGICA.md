# Diagrama de flujo clase trabajadora


``` mermaid

flowchart TD
    A([Inicio]) --> B

    B["__init__(nombre, dinero, energia, trabajo)
    Inicializa atributos del objeto"]

    B --> C["set_dinero(nuevo_dinero)
    Setter: valida y modifica __dinero"]

    C --> D{nuevo_dinero mayor a 0}
    D -- Si --> E[Actualiza __dinero]
    D -- No --> F[Muestra mensaje de error]
    E --> G
    F --> G

    G["atributos()
    Muestra nombre, dinero, energia y trabajo"]

    G --> H["trabajar()
    Ingresa horas, suma dinero, resta energia"]

    H --> I{energia menor o igual a 0}
    I -- Si --> J[Energia = 0 y avisa al usuario]
    I -- No --> K[Muestra energia restante]
    J --> L
    K --> L

    L["ganancias()
    Productos vendidos, suma al dinero"]

    L --> M["descansar()
    Horas de sueno, recupera energia max 100"]

    M --> N["get_dinero()
    Getter: retorna el valor de __dinero"]

    N --> O([Fin])
    ```
