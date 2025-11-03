# CREAR CLASE

class usuario:
    
    def __init__(self, nombre, apellido, n_d_cuenta, direccion, login, password):
        self.nombre= nombre
        self.apellido = apellido
        self.n_d_cuenta= n_d_cuenta
        self.direccion= direccion
        self.login= login
        self.password= password
        
    def enviar_sugerencia(self):
        print("sugerencia enviada correctamente")
    
    def leer(self):
        print("el usuario esta leyendo el contenido solicitado")
    
    def comprar(self):
        print("compra realizada con exito")
    
    def vender(self):
        print("venta registrada correctamente")
    
    def realizar_reclamacion(self):
        print("reclamacion enviada. nuestro equipo la revisara pronto")  

    def mostrar_datos(self):
        print(f"(nombre: {self.nombre} {self.apellido}) - (cuenta: {self.n_d_cuenta}) - (direccion: {self.direccion}) - (datos del usuario: {self.login} {self.password}) ")