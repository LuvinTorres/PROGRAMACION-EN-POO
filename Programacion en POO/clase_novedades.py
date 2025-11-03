class novedades:
    def __init__(self, clasificacion, tema):
        self.clasificacion=clasificacion
        self.tema=tema
        
    def mostrar_novedades(self, nueva_calsificacion):
        print("cambiando clasificacion...")
        self.clasificacion= nueva_calsificacion
        print(f"la nueva clasificacion es: {self.clasificacion} ")