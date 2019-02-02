import web
import config as config

class View:
    def __init__(self):
        pass
    
    def GET(self, id):
        productos = config.model_productos.select_producto(id) #Selecciona el registro que coincida con id
        return config.render.view(productos) #Envia el registro y renderiza view.hmtl