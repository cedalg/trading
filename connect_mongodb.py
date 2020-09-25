from pymongo import MongoClient

try:
    client = MongoClient('mongodb+srv://cedric:Casablanca1@cluster0.e1ph3.gcp.mongodb.net/test')
    print('Connected successfully :D')
except:
    print('Could not connect to MongoDB :(')