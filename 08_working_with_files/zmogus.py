import pickle
import os 

class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __str__(self):
        return f"{self.vardas}, {self.amzius} metų"
    
zmogus = Zmogus(
    input('vardas:  '),
    int(input('metai  ')),
)

ZMONES_FILE = '08_working_with_files'

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