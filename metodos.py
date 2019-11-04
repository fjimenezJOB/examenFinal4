import random
import time

gajos = ['1000', '500', 'PIERDE', '200',
         '-50%Dinero', 'CALABOZO', 'DINEROX2']

bote = 0


class Logica:

    def __init__(self, saldo, score, saltar, ronda):
        self.ronda = ronda
        self.saldo = saldo
        self.score = score
        self.saltar = False

        # Metodo que escribe el registro de premios en el archivo txt

    def escribir_historico(self, premio):
        with open('registro.txt', 'a') as f:
            f.write(f'{premio}\n')
        f.close()

        # Metodo que lee el registro de premios en el archivo txt
    def leer_historico(self):
        historia = []
        with open('registro.txt', 'r') as f:
            for line in f:
                historia.append(line)
                return historia

    def escribir(self, nombre, score):
        ahora = time.strftime("%c")  # Fecha y hora actuales
        with open('scores.txt', 'a+') as f:
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

    def setBote(self, bote):
        bote = self.saldo

    def getBote(self):
        return bote

    def normas(self, suerte):
        self.saltar = False
        pierde = False
        if suerte == '1000':
            self.saldo = self.saldo + 1000
            self.score = self.score + 1000

        elif suerte == '500':
            self.saldo += 500
            self.score += 500

        elif suerte == 'PIERDE':
            self.saldo = 0
            pierde = True
            self.ronda = 0

        elif suerte == '200':
            self.saldo += 200
            self.score += 200

        elif suerte == '-50%Dinero':
            self.saldo /= 2
            self.score -= 100

        elif suerte == 'CALABOZO':
            self.saldo -= 1000
            self.score -= 100

        elif suerte == 'DINEROX2':
            self.saldo *= 2
            self.score *= 2

        elif suerte == 'saltar':
            self.score += 10000
            self.saltar = True

        elif suerte == 'coche':
            self.score = self.score + 10000

        elif suerte == '5000':
            self.saldo += 5000
            self.score += 5000
            self.ronda -= 1

        elif suerte == 'bote':
            self.score *= 2
            l.setBote(self, self.saldo)

        elif suerte == '100':

            self.saldo += 100
            self.score += 100

        elif suerte == 'botex2':
            self.saldo *= 2
            self.score += 1000

        elif suerte == 'moto':
            self.score *= 10

        elif suerte == 'bici':
            self.score += 1000

        elif suerte == 'pc':
            self.saldo -= 10
            self.score += 1000

        elif suerte == 'nevera':
            self.saldo -= 10
            self.score += 200

        self.ronda += 1
        l.escribir_historico(self, suerte)
        return self.saldo, self.score, self.ronda, self.saltar, pierde

    def getScore(self):
        return self.score


l = Logica
