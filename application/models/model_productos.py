import config as config #Importa el archivo config

db = config.db #Crea un objeto db del objeto db creado en config

'''
Metodo para seleccionar todos los registros de la tabla productos
'''
def select_productos():
    try:
        return db.select('productos') #Selecciona todos los registros de la tabla productos
    except Exception as e:
        print "Model select_productos Error {}".format(e.args)
        print "Model select_productos Message {}".format(e.message)
        return None

def select_producto(id):
    try:
        return db.select('productos', where='id_producto=$id', vars=locals())[0] #Selecciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_id Error {}".format(e.args)
        print "Model select_id Message {}".format(e.message)
        return None

'''
Metodo para insertar un nuevo registro
'''
def insert_producto(id, nombreProducto, loteProducto, existenciaProducto, fechaCProducto):
    try:
        return db.insert('productos', 
        id_producto=id, 
        nombre_producto=nombreProducto, 
        lote_producto=loteProducto, 
        existencia_producto=existenciaProducto, 
        fecha_caducida_producto=fechaCProducto) #Insertar un registo de productos
    except Exception as e:
        print "Model insert_producto Error {}".format(e.args)
        print "Model insert_producto Message {}".format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el id del producto recibido
'''
def delete_producto(id):
    try:
        return db.delete('productos', where='id_producto=$id', vars=locals()) #Borra un registro de productos
    except Exception as e:
        print "Model delete_producto Error {}".format(e.args)
        print "Model delete_producto Message {}".format(e.message)
        return None

'''
Metodo para actualizar los datos del producto de acuerdo al id recibido
'''
def update_producto(id, nombreProducto, loteProducto, existenciaProducto, fechaCProducto):
    try:
        return db.update('productos', 
        nombre_producto=nombreProducto,
        lote_producto=loteProducto,
        existencia_producto=existenciaProducto,
        fecha_caducida_producto=fechaCProducto,
        where="id_producto=$id",
        vars=locals())
    except Exception as e:
        print "Model update_cliente Error {}".format(e.args)
        print "Model update_cliente Message {}".format(e.message)
        return None
