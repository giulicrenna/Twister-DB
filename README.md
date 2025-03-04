# Twister DB

![logo]('')

A lightweight, local, and portable NoSQL database built with Python. Designed for fast and efficient storage, retrieval, and manipulation of structured data without the need for a traditional relational database system.

## Table of Contents

- [Twister DB](#twister-db)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Example](#example)
  - [License](#license)
  - [Contributing](#contributing)
  - [Development Checklist](#development-checklist)
  - [Roadmap](#roadmap)
  - [Contact](#contact)

## Features

- **Lightweight & Portable:** No heavy dependencies; easily moved across systems.
- **Local Storage:** Optimized for local data persistence.
- **NoSQL Approach:** Structured data management without traditional relational database overhead.
- **Simple API:** Intuitive methods for creating databases, collections, and registers.
- **Efficient:** Designed for fast data storage and retrieval.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/twister-db.git
   cd twister-db
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Tests (Optional):**
   ```bash
   python -m unittest discover
   ```

## Usage

Twister DB provides a straightforward API for managing your data. Here’s a basic overview:

- **Manager:** The central class to interact with the database system.
- **Database:** Represents a database instance.
- **Collection:** Represents a collection within a database.
- **Register:** Represents an individual data entry within a collection.

## Example

Below is a simple example to get started:

```python
from twister.src.manager import Manager

# Initialize the Manager with custom database path and file name
manager = Manager(DB_PATH="data", file_name="database.tw")

# Create a new database
manager.__create_database__("my_database")

# Create a new collection in the database (set create_db=True to auto-create the database if needed)
manager.__create_collection__("my_database", "my_collection", create_db=False)

# Insert a new register (document) into the collection
data = {"name": "John Doe", "age": 30}
manager.__create_register__("my_database", "my_collection", data)
```

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for full details.

## Contributing

Contributions are welcome! If you would like to contribute:

1. **Fork the Repository:** Create your own branch from the `main` branch.
2. **Create a Feature Branch:** Use a descriptive branch name for your feature or bug fix.
3. **Write Tests & Documentation:** Ensure your changes are covered by tests and documentation.
4. **Submit a Pull Request:** Provide a detailed description of your changes.

Please review our [Code of Conduct](CODE_OF_CONDUCT.md) for community guidelines.

## Development Checklist

- [x] Core functionality for creating databases and collections
- [x] Register creation and data insertion
- [x] Logging and error handling mechanisms
- [ ] Additional tests and extended documentation
- [ ] Enhanced error validation and user feedback
- [ ] User-friendly API improvements and examples

## Roadmap

- **v1.0 (Initial Release):**
  - Basic NoSQL database operations
  - File-based persistence using pickle
  - Logging integration

- **Future Enhancements:**
  - Advanced query capabilities and indexing
  - Performance optimizations
  - Enhanced error handling and user messaging
  - CLI or GUI interfaces for easier database management

## Contact

For any questions, suggestions, or issues, please reach out via [giulicrenna@gmail.com](mailto:giulicrenna@gmail.com).

---
