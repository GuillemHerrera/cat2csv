#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import csv


from catstruct import catstruct # define la estructura de un .CAT

	
#inputfile=sys.argv[1]
#basedir=sys.argv[2]
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))+'/'
#pathFoldCAT = os.path.join(__location__, '')
#print (__location__)
#print(pathFoldCAT)
pathFileCAT = ''
for file in os.listdir(__location__):
	#print(file)
	if '.CAT' in file:
		pathFileCAT = os.path.join(__location__, file)
		break
	#else:
	#	break

inputfile=pathFileCAT
basedir=__location__+'Categoria'

rf = open(inputfile, encoding='latin-1') # input file
wf = {}              # output files

# Generamos un CSV por cada tipo de registro
for tipo in catstruct:
    filename = basedir+'CAT_'+str(tipo)+'.csv'
    print ('Creando ' + filename)
    wf[tipo] = open(filename, 'w')
    # Escribimos primer registro con nombres de campos
    csv.writer(wf[tipo]).writerow(i[3]for i in catstruct[tipo])

# Leemos .cat registro a registro
for line in rf.readlines():
    line = (line.encode('utf-8')).decode('utf-8')
    #line=unicode(line, errors='replace')
    row = []
    tipo = int(line[0:2])
    # Parseamos si conocemos la estructura del tipo de registro
    if tipo in catstruct:
        for campos in catstruct[tipo]:
            ini = campos[0]-1 # offset
            fin = ini + campos[1] # longitud
            valor = (line[ini:fin].strip().encode("utf-8")).decode('utf-8') # valor
            row.append(valor)
        csv.writer(wf[tipo]).writerow(row)

# close input file handle
rf.close()  

# close output file handles
for f in wf:
    wf[f].close()