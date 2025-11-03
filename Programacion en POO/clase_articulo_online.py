class articulo_online:
    def __init__(self, tema):
        self.tema=tema
        
    def publicar(self):
        print("publicando articulo en linea...")
        print(f"el articulo sobre {self.tema} ha sido publicado exitosamente.")