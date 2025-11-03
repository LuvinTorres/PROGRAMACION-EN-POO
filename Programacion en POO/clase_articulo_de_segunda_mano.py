class articulo_de_segunda_mano:
    def __init__(self, clasificacion, tema, vendedor):
        self.clasificacion=clasificacion
        self.tema=tema
        self.vendedor=vendedor
        
    def mostrar_datos_articulo(self):
        print(f"clasificacion: {self.clasificacion}")
        print(f"tema: {self.tema}")
        print(f"vendedor: {self.vendedor}")