'''
It's important the file name and the variable name are 'app' as when the command 'flask run' is passed the framework know what
you want to run.

This is being develop my following the udemy restful api course
 at https://www.udemy.com/course/rest-api-flask-and-python/learn/lecture/33781648?start=120#overview
'''

from flask import Flask, request
from db import items, stores
import uuid

#running the app will make any end points that we define available to the client
app = Flask(__name__)

#create an endpoint the '/store' is the endpoint and func associated the EP is 'get_stores'
@app.get("/store")
def get_stores():
    return {"stores":list(stores.values())}

#using the same endpoint but to post to.
@app.post("/store")
def create_store():
    #import the request module to interperate the json data in the payload
    store_data = request.get_json()
    #create a uuid for the object
    store_id = uuid.uuid4().hex
    #create a variable to sore the data from the payload
    new_store = {**store_data, "id": store_id}
    #add the data to our list in memory
    stores[store_id] = new_store
    #return our confrimation and response code 201(added)
    return new_store, 201


@app.post("/item")
def create_item():
    #use the request module to interperate the json data in the payload
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        return {"message": "Store not found"}, 404  
    
    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item      
    
    return new_item, 201

@app.get("/item")
def get_all_items():
    return {"stores":list(items.values())}

@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {"message": "store not found"}, 404

@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return {"message": "store not found"}, 404
