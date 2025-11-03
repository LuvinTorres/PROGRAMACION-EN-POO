class procesador:
    def mandar_datos_de_venta(self):
        producto= input("ingrese el nombre del producto: ")
        cantidad= int(input("ingrese la cantidad: "))
        precio= float(input("ingrese el precio del producto: "))
        total= cantidad*precio
        print (f"producto: {producto}")
        print (f"cantidad vendida: {cantidad} ")
        print (f"precio: {precio} ")
        print (f"total: {total}")
                
    def mandar_articulo_online(self):
        print("procesando pedido....")
        print("veridicando direccion de envio.... ")
        print("empaquetando producto....")
        print("enviando articulo al transportista...")
        print("articulo enviado con exito.")
        
    def enviar_sugerencia_al_administrador(self):     
        print(input("tiene alguna sugerencia para enviarnos?: "))
        
    def modificar_stock(self):
        print("stock modificado correctamente. ")    
        
    def realizar_cobro(self): 
        print("calculando el total de la compra...")
        print("generando factura...")
        print("cobro realizado correctamente.")        
        
    def realizar_pago(self):
        print("procesando pago....")    
        print("verificando datos del cliente.....")
        print("pago realizado correctamente.")
        
    def actualizar_catalogo(self):
        print("actualizando catalogo....")
        print("catalogo actualizado correctamente. ") 
        
    def realizar_busqueda(self):
        print("buscando producto en el catalogo...")
        print("producto encontrado. ")