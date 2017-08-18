import pymongo
import os

#Define the connection
url = "{pythonmongodburl}"
client = pymongo.MongoClient(url)

db = client.iotdb.iotdbcollection
student_record = jsonobject

db.insert(student_record)

results = db.find()

#Loop through the results 
for record in results:
    print(record)

# close the connection to MongoDB
connection.close()