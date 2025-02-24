import os
import pickle
from typing import Dict, Optional, Any
from twister.src.models import Document, Collection, Database


class CollectionManager:
    """Manages document storage in a collection using pickle."""
    
    def __init__(self, collection: Collection, db_path: str):
        self.collection = collection
        self.path = os.path.join(db_path, collection.name)
        os.makedirs(self.path, exist_ok=True)

    def _get_document_path(self, doc_id: str) -> str:
        """Returns the file path for a document."""
        return os.path.join(self.path, f"{doc_id}.pkl")

    def insert(self, data: Dict[str, Any]) -> str:
        """Inserts a new document and stores it on disk."""
        doc = Document(data)
        with open(self._get_document_path(doc.id), "wb") as f:
            pickle.dump(doc, f)
        return doc.id

    def find(self, doc_id: str) -> Optional[Document]:
        """Finds a document by ID without loading everything into RAM."""
        try:
            with open(self._get_document_path(doc_id), "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return None

    def delete(self, doc_id: str) -> bool:
        """Deletes a document from disk."""
        try:
            os.remove(self._get_document_path(doc_id))
            return True
        except FileNotFoundError:
            return False

    def update(self, doc_id: str, new_data: Dict[str, Any]) -> bool:
        """Updates a document by modifying its stored file."""
        doc = self.find(doc_id)
        if doc:
            doc.data.update(new_data)
            with open(self._get_document_path(doc_id), "wb") as f:
                pickle.dump(doc, f)
            return True
        return False

    def list_all(self) -> Dict[str, None]:
        """Returns a dictionary of all document IDs in the collection."""
        return {filename[:-4]: None for filename in os.listdir(self.path) if filename.endswith(".pkl")}


class DatabaseManager:
    """Manages multiple collections stored on disk."""
    
    def __init__(self, database: Database, db_path: str = "database"):
        self.database = database
        self.db_path = os.path.join(db_path, database.name)
        os.makedirs(self.db_path, exist_ok=True)

    def get_collection_manager(self, name: str) -> CollectionManager:
        """Returns a CollectionManager for a collection."""
        collection = Collection(name)
        return CollectionManager(collection, self.db_path)
