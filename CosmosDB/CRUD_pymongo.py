import pymongo
import os
from bson.objectid import ObjectId

#Define the connection
url = "mongodb://iotdbaccount838:cOl25CnJVEonhsGShaSJZqCNYWPIR9j8mfcQLaloJwvy4oG5oZVF9aenWdUchYXHuRrLf2JZqwKOkcEeh9tzWg==@iotdbaccount838.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
client = pymongo.MongoClient(url)

db = client.iotdb.iotdbcollection

def readvalues():
    button1value = db.find_one({"id":"button1"})["value"]
    button2value = db.find_one({"id":"button2"})["value"]
    totalplayed = db.find_one({"id":"totalvotes"})["value"]
    print("Button 1 was pressed %s times.\nButton 2 was pressed %s times.\nThe total times this game has been played is %s times." %(button1value,button2value,totalplayed))

def reset():
    totalplayed = db.find_one({"id":"totalvotes"})["value"]
    totalplayed = int(totalplayed) + 1
    db.update_one({"id":"totalvotes"},{"$set": {"value":totalplayed}})
    db.update_one({"id":"button1"},{"$set": {"value":0}})
    db.update_one({"id":"button2"},{"$set": {"value":0}})

def start():
    db.delete_many({"id":"button1"})
    db.delete_many({"id":"button2"})
    db.delete_many({"id":"totalvotes"})
    db.insert_one({"id": "button1", "value": 0})
    db.insert_one({"id": "button2", "value": 0})
    db.insert_one({"id": "totalvotes", "value": 0})

def played(pressed):
    if "button1" in pressed.lower():
        button1 = db.find_one({"id":"button1"})["value"]
        button1 = int(button1) + 1
        db.update_one({"id":"button1"},{"$set": {"value":button1}})
    elif "button2" in pressed.lower():
        button2 = db.find_one({"id":"button2"})["value"]
        button2 = int(button2) + 1
        db.update_one({"id":"button2"},{"$set": {"value":button2}})
    elif "reset" in pressed.lower():
        reset()
    else:
        print("You didn't select the right option")
    print("***Current Values***")
    readvalues()

start()
readvalues()
#import pdb; pdb.set_trace();
