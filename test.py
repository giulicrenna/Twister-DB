from twister import Manager
import os

os.remove("data/database.tw")

databases = ["users", "products", "orders", "invoices", "payments"]

fake_records = [
    {"name": "John Doe", "email": "john.doe@example.com", "password": "password123"},
    {
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "password": "password456",
    },
    {
        "name": "Alice Johnson",
        "email": "alice.johnson@example.com",
        "password": "password789",
    },
    {"name": "Bob Brown", "email": "bob.brown@example.com", "password": "password321"},
    {
        "name": "Charlie Davis",
        "email": "charlie.davis@example.com",
        "password": "password654",
    },
    {
        "name": "Diana Prince",
        "email": "diana.prince@example.com",
        "password": "wonderwoman",
    },
    {"name": "Bruce Wayne", "email": "bruce.wayne@example.com", "password": "batman"},
    {"name": "Clark Kent", "email": "clark.kent@example.com", "password": "superman"},
    {"name": "Barry Allen", "email": "barry.allen@example.com", "password": "flash"},
    {
        "name": "Hal Jordan",
        "email": "hal.jordan@example.com",
        "password": "greenlantern",
    },
    {
        "name": "Arthur Curry",
        "email": "arthur.curry@example.com",
        "password": "aquaman",
    },
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

if __name__ == "__main__":
    manager = Manager("data")

    for database in databases:
        try:
            manager.__create_database__(database)
        except ValueError as e:
            pass

    try:
        manager.__create_collection__("users", "user_data")
        manager.__create_collection__("users", "user_data")
        manager.__create_collection__("passwords", "user_data")
    except ValueError as e:
        pass

    for record in fake_records:
        try:
            manager.__create_register__("users", "user_data", record)
        except ValueError as e:
            print(f"Error creating record {record}: {e}")
            
    for record in fake_products:
        try:
            manager.__create_register__("users", "user_products", record)
        except ValueError as e:
            print(f"Error creating record {record}: {e}")


    data_retrieve = manager.__get_collection_data__(database_name="users", collection_name="user_data")
    print(data_retrieve._data)
    
