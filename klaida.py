try:
    x = int(input("Įveskite pirmąjį skaičių: "))
    y = int(input("Įveskite antrąjį skaičių: "))
    rezultatas = x / y
    print("Rezultatas:", rezultatas)
except ValueError:
    print("Įvestas neteisingas skaičius")
except ZeroDivisionError:
    print("Negalima dalinti iš nulio")