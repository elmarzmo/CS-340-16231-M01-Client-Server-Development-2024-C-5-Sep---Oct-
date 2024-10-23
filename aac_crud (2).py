from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
  """ CRUD operations for Animal collection in MongoDB """

  def __init__(self, username, password, host, port, database, collection):
    # Initializing the MongoClient. This helps to 
    # access the MongoDB databases and collections.
    # This is hard-wired to use the aac database, the 
    # animals collection, and the aac user.
    # Definitions of the connection string variables are
    # unique to the individual Apporto environment.
    #
    # You must edit the connection variables below to reflect
    # your own instance of MongoDB!
    #
    # Connection Variables
#
    USER = username
    PASS = password
    HOST = host
    PORT = port
    DB = database
    COL = collection
  #
    #  Initialize Connection
#
    self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
    self.database = self.client['%s' % (DB)]
    self.collection = self.database['%s' % (COL)]

  # Complete this create method to implement the C in CRUD.
  def create(self, data):
    """ Insert a document into MongoDB """
    try:
      result = self.collection.insert_one(data)
      return True if result.inserted_id else False
    except Exception as e:
      print(f"Error inserting document: {e}")
    return False
  




  # Create method to implement the R in CRUD.
  def read(self, query):
    """Query document from MongoDB"""
    try:
      cursor = self.collection.find(query)
      return list(cursor) #convert cursor to a list
    except Exception as e:
      print(f"Error quering document : {e}")
    return []
  def update(self, query, new_data):
    """Query document from MongoDB"""
    try:
      result = self.collection.update_many(query, {'$set': new_data})
      return result.modified_count
    except Exception as e:
      print(f"Error occured : {e}")
    return 0
  
  def delete(self, query):
    """Query document from MongoDB"""
    try:
      result = self.collection.delete_many(query)
      return result.deleted_count
    except Exception as e:
      print(f"Error occurred : {e}")
    return 0
 
  
      
      
      
      
