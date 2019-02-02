import web
import config as config

class Insert:
    def __init__(self):
        pass
    
    def GET(self):
        return config.render.insert() #Renderiza la pagina insert.html

    def POST(self):
        formulario = web.input() #Almacena los datos del formulario
        id = formulario['id']
        nombreProducto = formulario['nombreProducto']
        loteProducto = formulario['loteProducto']
        existenciaProducto = formulario['existenciaProducto']
        fechaCProducto = formulario['fechaCProducto']
        config.model_productos.insert_producto(id, nombreProducto, loteProducto, existenciaProducto, fechaCProducto) #Llama al metodo insert_cliente y le paso los datos guardados
        raise web.seeother('/productos') #rediercciona al index.html
