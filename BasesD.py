import sqlite3  #importamosla biblioteca quenos permite conoctarnos con sqlite3

def run_query(query, params = ()): #Creamos una funcion que recibe la consulta a hacer y los parametros
#Creamos y cerramos la conexion    
    with sqlite3.connect('mydatabases.db') as conn: #"mydatabases"  es el nombre de la base de datos
        cursor = conn.cursor() #Nos posicionamos  para recorrer la base de datos
        result = cursor.execute(query, params) #Ejecutamos la consulta
        conn.commit() # Ejecutamos la orden en la base de datos mediante la insruccion commit
    return result #Regresamos la consulta en caso de una busqueda

def select_record():#Funcion ejemplo de busqueda
    query = 'SELECT * FROM persona ORDER BY id' # Seleccionamos todos los datos de la tabla personas y los ordenamos por id
    db_row = run_query(query)#Llamamos la funcion que creamos, como no requerimos de parametros solo enviamos la consulta
    for row in db_row: #db_row contiene los resultados de la consulta, por lo tanto los mostramos con un for
    	print(row) # Mostramos la tupla que contiene cada fila, resultado de la consulta

def insert_record(): #Funcion para insertar un registro en la base de datos
	query = 'INSERT INTO persona VALUES (NULL, ?, ?)'#Codigo sql para insertar, por cada ? se debe introducir un elemento en la tupla params
	params = ('Jorge', 20) # Asignamosuna tupla con los valores a insertar en la consulta anterior
	run_query(query, params) # Llamamos a la funcion para ejecutar la consulta
	print('Datos actualizados')
	select_record()#Volvemos a mostrar los valores en la base de datos

select_record() #Llamamos a la funcion busqueda
insert_record() # Insertamos datos en La Base de Datos 