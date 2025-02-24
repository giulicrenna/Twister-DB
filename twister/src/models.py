from typing import List, Optional, Dict, Any
from uuid import uuid4


class Document:
    """Represents a document in a NoSQL database."""
    
    def __init__(self, data: Dict[str, Any], doc_id: Optional[str] = None):
        self.id = doc_id or str(uuid4())
        self.data = data

    def to_dict(self) -> Dict[str, Any]:
        """Returns the document as a dictionary."""
        return {"id": self.id, **self.data}


class Collection:
    """Represents a collection of documents."""
    
    def __init__(self, name: str):
        self.name = name
        self.documents: Dict[str, Document] = {}

    def __len__(self) -> int:
        """Returns the number of documents in the collection."""
        return len(self.documents)


class Database:
    """Represents a NoSQL database."""
    
    def __init__(self, name: str):
        self.name = name
        self.collections: Dict[str, Collection] = {}

    def __len__(self) -> int:
        """Returns the number of collections in the database."""
        return len(self.collections)
