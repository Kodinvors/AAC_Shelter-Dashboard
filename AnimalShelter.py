from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """
    CRUD operations for Animal collection in MongoDB
    """

    def __init__(self, user, password, host, port, db, col):
        """
        Initializes the MongoClient and connects to database and collection.
        """
        self.client = MongoClient(f'mongodb://{user}:{password}@{host}:{port}')
        self.database = self.client[db]
        self.collection = self.database[col]

    def create(self, data):
        """
        Inserts a document into the MongoDB database and collection.
        """
        if data is not None:
            result = self.collection.insert_one(data)
            return True if result.inserted_id else False
        else:
            raise Exception("Create failed, no data entered")

    def read(self, query):
        """
        Search for documents from the MongoDB database and collection.
        """
        cursor = self.collection.find(query)
        result = [document for document in cursor]
        return result

# Example Usage
if __name__ == "__main__":
    # Connection Variables
    USER = 'aacuser'
    PASS = 'user'
    HOST = 'nv-desktop-services.apporto.com'
    PORT = 30813
    DB = 'AAC'
    COL = 'animals'

    # Instantiate the AnimalShelter class
    animal_shelter = AnimalShelter(USER, PASS, HOST, PORT, DB, COL)

    # Example data to insert
    data_to_insert = {
        'name': 'Kit',
        'animal_type': 'Cat',
        'age': 1,
        'breed': 'Lion'
    }

    # Test create method
    insert_result = animal_shelter.create(data_to_insert)
    print(f"Insert Result: {insert_result}")

    # Test read method
    query_criteria = {'name': 'Lion'}
    read_result = animal_shelter.read(query_criteria)
    print(f"Read Result: {read_result}")
