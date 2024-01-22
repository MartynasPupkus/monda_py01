while True:
    try:
        number = float(input('Write positive number:  '))
        if number <=0:
            raise ValueError('Number you wrote is negative')
        else:
            print('Thank you, your number: ', number)
            break
    except ValueError as error:
        print('ERROR!: ', error)