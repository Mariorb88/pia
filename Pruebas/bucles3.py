v_cont = 0

while v_cont < 100:
    v_palabra = str(input('Indica la palabra secreta!'))
    
    if v_palabra == 'chupacabra':
        break
    else:
        print('Error!!! vuelve a intentarlo!!')
    
    
print('¡Has dejado el bucle con éxito')
    