# Pasos para instalar Postgres 9.5 en Windows

## 1. Descargar postgre desde el [link](https://www.enterprisedb.com/download-postgresql-binaries)  , y descargue la version 9.5.25

![1](https://github.com/TamaMart/Recursos/blob/main/DATABASE/Postgresql/pg_pasos/1.png?raw=true)

## 2. Descomprima el archivo 

![2](https://github.com/TamaMart/Recursos/blob/main/DATABASE/Postgresql/pg_pasos/2.png?raw=true)

## 3. Para instalar abra el terminal en la carpeta  **>pgsql**

![3](https://github.com/TamaMart/Recursos/blob/main/DATABASE/Postgresql/pg_pasos/3.png?raw=true)

## 4. En la terminal escriba lo siguiente:

- crear el CLUSTER de datos
```powershell
.\bin\initdb.exe -D DATA_MI_NOMBRE -U postgres -W -E UTF8
```
 - Cambie **DATA_MI_NOMBRE**  por el nombre de la data

![4](https://github.com/TamaMart/Recursos/blob/main/DATABASE/Postgresql/pg_pasos/4.png?raw=true)

- Le pedira crear una contraseña

![5](https://github.com/TamaMart/Recursos/blob/main/DATABASE/Postgresql/pg_pasos/5.png?raw=true)

al finalizar le mostrara este mensaje, y podremos iniciar servidor 

![6](https://github.com/TamaMart/Recursos/blob/main/DATABASE/Postgresql/pg_pasos/6.png?raw=true)

## 5. Iniciar el servidor:
 - escriba en la tarminal y cambien "DATA" por el nombre de su data:
   
 ```powershell
.\bin\pg_ctl.exe -D data -l logfile start
```

![7](https://github.com/TamaMart/Recursos/blob/main/DATABASE/Postgresql/pg_pasos/7.png?raw=true)

- verifique si funciona con:
```powershell
.\bin\pg_isready.exe
```
![8](https://github.com/TamaMart/Recursos/blob/main/DATABASE/Postgresql/pg_pasos/8.png?raw=true)

- Conectarse:
```powershell
.\bin\psql.exe -U postgres
```
![10](https://github.com/TamaMart/Recursos/blob/main/DATABASE/Postgresql/pg_pasos/9.png?raw=true)

## 6. Ejecutar pg admin
- en la carpeta > pgsql>bin busque el ejecutable **pgadmin3** e inicielo
 ![10](https://github.com/TamaMart/Recursos/blob/main/DATABASE/Postgresql/pg_pasos/10.png?raw=true)
![11](https://github.com/TamaMart/Recursos/blob/main/DATABASE/Postgresql/pg_pasos/11.png?raw=true)

## 7. Establecer conexion
- ha click en el icono de **add a connection to a server**
- se depliegara una ventana donde tendra que rellenar lo siguiente como se muestra en la imagen 
![12](https://github.com/TamaMart/Recursos/blob/main/DATABASE/Postgresql/pg_pasos/12.png?raw=true)

### y listo !! estara funcionando su base de datos 

![13](https://github.com/TamaMart/Recursos/blob/main/DATABASE/Postgresql/pg_pasos/13.png?raw=true)



  
  
