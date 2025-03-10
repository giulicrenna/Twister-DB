import os
import logging
from twister import Manager

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

DATA_DIR = "data"
DB_FILE = os.path.join(DATA_DIR, "database.tw")

def remove_existing_db_file(db_file: str) -> None:
    """Elimina el archivo de base de datos si existe."""
    if os.path.exists(db_file):
        try:
            os.remove(db_file)
            logging.info(f"Archivo de base de datos eliminado: {db_file}")
        except Exception as e:
            logging.error(f"Error al eliminar {db_file}: {e}")

def create_databases(manager: Manager, databases: list) -> None:
    """Crea las bases de datos especificadas."""
    for db in databases:
        try:
            manager.__create_database__(db)
            logging.info(f"Base de datos '{db}' creada exitosamente.")
        except ValueError as e:
            logging.warning(f"La base de datos '{db}' puede ya existir: {e}")

def create_collections(manager: Manager) -> None:
    """Crea las colecciones necesarias."""
    collections_to_create = [
        ("users", "user_data"),
        ("users", "user_products"),
        ("passwords", "user_data"),
    ]
    for database, collection in collections_to_create:
        try:
            manager.__create_collection__(database, collection)
            logging.info(f"Colección '{collection}' en la base '{database}' creada exitosamente.")
        except ValueError as e:
            logging.warning(f"La colección '{collection}' en la base '{database}' puede ya existir: {e}")

def insert_records(manager: Manager, database: str, collection: str, records: list) -> None:
    """Inserta los registros en la colección indicada."""
    for record in records:
        try:
            manager.__create_register__(database, collection, record)
            logging.info(f"Registro insertado en {database}.{collection}: {record}")
        except ValueError as e:
            logging.error(f"Error al insertar el registro {record} en {database}.{collection}: {e}")

def main():
    # Eliminar el archivo de base de datos existente si es que existe
    remove_existing_db_file(DB_FILE)

    # Instanciar el Manager
    manager = Manager(DATA_DIR)

    # Lista de bases de datos a crear
    databases = ["users", "products", "orders", "invoices", "payments"]

    # Crear bases de datos y colecciones
    create_databases(manager, databases)
    create_collections(manager)

    # Datos de prueba para usuarios y productos
    fake_records = [
        {"name": "John Doe", "email": "john.doe@example.com", "password": "password123"},
        {"name": "Jane Smith", "email": "jane.smith@example.com", "password": "password456"},
        {"name": "Alice Johnson", "email": "alice.johnson@example.com", "password": "password789"},
        {"name": "Bob Brown", "email": "bob.brown@example.com", "password": "password321"},
        {"name": "Charlie Davis", "email": "charlie.davis@example.com", "password": "password654"},
        {"name": "Diana Prince", "email": "diana.prince@example.com", "password": "wonderwoman"},
        {"name": "Bruce Wayne", "email": "bruce.wayne@example.com", "password": "batman"},
        {"name": "Clark Kent", "email": "clark.kent@example.com", "password": "superman"},
        {"name": "Barry Allen", "email": "barry.allen@example.com", "password": "flash"},
        {"name": "Hal Jordan", "email": "hal.jordan@example.com", "password": "greenlantern"},
        {"name": "Arthur Curry", "email": "arthur.curry@example.com", "password": "aquaman"},
        {"name": "Victor Stone", "email": "victor.stone@example.com", "password": "cyborg"},
    ]

    fake_products = [
        {
            "name": "Laptop",
            "description": "A high performance laptop with Intel i7 processor, 16GB RAM, and 512GB SSD.",
            "price": 999.99,
            "stock": 10,
        },
        {
            "name": "Smartphone",
            "description": "Latest model smartphone with 6.5-inch display and dual-camera system.",
            "price": 799.99,
            "stock": 15,
        },
        {
            "name": "Tablet",
            "description": "Portable tablet with a 10-inch screen, perfect for media consumption.",
            "price": 499.99,
            "stock": 20,
        },
        {
            "name": "Smartwatch",
            "description": "Feature-packed smartwatch with health tracking and GPS.",
            "price": 199.99,
            "stock": 25,
        },
        {
            "name": "Headphones",
            "description": "Noise-cancelling over-ear headphones with high-fidelity sound.",
            "price": 149.99,
            "stock": 30,
        },
        {
            "name": "Camera",
            "description": "DSLR camera with 24MP sensor and 4K video recording capabilities.",
            "price": 599.99,
            "stock": 8,
        },
        {
            "name": "Printer",
            "description": "All-in-one wireless printer with scanning and copying functions.",
            "price": 129.99,
            "stock": 12,
        },
        {
            "name": "Monitor",
            "description": "27-inch 4K UHD monitor with HDR support and ultra-thin bezel design.",
            "price": 349.99,
            "stock": 5,
        },
        {
            "name": "Keyboard",
            "description": "Mechanical keyboard with RGB backlight and programmable keys.",
            "price": 89.99,
            "stock": 18,
        },
        {
            "name": "Mouse",
            "description": "Ergonomic wireless mouse with adjustable DPI settings.",
            "price": 49.99,
            "stock": 22,
        },
        {
            "name": "Speaker",
            "description": "Bluetooth portable speaker with deep bass and long battery life.",
            "price": 59.99,
            "stock": 14,
        },
        {
            "name": "External Hard Drive",
            "description": "1TB USB 3.0 external hard drive for fast and reliable data storage.",
            "price": 79.99,
            "stock": 16,
        },
    ]

    # Insertar registros de usuarios y productos
    insert_records(manager, "users", "user_data", fake_records)
    insert_records(manager, "users", "user_products", fake_products)

    # Recuperar y mostrar los datos de la colección 'users.user_data'
    data_retrieve = manager.__get_collection_data__(database_name="users", collection_name="user_data")
    logging.info("Datos recuperados de 'users.user_data':")
    print(data_retrieve._data)

if __name__ == "__main__":
    main()
