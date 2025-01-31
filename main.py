import radar
import medio
import blanco
import generador
import datetime
import detector


# DISCLAMER!!
# todo esta en castellano por razones didacticas
# pero DEBEN programar en INGLES
# uno nunca sabe quien puede leer su codigo

def main():

    # Intervalo de tiempo en el que vamos a medir
    tiempo_inicial = datetime.datetime(2016, 3, 5, 1)
    tiempo_final = datetime.datetime(2016, 3, 5, 10)

    import math
    # parametros del generador de senales
    amplitud = 0.2
    fase = 1
    frecuencia = 20*math.pi
    
    gen1=generador(amplitud,fase,frecuencia)
    #TODO construir un detector
    rad1=radar(generador,detector)

    # parametros para un blanco
    amplitud_de_frecuencia_del_blanco = amplitud + 100
    tiempo_inicial_del_blanco = datetime.datetime(2016, 3, 5, 2)
    tiempo_final_del_blanco = datetime.datetime(2016, 3, 5, 4)
    
    blanco1=blanco(amplitud_de_frecuencia_del_blanco, tiempo_inicial_del_blanco,\
                   tiempo_final_del_blanco)


    #TODO contruir un medio

    #TODO construir un radar

if __name__ == "__main__":
    main()
