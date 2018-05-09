# cat2csv

Forked from oscarfonts/catastro2postgis and upgraded to python3

## Requisitos:
Python3

Parsea y crea nuevas tablas .csv para cada una de las categorías definidas en los archivos .cat del ![Cadastro Español](https://www.sedecatastro.gob.es/)

## Funcionamiento

Sencillo script en Python3 para convertir archivos .CAT a tablas .csv, para cada una de las categorías.

- Descargar los archivos .py (cat2csv.py y catstruct.py) en una misma carpeta de trabajo
- Copiar en esta misma carpeta el archivo .CAT que se desee convertir a csv.
- Asegurarse que solo existe **un archivo .CAT** en la carpeta de trabajo
- Ejecutar el script, en consola de comandos desde la carpeta de trabajo

Linux

```cpp
python3 cat2csv.py
```
Testeado en entorno Linux. Pendiente de especificar el procedimiento necesario en Windows y IOS.
Abierto a sugerencias de ejecución en Windows

Ya podéis trabajar con los datos alfanuméricos de catastro en vuestro GisDesktop preferido!!
Siempre mejor si es en QGIS!! :) 
