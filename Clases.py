import numpy as np
from Tableros import tab_vacio_humano, tab_respuesta_bot, tab_respuesta_humano, tab_vacio_bot

#Vamos a definir dos cases, la clase barco y la clase jugadores
class Barco:
    def __init__(self,tipo,eslora):
        """
        En el constructor de la clase barco se definen los atributos de los mismos tales como el tipo de barco (según su tamaño),
        las coordenadas donde se situarán en el tablero (self.x y self.y), que son aleatorias, y la dirección que tendrá (horizontal
        o vertical), también aleatoria. El constructor recibe por parámetros el tipo de barco y la eslora (lo que ocupan).
        """
        self.tipo=tipo
        self.eslora=eslora
        self.x=np.random.randint(0,11)+1
        self.y=np.random.randint(0,11)+1
        self.dire= np.random.randint(2) #0=Vertical, 1=Horizontal
    def colocarbarco(self,tablero):
        """
        Este método se encarga de colocar los barcos en el tablero, para lo que se tiene en cuenta su tipo y dirección. Se colocarán
        siempre y cuando no haya otros barcos en esa posición y teniendo en cuenta la longitud del tablero (impidiendo que estos no
        puedan salirse del tablero). Se utilizará la letra F para las fragatas (1 eslora), la D para los destructores (2 esloras), A
        para los acorazados (3 esloras) y P para e portavión (4 esloras). Este método recibe por parámetro el tablero donde se colocarán.
        """
        while True:
            if self.tipo=="Fragata":
                if tablero[self.x,self.y]==" ":
                    tablero[self.x,self.y]="F"
                    break
                else:
                    self.x=np.random.randint(0,11)+1
                    self.y=np.random.randint(0,11)+1
            elif self.tipo=="Destructor":
                if self.dire ==0 and self.x<=9 and np.all(tablero[self.x:self.x+2,self.y]==" "):
                    tablero[self.x:self.x+2,self.y]="D"
                    break
                elif self.dire ==1 and self.y<=9 and np.all(tablero[self.x,self.y:self.y+2]==" "):
                    tablero[self.x,self.y:self.y+2]="D"
                    break
                else:
                    self.x=np.random.randint(0,11)+1
                    self.y=np.random.randint(0,11)+1
            elif self.tipo == "Acorazado":
                if self.dire ==0 and self.x<=8 and np.all(tablero[self.x:self.x+3,self.y]==" "):
                    tablero[self.x:self.x+3,self.y]="A"
                    break
                elif self.dire ==1 and self.y<=8 and np.all(tablero[self.x,self.y:self.y+3]==" "):
                    tablero[self.x,self.y:self.y+3]="A"
                    break
                else:
                    self.x=np.random.randint(0,11)+1
                    self.y=np.random.randint(0,11)+1
            elif self.tipo == "Portaviones":
                if self.dire ==0 and self.x<=7 and np.all(tablero[self.x:self.x+4,self.y]==" "):
                    tablero[self.x:self.x+4,self.y]="P"
                    break
                elif self.dire ==1 and self.y<=7 and np.all(tablero[self.x,self.y:self.y+4]==" "):
                    tablero[self.x,self.y:self.y+4]="P"
                    break
                else:
                    self.x=np.random.randint(0,11)+1
                    self.y=np.random.randint(0,11)+1
class Jugadores:
    def __init__(self,jugador):
        """
        El constructor de la clase Jugadores guarda como atributos el jugador que jugará al juego, que se indicará como parámetro,
        y las coordenadas que utilizará ese jugador para atacar al tablero enemigo (self.x_1 y self.x_2), que por defecto no existirán.
        También tendrá por atributos una serie de mensajes que por defecto no existirán que se utilizarán posteriormente en el método atacar.
        """
        self.jugador=jugador
        self.x_1=None
        self.y_1=None
        self.mensaje_fragata=False
        self.mensaje_destructor=False
        self.mensaje_acorazado=False
        self.mensaje_portavi=False
        self.mensaje_fragata_ene=False
        self.mensaje_destructor_ene=False
        self.mensaje_acorazado_ene=False
        self.mensaje_portavi_ene=False

    def atacar(self,tablero_respuesta,tablero_vacio):
        """
        El método atacar se encargará de lanzar los disparos a los barcos del jugador enemigo y tendrá en cuenta si el jugador es
        el jugador principal o la consola. Las coordenadas de disparo se pediran al usuario mediante un input, mientras que si el
        turno es de la consola, estas coordenas se darán de forma aleatoria. En función de si el jugador acierta o no, el método
        imprimirá por pantalla si el disparo ha caído en agua, lo cual finalizará el turno del jugador, o si, por el contrario, acierta,
        lo cual permitirá al jugador seguir jugando. También se avisará al jugador cuándo se destruyen todos los barcos de un tipo, o, por
        el contrario, cuándo la consola se los destruye a él
        """
        while True:
            if self.jugador=="Humano":
                if np.count_nonzero(tablero_respuesta == "X") == 20:
                    break
                if (np.count_nonzero(tab_respuesta_bot == "F") == 0) and not self.mensaje_fragata_ene:
                    self.mensaje_fragata_ene=True
                    print("Has destruido todas las Fragatas!")
                if (np.count_nonzero(tab_respuesta_bot == "D") == 0) and not self.mensaje_destructor_ene:
                    self.mensaje_destructor_ene=True
                    print("Has destruido todos los Destructores!")
                if (np.count_nonzero(tab_respuesta_bot == "A") == 0) and not self.mensaje_acorazado_ene:
                    self.mensaje_acorazado_ene=True
                    print("Has destruido todos los Acorazados!")
                if (np.count_nonzero(tab_respuesta_bot == "P") == 0) and not self.mensaje_portavi_ene:
                    self.mensaje_portavi_ene=True
                    print("Has destruido todos los Portaviones!")
                if np.count_nonzero(tablero_respuesta == "X") == 0 and np.count_nonzero(tablero_respuesta == "-") == 0:
                    print ("TABLERO DE ATAQUE")
                    print (tab_vacio_humano)
                    print ("----------------")
                    print ("TABLERO DE BARCOS")
                    print (tab_respuesta_humano)

                self.x_1=int(input("Introduzca un valor de la fila entre 0-9:"))+1
                self.y_1=int(input("Introduzca un valor de la columna entre 0-9:"))+1
                if tablero_respuesta[self.x_1,self.y_1] == "-":
                    print(f"Ya has atacado la coordenada ({(self.x_1)-1},{(self.y_1)-1}) y es agua, intentalo de nuevo")
                    continue
                elif tablero_respuesta[self.x_1,self.y_1] == "X":
                    print(f"Ya has atacado la coordenada ({(self.x_1)-1},{(self.y_1)-1}) y es un barco, intentalo de nuevo")
                    continue
                if tablero_respuesta[self.x_1,self.y_1] != " " and tablero_respuesta[self.x_1,self.y_1] != "-":
                    tablero_vacio[self.x_1,self.y_1]="X"
                    tablero_respuesta[self.x_1,self.y_1]="X"
                    print(f"Has atacado la coordenada ({(self.x_1)-1},{(self.y_1)-1}): Tocado")
                    print ("TABLERO DE ATAQUE")
                    print (tab_vacio_humano)
                    print ("----------------")
                    print ("TABLERO DE BARCOS")
                    print (tab_respuesta_humano)
                    continue
                elif tablero_respuesta[self.x_1,self.y_1] == " ":
                    tablero_vacio[self.x_1,self.y_1]="-"
                    tablero_respuesta[self.x_1,self.y_1]="-"
                    print(f"Has atacado la coordenada ({(self.x_1)-1},{(self.y_1)-1}): Agua")
                    print ("TABLERO DE ATAQUE")
                    print (tab_vacio_humano)
                    print ("----------------")
                    print ("TABLERO DE BARCOS")
                    print (tab_respuesta_humano)
                    break
            else:
                self.x_1=(np.random.randint(0,10))+1
                self.y_1=(np.random.randint(0,10))+1
                if np.count_nonzero(tablero_respuesta == "X") == 20:
                    break
                if (np.count_nonzero(tab_respuesta_humano == "F") == 0) and not self.mensaje_fragata:
                    self.mensaje_fragata=True
                    print("Has perdido todas las Fragatas!")
                if (np.count_nonzero(tab_respuesta_humano == "D") == 0) and not self.mensaje_destructor:
                    self.mensaje_destructor=True
                    print("Has perdido todos los Destructores!")
                if (np.count_nonzero(tab_respuesta_humano == "A") == 0) and not self.mensaje_acorazado:
                    self.mensaje_acorazado=True
                    print("Has perdido todos los Acorazados!")
                if (np.count_nonzero(tab_respuesta_humano == "P") == 0) and not self.mensaje_portavi:
                    self.mensaje_portavi=True
                    print("Has perdido todos los Portaviones!")

                if tablero_respuesta[self.x_1,self.y_1] == " ":
                    tablero_vacio[self.x_1,self.y_1]="-"
                    tablero_respuesta[self.x_1,self.y_1]="-"
                    print(f"La coordenada del bot es: ({(self.x_1)-1},{(self.y_1)-1}): Agua")
                    print ("TABLERO DE ATAQUE")
                    print (tab_vacio_humano)
                    print ("----------------")
                    print ("TABLERO DE BARCOS")
                    print (tab_respuesta_humano)
                    break
                elif tablero_respuesta[self.x_1,self.y_1] == "-":
                    continue
                elif tablero_respuesta[self.x_1,self.y_1] == "X":
                    continue
                elif tablero_respuesta[self.x_1,self.y_1] != " " and tablero_respuesta[self.x_1,self.y_1] != "-":
                    tablero_vacio[self.x_1,self.y_1]="X"
                    tablero_respuesta[self.x_1,self.y_1]="X"
                    print(f"La coordeanda del bot es:({(self.x_1)-1},{(self.y_1)-1}) Tocado")
                    print ("TABLERO DE ATAQUE")
                    print (tab_vacio_humano)
                    print ("----------------")
                    print ("TABLERO DE BARCOS")
                    print (tab_respuesta_humano)
                    continue