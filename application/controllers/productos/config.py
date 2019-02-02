import web
import application.models.model_productos as model_productos #Importa el modelo productos

render = web.template.render('application/views/productos/', base='../principal/master') #Configura la ubicacion de las vistas