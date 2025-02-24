from twister.src.manager import DatabaseManager

# Crear la base de datos
db_manager = DatabaseManager(database="my_nosql_db")

# Obtener una colección
users_manager = db_manager.get_collection_manager("users")

# Insertar un documento
doc_id = users_manager.insert({"name": "Alice", "age": 25})
print(f"Inserted document with ID: {doc_id}")

# Buscar un documento
doc = users_manager.find(doc_id)
print(f"Found document: {doc.to_dict()}") if doc else print("Document not found")

# Actualizar un documento
users_manager.update(doc_id, {"age": 26})
print(f"Updated document: {users_manager.find(doc_id).to_dict()}")

# Listar todos los documentos sin cargarlos en memoria
print("Documents in collection:", users_manager.list_all())

# Eliminar un documento
users_manager.delete(doc_id)
print(f"Deleted document with ID: {doc_id}")

# Verificar eliminación
print("After deletion:", users_manager.list_all())
