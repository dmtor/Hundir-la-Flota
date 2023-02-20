import numpy as np
from Clases import Barco,Jugadores
from Tableros import tab_respuesta_bot, tab_respuesta_humano, tab_vacio_bot, tab_vacio_humano

#Se instancian todos los barcos, para que puedan colocarse en el tablero
Fragata1=Barco("Fragata",1)
Fragata2=Barco("Fragata",1)
Fragata3=Barco("Fragata",1)
Fragata4=Barco("Fragata",1)
Destructor1=Barco("Destructor",2)
Destructor2=Barco("Destructor",2)
Destructor3=Barco("Destructor",2)
Acorazado1=Barco("Acorazado",3)
Acorazado2=Barco("Acorazado",3)
Portavion=Barco("Portaviones",4)
Fragata1_Ene=Barco("Fragata",1)
Fragata2_Ene=Barco("Fragata",1)
Fragata3_Ene=Barco("Fragata",1)
Fragata4_Ene=Barco("Fragata",1)
Destructor1_Ene=Barco("Destructor",2)
Destructor2_Ene=Barco("Destructor",2)
Destructor3_Ene=Barco("Destructor",2)
Acorazado1_Ene=Barco("Acorazado",3)
Acorazado2_Ene=Barco("Acorazado",3)
Portavion_Ene=Barco("Portaviones",4)

#Se instancian los jugadores que jugarán la partida (el jugador principal y la consola)
Humano=Jugadores("Humano")
Bot=Jugadores("Bot")

#Se colocan los barcos tanto en el tablero del jugador principal, como en el tablero del enemigo mediante una llamada y un bucle for:
llamada=[Fragata1,Fragata2,Fragata3,Fragata4,Destructor1,Destructor2,Destructor3,
        Acorazado1,Acorazado2,Portavion]
for i in llamada:
    i.colocarbarco(tab_respuesta_humano)
llamada_Ene=[Fragata1_Ene,Fragata2_Ene,Fragata3_Ene,Fragata4_Ene,Destructor1_Ene,Destructor2_Ene,Destructor3_Ene,
        Acorazado1_Ene,Acorazado2_Ene,Portavion_Ene]
for i in llamada_Ene:
    i.colocarbarco(tab_respuesta_bot)

#Se crea un bucle While que dará vueltas siempre cuando no exista ningún tablero con todos los barcos derribados


print("""

██╗  ██╗██╗   ██╗███╗   ██╗██████╗ ██╗██████╗     ██╗      █████╗     ███████╗██╗      ██████╗ ████████╗ █████╗     
██║  ██║██║   ██║████╗  ██║██╔══██╗██║██╔══██╗    ██║     ██╔══██╗    ██╔════╝██║     ██╔═══██╗╚══██╔══╝██╔══██╗    
███████║██║   ██║██╔██╗ ██║██║  ██║██║██████╔╝    ██║     ███████║    █████╗  ██║     ██║   ██║   ██║   ███████║    
██╔══██║██║   ██║██║╚██╗██║██║  ██║██║██╔══██╗    ██║     ██╔══██║    ██╔══╝  ██║     ██║   ██║   ██║   ██╔══██║    
██║  ██║╚██████╔╝██║ ╚████║██████╔╝██║██║  ██║    ███████╗██║  ██║    ██║     ███████╗╚██████╔╝   ██║   ██║  ██║    
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚══════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝    

""")

while True:

    if np.count_nonzero(tab_vacio_bot == "X") == 20:
        print("Lo siento, has perdido")
        break
    if np.count_nonzero(tab_vacio_humano == "X") ==20:
        print ("¡Enhorabuena! Has ganado")
        break
    else:
        print("Es el turno del jugador")
        Humano.atacar(tab_respuesta_bot,tab_vacio_humano)
        
        print("Es el turno del bot")
        Bot.atacar(tab_respuesta_humano,tab_vacio_bot)
        

