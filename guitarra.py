class Guitarra:
    def __init__(self, marca, modelo, precio, estado = 'disponible', stock = 1):
        self.__marca = marca
        self.__modelo = modelo 
        self.__precio = precio
        self.__estado = estado 
        self.__stock = stock

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_precio(self):
        return self.__precio

    def get_estado(self):
        return self.__estado

    def get_stock(self):
        return self.__stock

    def vender(self, cantidad):
        if cantidad <= self.__stock:
            self.__stock -= cantidad
            return f'Se vendieron {cantidad} guitarras. Stock restante: {self.__stock}'
        else:
            return "No hay suficiente stock para vender."

    def reponer_stock(self, cantidad):
        self.__stock += cantidad
        return f'Stock actualizado: {self.__stock}'

    def aplicar_descuento(self, porcentaje):
        if porcentaje > 0 and porcentaje < 100:
            descuento = self.__precio * (porcentaje / 100)
            self.__precio -= descuento
            return f'Descuento aplicado. Precio nuevo: ${self.__precio:.2f}'
        else:
            return 'Porcentaje inválido.'

    def __str__(self):
        return (f'Guitarra: {self.__marca} {self.__modelo}\n'
                f'Precio: ${self.__precio}\n'
                f'Estado: {self.__estado}\n'
                f'Stock: {self.__stock}')