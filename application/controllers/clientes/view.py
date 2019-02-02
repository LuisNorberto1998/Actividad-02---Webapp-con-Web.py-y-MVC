import web
import config as config

class View:
    def __init__(self):
        pass
    
    def GET(self, id):
        cliente = config.model_clientes.select_nombre(id) #Selecciona el registro que coincida con id
        return config.render.view(cliente) #Envia el registro y renderiza view.hmtl