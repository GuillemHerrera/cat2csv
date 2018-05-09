# cat2csv

Forked from oscarfonts/catastro2postgis and upgraded to python3

## Requisitos:
Python3

Parsea y crea nuevas tablas .csv para cada una de las categorias definidas en los archivos .cat del ![Cadastro Español](https://www.sedecatastro.gob.es/)

## Funcionamiento

Sencillo script en Python3 para convertir archivos .CAT a tablas .csv, para cada una de las categorias.

- Descargar los archivos .py (cat2csv.py y catstruct.py) en una misma carpeta de trabajo
- Copiar en esta misma carpeta el archivo .CAT que se desee convertir a csv. 
- Asegurarse que solo exite **un archivo .CAT** en la carpeta de trabajo
- Ejecutar el script, en consola de comandos desde la carpeta de trabajo

Linux

```cpp
python3 cat2csv.py
```


Ya podeis trabajar con los datos alfanumericos de cadastro en vuestro GisDesktop preferido!! 
Siempre mejor si és en QGIS!! :) 
