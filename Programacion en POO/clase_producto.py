class producto:
    def __init__(self,precio, titulo, autor, editorial, año_de_edicion, preferencias):
        self.precio = precio
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.año_de_edicion = año_de_edicion
        self.preferencias = preferencias
        
    def vender (self):
        print(f"el producto {self.titulo} ha sido vendido por {self.precio}) ")
        
    def comprar (self):
        print(f"has comprado el producto {self.titulo} , del autor {self.autor}) ")    
        
    def ver_catalogo (self):
        print(f"catalogo de producto")    
        print(f"titulo= {self.titulo}")
        print(f"autor= {self.autor}")
        print(f"editorial= {self.editorial}")
        print(f"año_de_edicion= {self.año_de_edicion}")
        print(f"precio= {self.precio}")
        print(f"preferencias= {self.preferencias}")  
