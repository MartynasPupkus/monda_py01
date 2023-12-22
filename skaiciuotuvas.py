print('paskaiciuokime')
number1 = float(input('pirmas numeris: '))
number2 = float(input('antras numeris: '))
print('ka noretumet suskaiciuoti?')
operation = input('operation (+ , - , * , / ): ')
if operation == '+':
    print('rezultatas: ', number1 + number2)
elif operation == '-':
    print('rezultatas: ', number1 - number2)
elif operation == '*':
    print('rezultatas: ', number1 * number2)
elif operation == '/':
    print('rezultatas: ', number1 / number2)
else:
    print('KLAIDA: neteisinga operacija')