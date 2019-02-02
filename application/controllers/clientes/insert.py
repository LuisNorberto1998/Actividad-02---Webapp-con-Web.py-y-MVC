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
        nombreCliente = formulario['nombreCliente']
        apellidoPC = formulario['apellidoPC']
        apellidoMC = formulario['apellidoMC']
        telefonoCliente = formulario['telefonoCliente']
        emailCliente = formulario['emailCliente']
        config.model_clientes.insert_cliente(id, nombreCliente, apellidoPC, apellidoMC, telefonoCliente, emailCliente) #Llama al metodo insert_cliente y le paso los datos guardados
        raise web.seeother('/clientes') #rediercciona al index.html
