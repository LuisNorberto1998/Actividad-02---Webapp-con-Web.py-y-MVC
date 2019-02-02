import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, id):
        # Selecciona el registro que coincida con el id
        cliente = config.model_clientes.select_nombre(id)
        # Envia el registro y realiza el render
        return config.render.update(cliente)

    def POST(self, id):
        formulario = web.input()  # Almacena los datos del formulario
        id = formulario['id']
        nombreCliente = formulario['nombreCliente']
        apellidoPC = formulario['apellidoPC']
        apellidoMC = formulario['apellidoMC']
        telefonoCliente = formulario['telefonoCliente']
        emailCliente = formulario['emailCliente']
        config.model_clientes.update_cliente(id, nombreCliente, apellidoPC, apellidoMC, telefonoCliente, emailCliente) #Llama al metodo insert_cliente y le paso los datos guardados
        raise web.seeother('/clientes') #rediercciona al index.html
