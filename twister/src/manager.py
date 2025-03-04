import logging
import pickle
import os
from twister.src.collection import Collection, CollectionData
from twister.src.database import DataBase
from twister.src.system import System, TemporalCollections
from twister.src.register import Register
from twister.src.logger import Logger
from typing import Any

"""
TODO:
# Database
[X] Creation
[] Deletion
[] Update

# Collection
[X] Creation
[] Deletion
[] Modification

# Registers
[X] Creation
[] Deletion
[] Modification
[X] All data retrieval
[] Specific data retrieval
[] Regex data retrieval
[] Criteria data retrieval

# Miscelaneous
[] Data retrieval
[] Data update
[] Data deletion
[] Connections
"""

class Manager:
    def __init__(self, DB_PATH: str = "data", file_name: str = "database.tw") -> None:
        """
        Initialize the Manager instance.

        Args:
            DB_PATH (str): Directory path where the database file is stored.
            file_name (str): Name of the database file.
        """
        self.__DB_PATH__ = DB_PATH
        self.__file_name__ = file_name
        self.__system__: System = None
        self.__temporal_collections__: TemporalCollections = TemporalCollections()
        self.log_level = logging.DEBUG
        self.logger = Logger(loglevel=self.log_level)

        self.logger.info(f"Initializing Manager with DB_PATH: '{DB_PATH}', file_name: '{file_name}'")

        if not os.path.exists(DB_PATH):
            self.logger.debug(f"Directory '{DB_PATH}' does not exist. Creating directory.")
            os.mkdir(DB_PATH)

        if not os.path.isfile(f"{DB_PATH}/{file_name}"):
            self.logger.debug(f"File '{DB_PATH}/{file_name}' does not exist. Creating new system file.")
            self.__create__()

        self.__load_system__()
        self.logger.info("Manager initialized successfully.")

    def __create__(self) -> None:
        """
        Create a new system file with a serialized System object.
        """
        self.logger.info(f"Creating new system in file: '{self.__DB_PATH__}/{self.__file_name__}'")
        with open(f"{self.__DB_PATH__}/{self.__file_name__}", "wb") as file:
            new_system = System()
            pickle.dump(new_system, file)
        self.logger.debug("New system created and saved to file.")

    def __load_system__(self) -> None:
        """
        Load the System object from the database file.
        """
        self.logger.info(f"Loading system from file: '{self.__DB_PATH__}/{self.__file_name__}'")
        with open(f"{self.__DB_PATH__}/{self.__file_name__}", "rb") as file:
            self.__system__ = pickle.load(file)
        self.logger.debug("System loaded successfully.")

    def __modify_system__(self, new_object: Any) -> None:
        """
        Modify the first serialized object in the file without loading the entire file into memory.
        It reads and rewrites the file object by object using a temporary file.

        Args:
            new_object (Any): The new object to replace the first serialized object.
        """
        self.logger.info(f"Modifying system in file: '{self.__DB_PATH__}/{self.__file_name__}'")
        original_path = f"{self.__DB_PATH__}/{self.__file_name__}"
        temp_path = original_path + ".tmp"

        first_modified = False
        with open(original_path, "rb") as fin, open(temp_path, "wb") as fout:
            while True:
                try:
                    obj = pickle.load(fin)
                    if not first_modified and isinstance(obj, System):
                        self.logger.debug("Modifying first System object in the file.")
                        pickle.dump(new_object, fout)
                        first_modified = True
                    else:
                        pickle.dump(obj, fout)
                except EOFError:
                    self.logger.debug("Reached end of file during system modification.")
                    break

        os.replace(temp_path, original_path)
        self.logger.info("System modification complete and file replaced.")

    """
    REGISTER ZONE
    """
    def __create_register__(self, database_name: str, collection_name: str, data: dict) -> None:
        """
        Create a new register and add it to the collection.

        Args:
            collection_name (str): Name of the collection.
            data (dict): Data to be stored in the register.
        """
        self.logger.info(f"Creating new register in collection '{collection_name}'")
        
        if database_name not in self.__system__.__list_databases__():
            self.logger.error(f"Database '{database_name}' not found.")
            raise ValueError(f"Database '{database_name}' not found.")
        
        db_id = self.__system__.__get_id_by_name__(database_name)
        
        if collection_name not in self.__system__.__databases__[db_id].__list_collections__():
            self.logger.error(f"Collection '{collection_name}' not found in database '{database_name}'.")
            raise ValueError(f"Collection '{collection_name}' not found in database '{database_name}'.")
        
        collection_id = self.__system__.__databases__[db_id].__get_collection_id__(collection_name=collection_name)        
        
        new_register = Register(data=data, collection_id=collection_id, database_id=db_id)

        with open(f"{self.__DB_PATH__}/{self.__file_name__}", "ab") as file:
            pickle.dump(new_register, file)
        
        self.logger.info("System updated after adding new register.")
        
    """
    COLLECTION ZONE  
    """
    def __create_collection__(self, database_name: str, collection_name: str, create_db: bool = False) -> None:
        """
        Create a new collection and add it to the system.

        Args:
            collection_name (str): Name of the new collection.
        """
        self.logger.info(f"Creating new collection with name: '{collection_name}'")
        
        new_collection = Collection(collection_name=collection_name)
        
        self.logger.debug(f"Databases in system: {self.__system__.__list_databases__()}")
        
        if database_name not in self.__system__.__list_databases__() and create_db:
            self.logger.debug(f"Database '{database_name}' not found. Creating new database.")
            self.__create_database__(database_name)
        
        if database_name not in self.__system__.__list_databases__():
            self.logger.error(f"Database '{database_name}' not found.")
            
            raise ValueError(f"Database '{database_name}' not found.")
        
        db_id = self.__system__.__get_id_by_name__(database_name)
        
        self.__system__.__databases__[db_id].__add_collection__(new_collection)

        self.__modify_system__(self.__system__)
        
        self.logger.info("System updated after adding new collection.")
        
    def __get_collection_data__(self, collection_name, database_name) -> CollectionData:
        db_id = self.__system__.__get_id_by_name__(database_name)
        collection_id = self.__system__.__databases__[db_id].__get_collection_id__(collection_name)
        
        data = []
        
        with open(f"{self.__DB_PATH__}/{self.__file_name__}", "rb") as file:
            while True:
                try:
                    obj = pickle.load(file)
                    if isinstance(obj, Register) and obj.__collection_id__ == collection_id and obj.__database_id__ == db_id:
                        data.append(obj.__data__)
                except EOFError:
                    break
                
        return CollectionData(collection_name=collection_name, data=data)
    
    """
    DATABASE ZONE
    """
    def __create_database__(self, database_name: str) -> None:
        """
        Create a new database and add it to the system.

        Args:
            database_name (str): Name of the new database.
        """
        self.logger.info(f"Creating new database with name: '{database_name}'")
        new_database = DataBase(database_name=database_name)

        self.__system__.__add_database__(new_database)
        self.logger.debug(f"Database '{database_name}' added to system.")

        self.__modify_system__(self.__system__)
        self.logger.info("System updated after adding new database.")
