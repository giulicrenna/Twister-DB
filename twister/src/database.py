from uuid import uuid4
from typing import List
from twister.src.collection import Collection

class DataBase:
    def __init__(self, database_name: str):
        self.__id__ = str(uuid4())
        self.__collections__: List[Collection] = []
        self.database_name = database_name
    
    def __get_collection_id__(self, collection_name: str) -> str:
        """
        Retrieve the collection ID corresponding to the given collection name.

        Args:
            collection_name (str): The name of the collection.

        Returns:
            str: The ID of the collection.

        Raises:
            ValueError: If no collection with the given name is found.
        """
        collection_id = next(
            (collection.__id__ for collection in self.__collections__ if collection.collection_name == collection_name),
            None
        )
        if collection_id is None:
            raise ValueError(f"Collection '{collection_name}' not found")
        
        return collection_id
    
    def __add_collection__(self, collection: Collection) -> None:
        if collection.collection_name not in [col.collection_name for col in self.__collections__]:
            self.__collections__.append(collection)
        else:
            raise ValueError("Collection already exists")
    
    def __list_collections__(self) -> List[str]:
        return [collection.collection_name for collection in self.__collections__]
    
    def __get_collection__(self, collection_name: str) -> Collection:
        for collection in self.__collections__:
            if collection.collection_name == collection_name:
                return collection
        raise ValueError("Collection not found")
    
    def __remove_collection__(self, collection_name: str) -> None:
        for collection in self.__collections__:
            if collection.collection_name == collection_name:
                self.__collections__.remove(collection)
                return
        raise ValueError("Collection not found")