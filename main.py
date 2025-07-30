from guitarra import Guitarra

def menu():
    guitarra = Guitarra('Fender', 'Stratocaster', 150000, estado = 'nueva', stock=5)

    while True:
        print('\n--- MENÚ GUITARRA ELÉCTRICA ---')
        print('1. Ver información de la guitarra')
        print('2. Vender guitarra')
        print('3. Reponer stock')
        print('4. Aplicar descuento')
        print('5. Ver stock actual')
        print('6. Ver precio actual')
        print('7. Salir')

        opcion = input('Selecciona una opción: ')

        if opcion == '1':
            print(guitarra)

        elif opcion == '2':
            try:
                cantidad = int(input('¿Cuántas guitarras querés vender?: '))
                print(guitarra.vender(cantidad))
            except ValueError:
                print('Ingresá un número válido.')

        elif opcion == '3':
            try:
                cantidad = int(input('¿Cuántas guitarras querés agregar al stock?: '))
                print(guitarra.reponer_stock(cantidad))
            except ValueError:
                print('Ingresá un número válido.')

        elif opcion == '4':
            try:
                porcentaje = float(input('¿Qué porcentaje de descuento querés aplicar?: '))
                print(guitarra.aplicar_descuento(porcentaje))
            except ValueError:
                print('Ingresá un número válido.')

        elif opcion == '5':
            print(f'Stock actual: {guitarra.get_stock()}')

        elif opcion == '6':
            print(f'Precio actual: ${guitarra.get_precio()}')

        elif opcion == '7':
            print('¡Gracias por usar el sistema!')
            break

        else:
            print('Opción inválida. Intentá de nuevo.')

if __name__ == '__main__':
    menu()
