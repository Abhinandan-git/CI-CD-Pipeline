from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")

uri = f"mongodb+srv://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@freecluster.9qe4tkg.mongodb.net/?retryWrites=true&w=majority&appName=FreeCluster"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
database = client['todo_database']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


def get_database():
  return database
