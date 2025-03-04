from typing import Any, Dict, List
from uuid import uuid4

class Register:
    def __init__(self, data: Dict[Any, Any], collection_id: str, database_id: str) -> None:
        self.uuid = str(uuid4())
        self.__data__ = data
        self.__collection_id__ = collection_id
        self.__database_id__ = database_id
        
        