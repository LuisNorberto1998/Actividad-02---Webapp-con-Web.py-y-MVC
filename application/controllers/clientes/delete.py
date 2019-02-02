import web
import config as config

class Delete:
    def __init__(self):
        pass

    def GET(self, id):
        cliente = config.model_clientes.select_nombre(id) #Selecciona el registro que coincida con id
        return config.render.delete(cliente) #Envia el registro y renderiza delete.html

    def POST(self, id):
        formulario = web.input() #Crea un objeto formulario con los datos enviados con el formulario
        id = formulario['id'] #Obtiene el nombre almacenado en el formulario
        config.model_clientes.delete_cliente(id) #Borra el registro en el formulario
        raise web.seeother('/clientes') #Reedirecciona a raiz