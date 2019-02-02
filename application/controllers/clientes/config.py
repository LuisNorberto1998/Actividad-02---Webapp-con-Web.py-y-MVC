import web
import application.models.model_clientes as model_clientes #Importa el modelo personas

render = web.template.render('application/views/clientes/', base='../principal/master') #Configura la ubicacion de las vistas