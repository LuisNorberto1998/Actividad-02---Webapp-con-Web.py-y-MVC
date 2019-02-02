import web
import config as config

class Delete:
    def __init__(self):
        pass

    def GET(self, id):
        producto = config.model_productos.select_producto(id) #Selecciona el registro que coincida con id
        return config.render.delete(producto) #Envia el registro y renderiza delete.html

    def POST(self, id):
        formulario = web.input() #Crea un objeto formulario con los datos enviados con el formulario
        id = formulario['id'] #Obtiene el nombre almacenado en el formulario
        config.model_productos.delete_producto(id) #Borra el registro en el formulario
        raise web.seeother('/productos') #Reedirecciona a raiz