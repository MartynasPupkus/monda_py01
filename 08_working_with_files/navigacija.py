import os
from datetime import datetime

print(os.getcwd())
os.chdir('08_working_with_files')
print(os.getcwd())

if os.path.exists('daiktai.txt'):
    with open('daiktai.txt', 'r') as daiktai_f:
        for line in daiktai_f:
            print(line, end='')
    print()
else:
    print('file is not there')

if not os.path.exists('siuksles'):
    os.makedirs('siuksles')
    with open('siuksles/siuksle', 'w') as siuksle:
        siuksle.write('xxx')
else:
    if os.path.exists('siuksles/siuksle'):
        os.remove('siuksles/siuksle')
    os.rmdir('siuksles')

os.chdir('..')
print(os.getcwd())
main_dir_content = os.listdir()
for item in main_dir_content:
    item_st = os.stat(item)
    print(f'{item[:29]:30} {item_st.st_size:>9} {datetime.fromtimestamp(item_st.st_ctime)}')

if os.path.exists('README.md'):
    readme_stats = os.stat('README.md')
    print(readme_stats.st_ctime)
    print(datetime.fromtimestamp(readme_stats.st_ctime))

import os

katalogo_kelias = "Mano_Katalogas"

if not os.path.exists(katalogo_kelias):
    os.makedirs(katalogo_kelias)
    print(f"Katalogas '{katalogo_kelias}' sukurtas.")

import os

dabartinis_katalogas = os.getcwd()
print(f"Dabartinis katalogas: {dabartinis_katalogas}")

print("Failai ir katalogai:")
for elementas in os.listdir(dabartinis_katalogas):
    print(elementas)

import os

failo_kelias = "testas.txt"


with open(failo_kelias, "w") as f:
    f.write("Tai yra testinis failas.")

# Patikrinkite, ar failas egzistuoja, ir trinkite jį
if os.path.exists(failo_kelias):
    os.remove(failo_kelias)
    print(f"Failas '{failo_kelias}' ištrintas.")
else:
    print(f"Failas '{failo_kelias}' neegzistuoja.")
