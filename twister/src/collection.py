from uuid import uuid4
from typing import Dict, List

class Collection:
    def __init__(self, collection_name: str):
        self.__id__ = str(uuid4())
        self._collection_name = collection_name
        
    @property
    def collection_name(self) -> str:
        return self._collection_name
    
    @collection_name.setter
    def collection_name(self, new_name: str) -> None:
        self._collection_name = new_name


class CollectionData:
    def __init__(self, collection_name: str, data: List[Dict]):
        self._collection_name = collection_name
        self._data = data
        self._changes = [False for _ in range(len(data))]