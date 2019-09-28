from pymongo import MongoClient

MONGO_URI1="mongodb+srv://admin:admin@cluster0-lhhnh.mongodb.net/test?retryWrites=true&w=majority"
client=MongoClient(MONGO_URI1)

def db_connect(MONGO_URI1, db_name, col_name):
	#crear variable cliente
	client=MongoClient(MONGO_URI1)
	database=client[db_name]
	collection=database[col_name]
	return collection

def db_insert_user(collection, user):
	return collection.insert_one(user)


def db_find_all(collection, query={}):
	return collection.find(query)



if __name__ == '__main__':
    print("MongoClient imported successfully!")
    #Creamos una base de datos llamada mi_app
    database=client['mi_app']
    #Creamos una colección llamada users
    users=database['users']

    usuario_demo={
        "user": "Josue Gil",
        "email": "joseugamez7@gmail.com"
    }

    users.insert_one(usuario_demo)