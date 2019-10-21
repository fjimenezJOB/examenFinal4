import random
import time

gajos = ['1000', '500', 'PIERDE', '200',
         '-50%Dinero', 'CALABOZO', 'DINEROX2']

class Logica:

    def __init__(self, saldo, score, saltar, ronda):
        self.ronda = ronda
        self.saldo = saldo
        self.score = score
        self.saltar = False

        # Metodo que escribe el score en el archivo txt

    def escribir_historico(self, premio):
        with open('registro.txt', 'a') as f:
            f.write(f'{premio}\n')
        f.close()

    def leer_historico(self):
        historia = []
        with open('registro.txt', 'r') as f:
            for line in f:
                historia.append(line)
                return historia


    def escribir(self, nombre, score):

        ahora = time.strftime("%c")  # Fecha y hora actuales
        with open('scores.txt', 'w') as f:
            f.write(f'{nombre},{score},{ahora}\n')
        f.close()

        # Metodo que lee el txt

    def leer(self):
        lineas = []
        with open('scores.txt', 'r') as f:
            for line in f:
                lineas.append(line)
                return lineas

    def añadir_opciones(self, opciones=[]):
        for opcion in range(6):
            gajos.append(opciones[opcion])

        # Metodo que saca un gajo random y le añade los que el usuario haya elegido

    def random(self):
        elegido = gajos[random.randint(0, 13)]
        return elegido

    def normas(self, suerte):
        pierde = False
        if suerte == '1000':
            self.saldo = self.saldo + 1000
            self.score = self.score + 1000
            self.ronda = self.ronda + 1
            self.saltar = False
        elif suerte == '500':
            self.saldo = self.saldo + 500
            self.score = self.score + 500
            self.ronda = self.ronda + 1
            self.saltar = False
        elif suerte == 'PIERDE':
            self.saldo = 0
            self.ronda = self.ronda + 1
            pierde = True
            self.saltar = False
        elif suerte == '200':
            self.saldo = self.saldo + 200
            self.score = self.score + 200
            self.ronda = self.ronda + 1
            self.saltar = False
        elif suerte == '-50%Dinero':
            self.saldo = self.saldo / 2
            self.score = self.score - 100
            self.ronda = self.ronda + 1
            self.saltar = False
        elif suerte == 'CALABOZO':
            self.saldo = self.saldo - 1000
            self.score = self.score - 100
            self.ronda = self.ronda + 1
            self.saltar = False
        elif suerte == 'DINEROX2':
            self.saldo = self.saldo * 2
            self.score = self.score * 2
            self.ronda = self.ronda + 1
            self.saltar = False
        elif suerte == 'saltar':
            
            self.score = self.score + 10000
            self.saltar = True
            self.ronda = self.ronda + 1
        elif suerte == 'coche':
                
            self.score = self.score + 10000
            self.ronda = self.ronda + 1
            self.saltar = False
        elif suerte == '5000':
            self.saldo = self.saldo + 5000
            self.score = self.score + 5000
            self.ronda = self.ronda + 1
            self.saltar = False
        elif suerte == 'bote':
            self.score = self.score * 2
            self.ronda = self.ronda + 1
            self.saltar = False
            bote = self.saldo
        elif suerte == '100':
            self.saldo = self.saldo + 100
            self.score = self.score + 100
            self.ronda = self.ronda + 1
            self.saltar = False
        elif suerte == 'botex2':
            self.saldo = self.saldo * 2
            self.score = self.score + 1000
            self.ronda = self.ronda + 1
            self.saltar = False
        elif suerte == 'moto':

            self.score = self.score * 10
            self.ronda = self.ronda + 1
            self.saltar = False
        elif suerte == 'bici':

            self.score = self.score + 1000
            self.ronda = self.ronda + 1
            self.saltar = False
        elif suerte == 'pc':

            self.score = self.score + 1000
            self.ronda = self.ronda + 1
            self.saltar = False

        elif suerte == 'nevera':

            self.saldo = self.saldo - 1
            self.score = self.score + 200
            self.ronda = self.ronda + 1
            self.saltar = False
        l.escribir_historico(self,suerte)
        return self.saldo, self.score, self.ronda, self.saltar, pierde

l = Logica