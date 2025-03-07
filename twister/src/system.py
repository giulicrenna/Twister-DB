from typing import List, Dict, Any
from twister.src.database import DataBase
from twister.src.collection import Collection

class TemporalCollections:
    def __init__(self):
        self.collections: List[Dict[str, Collection]] = []
        
    def __add_collection(self, collection: Collection) -> None:
        if collection._collection_name not in self.collections:
            self.collections[collection._collection_name] = collection
    
class System:
    def __init__(self):
        self.__databases__: Dict[str, DataBase] = {}
        
    def __add_database__(self, database: DataBase) -> None:
        if database.database_name not in [db.database_name for db in self.__databases__.values()]:
            self.__databases__[database.__id__] = database
        else:
            raise ValueError("Database already exists")

    def __get_id_by_name__(self, name: str) -> str:
        db_id = next((db.__id__ for db in self.__databases__.values() if db.database_name == name), None)
        
        if db_id is None:
            raise ValueError(f"Database '{name}' not found")
        
        return db_id
    
    def __list_databases__(self) -> List[str]:
        return [db.database_name for db in self.__databases__.values()]
    
    def __get_database__(self, name: str) -> DataBase:
        ...