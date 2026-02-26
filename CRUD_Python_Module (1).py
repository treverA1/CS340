# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, USER, PASS): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        #USER = 'aacuser' 
        #PASS = 'SNHU1234' 
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
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        try:
            if data is not None: 
                self.database.animals.insert_one(data)  # data should be dictionary   
                return True
            else:
                raise Exception("Data Insert Failed")
        except Exception as e:
            print(f"Data Insert failed : {e}")
            return False

    # Create method to implement the R in CRUD.
    def read(self, query):
        try:
            if query is not None:
                AnimalList = self.database.animals.find(query)
                return list(AnimalList)
            else:
                raise Exception("Data Read Failed")
        except Exception as e:
            print(f"Data Read failed : {e}")
            return False
    
    #Update
    def update(self, query, new_values):
        try: 
            if query and new_values is not None:
                #use #set to change specific items in object
                result = self.database.animals.update_many(query, {"$set": new_values})
                #modified_count is a mongoDB variable that tracks the amount of changed items
            return result.modified_count
        
        except Exception as e:
            print(f"Data Update Failed: {e}")
            return
        
    #delete
    def delete(self, query):
        try:
            if query is not None:
                itemsDel = self.database.animals.delete_many(query)
            return itemsDel.deleted_count
        
        except Exception as e:
            print(f"Data delete failed: {e}")
            return