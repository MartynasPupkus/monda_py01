import pickle
import os
import pdb

class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __str__(self):
        return f"{self.vardas}, {self.amzius} metų"


class AgeError(ValueError):
    pass


if __name__ == '__main__':
    try:
        vardas = input('vardas:  ')
        amzius = int(input('metai:  '))
        if amzius > 100:
            raise ValueError('zmones tiek negyvena')
        if amzius < 0:
            raise ValueError('zmogus mire negimes')
    except Exception as error:
        print(f'klaida {error.__class__.__name__}: {error}')
        exit()

zmogus = Zmogus(
    input('vardas:  '),
    int(input('metai  ')),
)

ZMONES_FILE = 'MONDA_PY01'

if os.path.exists(ZMONES_FILE):
    with open(ZMONES_FILE, 'rb') as zmones_file:
        zmones = pickle.load()
        zmones = append(zmogus)
else:    
    zmones = [zmogus]

with open(ZMONES_FILE, 'wb'):
    pickle.dump(zmones, zmones_file)

print('---[ Visi zmones ]---')
for zmogus in zmones:
    print(zmogus)