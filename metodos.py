import random
import time

gajos = ['1000€', '500€', 'PIERDE', '200€',
         '-50% Dinero', 'CALABOZO', 'DINERO X2']

class Logica:

        # Metodo que escribe el score en el archivo txt
    def escribir(self, nombre, score):

        ahora = time.strftime("%c")  # Fecha y hora actuales
        with open('scores.txt', 'w') as f:
            f.write(f'{nombre},{score},{ahora}\n')
        f.close()


        # Metodo que lee el txt
    def leer(self):
        with open('scores.txt', 'r') as f:
            for line in f:
                print(line)

        # Metodo que saca un gajo random y le añade los que el usuario haya elegido
    def random_opciones(self, opciones=[]):
        for opcion in range(6):
            gajos.append(opciones[opcion])
        elegido = gajos[random.randint(0, 13)]
        print (gajos)
        return elegido