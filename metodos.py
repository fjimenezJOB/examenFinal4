
class Logica:

    def __init__(self):
        pass

    def escribir(self, nombre, score):
        with open('scores.txt', 'w') as f:
            f.write(f'{nombre},{score}\n')
        f.close()

    def leer(self):
        with open('scores.txt', 'r') as f:
            for line in f:
                print(line)