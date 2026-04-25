# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username 
        PASS = password 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
    def get_next_record_number(self):
        """ Return the next available record number for the collection. Finds the highest existing rec_num value and return the next integer. Returns 1 if no records exist yet. """
        try:
            #Sort by rec_num descending and grab top document
            record = self.database.animals.find_one(
                {"rec_num": {"$exists": True}},
                sort=[("rec_num", -1)]
            )
            if record is not None:
                # Increment the highest existing record number by 1
                return record["rec_num"] + 1
            else:
                # No records with rec_num exist yet so start at 1
                return 1
        except Exception as e:
            # Print error and default to 1 when fails
            print("Error getting next record number: %s" % (e))
            return 1
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        """ Insert a document into the animals collection."""
        if data is not None: 
            try:
                # Insert document and check acknowledgement
                result = self.database.animals.insert_one(data)  # data should be dictionary
                
                # Return true is MongoDB acknowledged the write
                return result.acknowledged
            except Exception as e:
                # Print error and return false when fails
                print("Insert error: %s" % (e))
                return False
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD.
    def read(self, query):
        """ Query for documents from the animals collection."""
        if query is not None:
            try:
                # User find() to return all matching documents as cursor
                cursor = self.database.animals.find(query)
                
                # Convert the cursor to list and return it
                result = list(cursor)
                return result
            except Exception as e:
                # Print error and return empty list when fails
                print("Query error: %s" % (e))
                return []
        else:
            raise Exception("Nothing to query because query parameter is empty")
    
    # Create method to implement the U in Crud
    def update(self, query, update_data):
        """ Query for and update document or documents in the animals collection. """
        if query is not None and update_data is not None:
            try:
                # Use update_many() to update all documents matching the query
                result = self.database.animals.update_many(query, update_data)
                
                # Return the number of documents modified
                return result.modified_count
            except Exception as e:
                # Print error and return 0 when fails
                print("Update error: %s" % (e))
                return 0
        else:
            raise Exception("Nothing to update because query or update_data parameter is empty")
    
    # Create method to implement the D in CRUD
    def delete(self, query):
        """ Query for and remove document or documents from the animals collection. """
        if query is not None:
            try:
                # Use delete_many() to remove all documents matching the query
                result = self.database.animals.delete_many(query)
            
                # Return the number of documents deleted
                return result.deleted_count
            except Exception as e:
                # Print error and return 0 when fails
                print("Delete error: %s" % (e))
                return 0
        else:
            raise Exception("Nothing to delete because query parameter is empty")
        