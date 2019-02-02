import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, id):
        # Selecciona el registro que coincida con el id
        producto = config.model_productos.select_producto(id)
        # Envia el registro y realiza el render
        return config.render.update(producto)

    def POST(self, id):
        formulario = web.input()  # Almacena los datos del formulario
        id = formulario['id']
        nombreProducto = formulario['nombreProducto']
        loteProducto = formulario['loteProducto']
        existenciaProducto = formulario['existenciaProducto']
        fechaCProducto = formulario['fechaCProducto']
        # Llama al metodo insert_cliente y le paso los datos guardados
        config.model_productos.update_producto(
            id, nombreProducto, loteProducto, existenciaProducto, fechaCProducto)
        raise web.seeother('/productos')  # rediercciona al index.html
