class editorial:
    def __init__(self, nombre, direccion, telefono):
        self.nombre= nombre
        self.direccion= direccion
        self.telefono= telefono
        
    def vender(self):
        print(f"(nombre: {self.nombre}) - (direccion: {self.direccion}) - (telefono: {self.telefono})")
        print("recopilando informacion del cliente...")
        print("venta realizada correctamente.")    