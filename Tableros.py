# Creamos los tableros del juego
import numpy as np

"""Para establecer los ejes hemos creado un array de 12 por 12, dandole a los valores de los bordes con slicing 
el valor de la lista fila. Después se han hecho copias de este tablero para establecer el resto de tableros del juego"""

filas = [" ",'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'," "]
tab_respuesta_humano= np.full((12,12), " ")
tab_respuesta_humano[0]=filas
tab_respuesta_humano[:,0]=filas
tab_respuesta_humano[-1]=filas
tab_respuesta_humano[:,-1]=filas
tab_vacio_humano=tab_respuesta_humano.copy()
tab_respuesta_bot=tab_respuesta_humano.copy()
tab_vacio_bot=tab_respuesta_humano.copy()