#!/usr/bin/python
# -*- coding: utf-8 -*-

# Estructura de los ficheros .cat
# 2019-01-15

# Transposicion literal de la especificacion (salvo error u omision):
# http://www.catastro.meh.es/pdf/formatos_intercambio/catastro_fin_cat_2006.pdf
# Añadido 5 campo con acronimos aptos para Oracle. Tablas 1 , 11 , 14 , 15 (Referencias catastrales urbanas)


catstruct = {}
catstruct[1] = [
    [3, 1, 'X', 'tipo_entidad_generadora', 'TEG'],
    [4, 9, 'N', 'codigo_entidad_generadora', 'CEG'],
    [13, 27, 'X', 'nombre_entidad_generadora', 'NEG'],
    [40, 8, 'N', 'fecha_generacion_fichero', 'FGF'],
    [48, 6, 'N', 'hora_generacion_fichero', 'HGF'],
    [54, 4, 'X', 'tipo_fichero', 'TF'],
    [58, 39, 'X', 'descripcion_contenido_fichero', 'DCF'],
    [97, 21, 'X', 'nombre_fichero', 'NOM_FICH'],
    [118, 3, 'N', 'codigo_entidad_destinataria', 'CE_DEST'],
    [121, 8, 'N', 'fecha_inicio_periodo', 'FECHA_INI'],
    [129, 8, 'N', 'fecha_finalizacion_periodo', 'FECHA_FIN']
]

# 11 - Registro de Finca
catstruct[11] = [
    [24, 2, 'N', 'codigo_delegacion_meh', 'COD_DELE_MEH'],
    [26, 3, 'N', 'codigo_municipio_dgc', 'COD_MUNI_DGC'],
    [31, 14, 'X', 'parcela_catastral', 'REFCAT'],
    [51, 2, 'N', 'codigo_provincia_ine', 'COD_PROV'],
    [53, 25, 'X', 'nombre_provincia', 'NOM_PROV'],
    [78, 3, 'N', 'codigo_municipio_dgc_2', 'PRIMER_NUM_P'],
    [81, 3, 'N', 'codigo_municipio_ine', 'COD_MUNI_INE'],
    [84, 40, 'X', 'nombre_municipio', 'NOM_MUNI'],
    [124, 30, 'X', 'nombre_entidad_menor', 'NOM_ENT_MEN'],
    [154, 5, 'N', 'codigo_via_publica_dgc','COD_VP'],
    [159, 5, 'X', 'tipo_via','TIPO_VIA'],
    [164, 25, 'X', 'nombre_via', 'NOMBRE_VIA'],
    [189, 4, 'N', 'primer_numero_policia', 'PRIMER_NUM_P'],
    [193, 1, 'X', 'primera_letra', 'PRIM_LETRA'],
    [194, 4, 'N', 'segundo_numero_policia', 'SEGUNDO_NUM_P' ],
    [198, 1, 'X', 'segunda_letra', 'SEGUN_LETRA'],
    [199, 5, 'N', 'kilometro_por_cien', 'KM_POR_CIEN'],
    [204, 4, 'X', 'bloque', 'BLOQUE'],
    [216, 25, 'X', 'direccion_no_estructurada', 'DIR_NO_E'],
    [241, 5, 'N', 'codigo_postal', 'CP'],
    [246, 2, 'X', 'distrito_municipal', 'DIST_MUNI'],
    [248, 3, 'N', 'codigo_municipio_origen_caso_agregacion_dgc','COD_MUN_OCAD' ],
    [251, 2, 'N', 'codigo_zona_concentracion', 'COD_ZC'],
    [253, 3, 'N', 'codigo_poligono','COD_POLI'],
    [256, 5, 'N', 'codigo_parcela', 'COD_PARCE'],
    [261, 5, 'X', 'codigo_paraje_dgc', 'COD_PARAJE'],
    [266, 30, 'X', 'nombre_paraje', 'NOM_PARAJE'],
    [296, 10, 'N', 'superficie_finca_o_parcela_catastral_m2', 'SUP_M2'],
    [306, 7, 'N', 'superficie_construida_total', 'SUP_CONST_TOT'],
    [313, 7, 'N', 'superficie_construida_sobre_rasante', 'SUP_CONST_SR'],
    [320, 7, 'N', 'superficie_construida_bajo_rasante', 'SUP_CONST_BR'],
    [327, 7, 'N', 'superficie_cubierta', 'SUP_CUBIERTA'],
    [334, 9, 'N', 'coordenada_x_por_cien', 'COOR_X_100'],
    [343, 10, 'N', 'coordenada_y_por_cien', 'COOR_Y_100'],
    [582, 20, 'X', 'referencia_catastral_bice', 'REF_CAT_BICE'],
    [602, 65, 'X', 'denominacion_bice', 'DENO_BICE'],
    [667, 10, 'X', 'codigo_epsg', 'EPSG']
]

# 13 - Registro de Unidad Constructiva
catstruct[13] = [
    [24, 2, 'N', 'codigo_delegacion_meh','COD_DELE_MEH'],
    [26, 3, 'N', 'codigo_municipio_dgc', 'COD_MUNI_DGC'],
    [29, 2, 'X', 'clase_unidad_constructiva', 'CL_UN_CONST'],
    [31, 14, 'X', 'parcela_catastral', 'REFCAT'],
    [45, 4, 'X', 'codigo_unidad_constructiva', 'UND_CONST'],
    [51, 2, 'N', 'codigo_provincia_ine', 'COD_PROV'],
    [53, 25, 'X', 'nombre_provincia', 'NOM_PROV'],
    [78, 3, 'N', 'codigo_municipio_dgc_2', 'COD_MUNI_2'],
    [81, 3, 'N', 'codigo_municipio_ine', 'COD_MUN_INE'],
    [84, 40, 'X', 'nombre_municipio', 'NOM_MUNI'],
    [124, 30, 'X', 'nombre_entidad_menor', 'NOM_ENT_MEN'],
    [154, 5, 'N', 'codigo_via_publica_dgc', 'COD_VIA_PUB'],
    [159, 5, 'X', 'tipo_via', 'TIPO_VIA'],
    [164, 25, 'X', 'nombre_via', 'NOMBRE_VIA'],
    [189, 4, 'N', 'primer_numero_policia', 'PRIMER_NUM_P'],
    [193, 1, 'X', 'primera_letra', 'PRIM_LETRA'],
    [194, 4, 'N', 'segundo_numero_policia', 'SEGUNDO_NUM_P'],
    [198, 1, 'X', 'segunda_letra', 'SEGUN_LETRA'],
    [199, 5, 'N', 'kilometro_por_cien', 'KM_POR_CIEN'],
    [216, 25, 'X', 'direccion_no_estructurada', 'DIR_NO_E'],
    [296, 4, 'N', 'anyo_construccion', 'ANYO_CONST'],    
    [300, 1, 'X', 'exactitud_anyo_construccion', 'EXCT_A_CONST'], #'E', '+', '-', 'C'
    [301, 7, 'N', 'superficie_suelo_ocupado', 'SUP_SUELO_O'],
    [308, 5, 'N', 'longitud_fachada_cm', 'LONG_F'],
    [410, 4, 'X', 'codigo_unidad_constructiva_matriz', 'COD_UC_MATRIZ']
]

# 14 - Registro de Construccion
catstruct[14] = [
    [24, 2, 'N', 'codigo_delegacion_meh','COD_DELE_MEH'],
    [26, 3, 'N', 'codigo_municipio_dgc', 'COD_MUNI_DGC'],
    [31, 14, 'X', 'parcela_catastral', 'REFCAT'],
    [45, 4, 'N', 'numero_orden_elemento_construccion', 'NUM_OEC'],
    [51, 4, 'X', 'codigo_unidad_constructiva_asociada', 'COD_UCA'],
    [59, 4, 'X', 'bloque', 'BLOQUE'],
    [63, 2, 'X', 'escalera', 'ESCALERA'],
    [65, 3, 'X', 'planta', 'PLANTA'],
    [68, 3, 'X', 'puerta', 'PUERTA'],
    [71, 3, 'X', 'codigo_destino_dgc', 'COD_DES_DGC'],
    [74, 1, 'X', 'tipo_reforma_o_rehabilitacion', 'TIPO_ROR'], # 'R', 'O', 'E', 'I', ''
    [75, 4, 'N', 'anyo_reforma', 'ANYO_RE' ],
    [79, 4, 'N', 'anyo_antiguedad_efectiva_catastro', 'ANY_ANT_EF'],
    [83, 1, 'X', 'indicador_local_interior', 'IND_LI'], # 'S', 'N'
    [84, 7, 'N', 'superficie_total_efectos_catastro_m2', 'SUPE_TEC'],
    [91, 7, 'N', 'superficie_porches_y_terrazas_m2', 'SUP_PYT'],
    [98, 7, 'N', 'superficie_imputable_en_otras_plantas_m2', 'SUP_IOP'],
    [105, 5, 'X', 'tipologia_constructiva', 'TIP_CONST'],
    [112, 3, 'X', 'modalidad_reparto_elementos_comunes', 'MOD_REC']
]

# 15 - Registro de Inmueble
catstruct[15] = [
    [24, 2, 'N', 'codigo_delegacion_meh','COD_DELE_MEH'],
    [26, 3, 'N', 'codigo_municipio_dgc', 'COD_MUNI_DGC'],
    [29, 2, 'X', 'clase_bien_inmueble', 'CL_B_INM'],
    [31, 14, 'X', 'parcela_catastral', 'REFCAT'],
    [45, 4, 'N', 'numero_secuencia_en_parcela', 'NUM_SE_PAR'],
    [49, 1, 'X', 'primer_caracter_control', 'PCC'],
    [50, 1, 'X', 'segundo_caracter_control','SCC'],
    [51, 8, 'N', 'numero_fijo_bien_inmueble', 'NUM_F_BINM'],
    [59, 15, 'X', 'identificacion_inmueble_segun_ayuntamiento', 'ID_INM_AY'],
    [74, 19, 'X', 'numero_finca_registral', 'NUM_F_CAT'],
    [93, 2, 'N', 'codigo_provincia_ine', 'COD_PROV'],
    [95, 25, 'X', 'nombre_provincia', 'NOM_PROV'],
    [120, 3, 'N', 'codigo_municipio_dgc_2', 'COD_MUNI_2'],
    [123, 3, 'N', 'codigo_municipio_ine', 'COD_MUNI_DGC'],
    [126, 40, 'X', 'nombre_municipio', 'NOM_MUNI'],
    [166, 30, 'X', 'nombre_entidad_menor', 'NOM_ENT_MEN' ],
    [196, 5, 'N', 'codigo_via_publica_dgc', 'COD_VP'],
    [201, 5, 'X', 'tipo_via', 'TIPO_VIA'],
    [206, 25, 'X', 'nombre_via', 'NOMBRE_VIA'],
    [231, 4, 'N', 'primer_numero_policia', 'PRIMER_NUM_P'],
    [235, 1, 'X', 'primera_letra', 'PRIM_LETRA'],
    [236, 4, 'N', 'segundo_numero_policia', 'SEGUNDO_NUM_P'],
    [240, 1, 'X', 'segunda_letra', 'SEGUN_LETRA'],
    [241, 5, 'N', 'kilometro_por_cien', 'KM_POR_CIEN'],
    [246, 4, 'X', 'bloque', 'BLOQUE'],
    [250, 2, 'X', 'escalera', 'ESCALERA'],
    [252, 3, 'X', 'planta', 'PLANTA'],
    [255, 3, 'X', 'puerta', 'PUERTA'],
    [258, 25, 'X', 'direccion_no_estructurada','DIR_NO_E'],
    [283, 5, 'N', 'codigo_postal', 'CP'],
    [288, 2, 'X', 'distrito_municipal', 'DIST_MUNI'],
    [290, 3, 'N', 'codigo_municipio_origen_caso_agregacion_dgc', 'COD_MUN_OCAD'],
    [293, 2, 'N', 'codigo_zona_concentracion', 'COD_ZC'],
    [295, 3, 'N', 'codigo_poligono', 'COD_POLI'],
    [298, 5, 'N', 'codigo_parcela', 'COD_PARCE'],
    [303, 5, 'X', 'codigo_paraje_dgc', 'COD_PARAJE'],
    [308, 30, 'X', 'nombre_paraje', 'NOM_PARAJE'],
    [368, 4, 'X', 'numero_orden_inmueble_en_escritura', 'NUM_OIE'],
    [372, 4, 'N', 'anyo_antiguedad_inmueble', 'ANY_ANT_INM'],
    [428, 1, 'X', 'clave_uso', 'CLAVE_USO'], # Ver cod_usos.csv
    [442, 10, 'N', 'superficie_construida_m2', 'SUP_CONS_M2'],
    [452, 10, 'N', 'superficie_asociada_m2', 'SUP_ASO_M2'],
    [462, 9, 'N', 'coeficiente_propiedad_en_cienmillonesimas_partes', 'COEF_PRO']
]

# 16 - Registro de reparto de elementos comunes
#catstruct[16] = [
#    [24, 2, 'N', 'codigo_delegacion_meh'],
#    [26, 3, 'N', 'codigo_municipio_dgc'],
#    [31, 14, 'X', 'parcela_catastral'],
#    [45, 4, 'N', 'numero_elemento'],
#    [49, 2, 'X', 'calificacion_catastral_subparcela_abstracta'],
#    [51, 4, 'N', 'numero_orden_segmento']
#    # Aqui hay un bloque que se repite hasta 15 veces, y que nos saltamos
#]
#
## 17 - Registro de cultivos
#catstruct[17] = [
#    [24, 2, 'N', 'codigo_delegacion_meh'],
#    [26, 3, 'N', 'codigo_municipio_dgc'],
#    [29, 2, 'X', 'naturaleza_suelo_ocupado'], # 'UR' urbana, 'RU' rustica
#    [31, 14, 'X', 'parcela_catastral'],
#    [45, 4, 'X', 'codigo_subparcela'],
#    [51, 4, 'N', 'numero_orden_fiscal_en_parcela'],
#    [55, 1, 'X', 'tipo_subparcela'], # 'T' terreno, 'A' absracta, 'D' dominio publico
#    [56, 10, 'N', 'superficie_subparcela_m2'],
#    [66, 2, 'X', 'calificacion_catastral_o_clase_cultivo'],
#    [68, 40, 'X', 'denominacion_clase_cultivo'],
#    [108, 2, 'N', 'intensidad_productiva'],
#    [127, 3, 'X', 'codigo_modalidad_reparto'] # [TA]C[1234]
#]
#
## 46 - Registro de situaciones finales de titularidad
#catstruct[46] = [
#    [24, 2, 'N', 'codigo_delegacion_meh'],
#    [26, 3, 'N', 'codigo_municipio_dgc'],
#    [29, 2, 'X', 'naturaleza_suelo_ocupado'], # 'UR' urbana, 'RU' rustica
#    [31, 14, 'X', 'parcela_catastral'],
#    [45, 4, 'X', 'codigo_subparcela'],
#    [49, 1, 'X', 'primer_carac_control'],
#    [50, 1, 'X', 'segundo_carac_control'],
#    [51, 2, 'X', 'codigo_derecho'],
#    [53, 5, 'N', 'porcentage_derecho'],
#    [58, 3, 'N', 'ordinal_derecho'],
#    [61, 9, 'X', 'nif_titular'],
#    [70, 60, 'X', 'nombre_titular'], # Primer apellido, segundo y nombre o razón social
#    [130, 1, 'X', 'motivo_no_nif'], # 1 Extranjero, 2 menor de edad, 9 otras situaciones
#    [131, 2, 'N', 'codigo_provincia_ine'],
#    [133, 25, 'X', 'nombre_provincia'],
#    [158, 3, 'N', 'codigo_municipio_dgc'],
#    [161, 3, 'N', 'codigo_municipio_ine'],
#    [164, 40, 'X', 'nombre_municipio'],
#    [204, 30, 'X', 'nombre_entidad_menor'],
#    [235, 5, 'N', 'codigo_via_publica_dgc'],
#    [239, 5, 'X', 'tipo_via'],
#    [244, 25, 'X', 'nombre_via'],
#    [269, 4, 'N', 'primer_numero_policia'],
#    [273, 1, 'X', 'primera_letra'],
#    [274, 4, 'N', 'segundo_numero_policia'],
#    [278, 1, 'X', 'segunda_letra'],
#    [279, 5, 'N', 'kilometro_por_cien'],
#    [284, 4, 'X', 'bloque'],
#    [288, 2, 'X', 'escalera'],
#    [290, 3, 'X', 'planta'],
#    [293, 3, 'X', 'puerta'],
#    [296, 25, 'X', 'direccion_no_estructurada'],
#    [321, 5, 'N', 'codigo_postal'],
#    [326, 5, 'N', 'apartado_correos'],
#    [331, 9, 'X', 'nif_conyuge'],
#    [340, 9, 'X', 'nif_cb'],
#    [349, 20, 'X', 'complemento_titularidad']
#]
#
## 47 - Registro de comunidad de bienes formalmente constituida presente en una situación final
#catstruct[47] = [
#    [24, 2, 'N', 'codigo_delegacion_meh'],
#    [26, 3, 'N', 'codigo_municipio_dgc'],
#    [29, 2, 'X', 'naturaleza_suelo_ocupado'], # 'UR' urbana, 'RU' rustica
#    [31, 14, 'X', 'parcela_catastral'],
#    [45, 4, 'X', 'codigo_subparcela'],
#    [49, 1, 'X', 'primer_carac_control'],
#    [50, 1, 'X', 'segundo_carac_control'],
#    [51, 9, 'X', 'nif_comunidad_bienes'],
#    [60, 60, 'X', 'denominacion_razon_socil'],
#    [120, 2, 'N', 'codigo_provincia_ine'],
#    [122, 25, 'X', 'nombre_provincia'],
#    [147, 3, 'N', 'codigo_municipio_dgc'],
#    [150, 3, 'N', 'codigo_municipio_ine'],
#    [153, 40, 'X', 'nombre_municipio'],
#    [193, 30, 'X', 'nombre_entidad_menor'],
#    [223, 5, 'N', 'codigo_via_publica_dgc'],
#    [228, 5, 'X', 'tipo_via'],
#    [233, 25, 'X', 'nombre_via'],
#    [258, 4, 'N', 'primer_numero_policia'],
#    [262, 1, 'X', 'primera_letra'],
#    [263, 4, 'N', 'segundo_numero_policia'],
#    [267, 1, 'X', 'segunda_letra'],
#    [268, 5, 'N', 'kilometro_por_cien'],
#    [273, 4, 'X', 'bloque'],
#    [277, 2, 'X', 'escalera'],
#    [279, 3, 'X', 'planta'],
#    [282, 3, 'X', 'puerta'],
#    [285, 25, 'X', 'direccion_no_estructurada'],
#    [310, 5, 'N', 'codigo_postal'],
#    [315, 5, 'N', 'apartado_correos']
#]
#
## 90 - Registro de cola
#catstruct[90] = [
#    [10, 7, 'N', 'numero_registros_tipo_11'],
#    [24, 7, 'N', 'numero_registros_tipo_13'],    
#    [31, 7, 'N', 'numero_registros_tipo_14'],
#    [38, 7, 'N', 'numero_registros_tipo_15'],
#    [45, 7, 'N', 'numero_registros_tipo_16'],
#    [52, 7, 'N', 'numero_registros_tipo_17'],
#    [59, 7, 'N', 'numero_registros_tipo_46'],
#    [66, 7, 'N', 'numero_registros_tipo_47']
#]
#
