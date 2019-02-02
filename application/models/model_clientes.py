import config as config #Importa el archivo config

db = config.db #Crea un objeto db del objeto db creado en config

'''
Metodo para seleccionar todos los registros de la tabla personas
'''
def select_clientes():
    try:
        return db.select('clientes') #Selecciona todos los registros de la tabla personas
    except Exception as e:
        print "Model select_personas Error {}".format(e.args)
        print "Model select_personas Message {}".format(e.message)
        return None

def select_nombre(id):
    try:
        return db.select('clientes', where='id_cliente=$id', vars=locals())[0] #Selecciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_nombre Error {}".format(e.args)
        print "Model select_nombre Message {}".format(e.message)
        return None

'''
Metodo para insertar un nuevo registro
'''
def insert_cliente(id, nombreCliente, apellidoPC, apellidoMC, telefonoCliente, emailCliente):
    try:
        return db.insert('clientes', 
        id_cliente=id, 
        nombre_cliente=nombreCliente, 
        apellido_paterno_cliente=apellidoPC, 
        apellido_materno_cliente=apellidoMC, 
        telefono_cliente=telefonoCliente, 
        email_cliente=emailCliente) #Insertar un registo de clientes
    except Exception as e:
        print "Model insert_cliente Error {}".format(e.args)
        print "Model insert_cliente Message {}".format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el id del cliente recibido
'''
def delete_cliente(id):
    try:
        return db.delete('clientes', where='id_cliente=$id', vars=locals()) #Borra un registro de clientes
    except Exception as e:
        print "Model delete_cliente Error {}".format(e.args)
        print "Model delete_cliente Message {}".format(e.message)
        return None

'''
Metodo para actualizar los datos del cliente de acuerdo al id recibido
'''
def update_cliente(id, nombreCliente, apellidoPC, apellidoMC, telefonoCliente, emailCliente):
    try:
        return db.update('clientes', 
        nombre_cliente=nombreCliente,
        apellido_paterno_cliente=apellidoPC,
        apellido_materno_cliente=apellidoMC,
        telefono_cliente=telefonoCliente,
        email_cliente=emailCliente,
        where="id_cliente=$id",
        vars=locals())
    except Exception as e:
        print "Model update_cliente Error {}".format(e.args)
        print "Model update_cliente Message {}".format(e.message)
        return None
