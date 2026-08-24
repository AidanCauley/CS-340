from pymongo import MongoClient
from urllib.parse import quote_plus


class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB."""

    def __init__(self, username="aacuser", password="aacpass"):
        # Connection variables
        HOST = "localhost"
        PORT = 27017
        DB = "aac"
        COL = "animals"

        # Initialize connection
        username = quote_plus(username)
        password = quote_plus(password)

        self.client = MongoClient(
            f"mongodb://{username}:{password}@{HOST}:{PORT}/?authSource=admin"
        )

        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """
        Insert a document into the animals collection.
        Returns True if successful, otherwise False.
        """
        if data is not None and isinstance(data, dict):
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print("Create error:", e)
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty.")

    def read(self, data):
        """
        Read documents from the animals collection.
        Returns a list of matching documents.
        """
        if data is not None and isinstance(data, dict):
            try:
                return list(self.collection.find(data))
            except Exception as e:
                print("Read error:", e)
                return []
        else:
            raise Exception("Nothing to read, because data parameter is empty.")

    def update(self, query, new_values):
        """
        Update documents in the animals collection.
        Returns the number of documents modified.
        """
        if query is not None and isinstance(query, dict):
            if new_values is not None and isinstance(new_values, dict):
                try:
                    result = self.collection.update_many(query, {"$set": new_values})
                    return result.modified_count
                except Exception as e:
                    print("Update error:", e)
                    return 0
            else:
                raise Exception("Nothing to update, because new_values parameter is empty.")
        else:
            raise Exception("Nothing to update, because query parameter is empty.")

    def delete(self, data):
        """
        Delete documents from the animals collection.
        Returns the number of documents deleted.
        """
        if data is not None and isinstance(data, dict):
            try:
                result = self.collection.delete_many(data)
                return result.deleted_count
            except Exception as e:
                print("Delete error:", e)
                return 0
        else:
            raise Exception("Nothing to delete, because data parameter is empty.")