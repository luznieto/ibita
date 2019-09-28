from pymongo import MongoClient

MONGO_URI2="mongodb+srv://experto:experto@cluster0-vtd2f.azure.mongodb.net/test?retryWrites=true&w=majority"
agentes=MongoClient(MONGO_URI2)

def dbocb_connect(MONGO_URI2, db_name, col_name):
    agentes=MongoClient(MONGO_URI2)
    database=agentes[db_name]
    collection=database[col_name]
    return collection

def db_insert_ocb(collection, ocb):
	return collection.insert_one(ocb)


def dbocb_find_all(collection, query={}):
	return collection.find(query)



if __name__ == '__main__':
    print("MongoClient imported successfully!")
    #Creamos una base de datos llamada mip_app
    database=agentes['mip_app']
    #Creamos una colección llamada ocbs
    ocbs=database['ocb']

    ocb_demo={
        "agente": "Agrobacterium radiobacter strain K1026",
        "tipo": "Bacteria",
        "descrip": "Bactericida",
        "issue": "Agrobacterium tumefaciens; Agrobacterium rhizogenes",
        "culture":" Ornamental; Frutas; Nueces",
        "product":"Nogall",
        "certified":"EPA"
    }

    ocbs.insert_one(ocb_demo)