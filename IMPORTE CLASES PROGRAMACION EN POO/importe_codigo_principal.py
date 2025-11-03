# Se importan las clases

from clase_usuario import usuario
from clase_producto import producto
from clase_servidor import servidor
from clase_indexador import indexador
from clase_procesador import procesador
from clase_hilo import hilo
from clase_recolector import recolector
from clase_editorial import editorial
from clase_libro import libro
from clase_revista import revista
from clase_articulo_de_segunda_mano import articulo_de_segunda_mano
from clase_novedades import novedades
from clase_articulo_online import articulo_online

#codigo principal

obj_usuario = usuario("andres", "torres", "13982773", "niza", "luvin706,", " 124556787")
obj_usuario.mostrar_datos()
obj_usuario.enviar_sugerencia()
obj_usuario.leer()
obj_usuario.comprar()
obj_usuario.vender()
obj_usuario.realizar_reclamacion()
obj_producto = producto(precio= "135.000", titulo= "cien años de soledad",  autor= "gabriel garcia marquez", editorial="editorial sudamericana", año_de_edicion="1967", preferencias="novela latinoamericana")
obj_producto.vender()
obj_producto.comprar()
obj_producto.ver_catalogo()
obj_servidor = servidor()
mostrar= obj_servidor.mostrar_pagina()
print(mostrar)
sug= obj_servidor.enviar_sugerencia()
print(sug)
datos= obj_servidor.envia_datos_de_compra()
print(datos)
venta= obj_servidor.envia_datos_de_venta()
print(venta)
obj_indexador= indexador()
actualizar= obj_indexador.actualiza_almacen()
print(actualizar)
enviar=obj_indexador.envia_resultado_busqueda()
print(enviar)
obj_datos= procesador()
obj_datos.mandar_datos_de_venta()
obj_datos.mandar_articulo_online()
obj_datos.enviar_sugerencia_al_administrador()
obj_datos.modificar_stock()
obj_datos.realizar_cobro()
obj_datos.realizar_pago()
obj_datos.actualizar_catalogo()
obj_datos.realizar_busqueda()
obj_hilo= hilo()
obj_hilo.busca_novedades()
obj_recolector= recolector()
obj_recolector.envia_novedades()
obj_editorial= editorial("andres", "av 15ce b.n", "3214537865")
obj_editorial.vender()
obj_libro= libro("fantasia")
print("genero del libro: ", obj_libro.genero)
obj_revista= revista("literatura")
print("categoria: ", obj_revista.categoria)
obj_articulo= articulo_de_segunda_mano("realismo magico", "obra literaria", "libreria central")
obj_articulo.mostrar_datos_articulo()
obj_novedad= novedades("ficcion", "lanzamientos literarios")
obj_novedad.mostrar_novedades("realismo magico")
obj_art_online= articulo_online("nuevas tendencias en literatura digital")
obj_art_online.publicar()
